from flask import Flask, render_template, request, redirect
import logging
from apis import SpotifyAPI, SpotifyAuthAPI, MusicbrainzAPI
from logger import build_logger
import random

app = Flask(__name__)

# make Flask only log messages that are ERROR-level
logging.getLogger('werkzeug').setLevel(logging.ERROR)

# custom logger
logger = build_logger("main")
logger("Please open Replit website in an external tab to make logging in work.")

# this token is the spotify access_token of the user we are currently serving
# this setup only allows us to serve one user at a time
token = None

alerted = False
@app.route("/")
def index():
    """
    Alerts what is needed to get Spotify API working on their site. Returns index page
    """
    global alerted
    if not alerted:
        alerted = True
        redirect_url = f"{request.base_url}callback"
        logger(f"Please make sure Spotify API allowed callbacks includes {redirect_url}")
        logger("Please also make sure your Spotify account is added as a user to the application's list of test users.")

    # check if the user is already logged in
    # if they are not, we make them log in to Spotify
    global token
    if token is None:
        return redirect("/login")

    # if they are logged in, the show the app
    try:
        profile = SpotifyAPI(token).get_profile()
        name = profile["display_name"] or "USERNAME"
        return render_template(
            "index.html", 
            name=name
        )
    except Exception as e:
        return render_template("error.html", error_message=e)

@app.route("/login")
def login():
    """
    Returns login page
    """
    return render_template("login.html")

@app.route("/logout")
def logout():
    """
    This endpoint logs out the current user by emptying the token. Returns back to login
    """
    global token
    token = None
    return redirect("/login")

@app.route('/authorize')
def authorize():
    """
    This endpoint will make the Spotify API create a redirect
    asking for permissions from the Spotify user to log in.
    Once the user grants the permissions, Spotify will redirect
    them back to our [/callback] endpoint
    """
    return redirect(SpotifyAuthAPI().get_login_url())

@app.route("/callback")
def callback():
    """
    This is the endpoint that Spotify redirects users back to
    after signing in and granting permissions. There would
    also be a code in the URL and we grab that to generate an
    access_token for the user via Spotify API
    """
    global token
    try:
        # retrieve the code and generate the access token
        code = request.args.get("code")
        token = SpotifyAuthAPI().get_access_token(code)
    except Exception as e:
        # if fail, make them log in again
        return render_template("error.html", error_message=e)

    # if everything goes smoothly, then return them to home
    logger("A user logged in!")
    return redirect("/")

@app.route("/top_artist")
def top_artist():
    """
    Get user's top artist using API and returns top_artist page
    """
    # before getting their top artist, make sure they are logged  in
    global token
    if token is None:
        return redirect("/login")

    # if they are, get one of their top artist
    try:
        results = SpotifyAPI(token).get_top_artists()
        artists = results["items"]

        # if their account is relatively new or rarely used
        # they may not have any top artists, so send them an error page
        if artists is None or len(artists) < 1:
            return render_template("error.html", error_message="No top artist found on account!")

        # if they do have top artists, randomly choose one and extract the specific info to display
        top = random.choice(artists)
        return render_template(
            "top_artist.html",
            artist_name=top["name"],
            artist_photo_url=top["images"][0]["url"],
            artist_id=top["id"]
        )
    except:
        pass
    return render_template("error.html", error_message="Failed to find top artist")

@app.route("/info/<artist_id>")
def info(artist_id):
    """
    Returns information about user's top artist using musicbrainz api
    """
    # make sure the user is logged in
    if token is None:
        return redirect("/login")

    try:
        # using the artist_id from the URL, we use Spotify API to get their name
        spotify_artist = SpotifyAPI(token).get_artist(artist_id)

        # use MusicBrainz API to lookup artists with matching name
        query_results = MusicbrainzAPI(spotify_artist["name"]).get()
        matching_artists = query_results["artists"]

        # if MusicBrainz can't find any
        if len(matching_artists) < 1:
            return render_template("error.html", error_message="Cannot find artist on MusicBrainz")

        # if they do find one, take the first result and display that
        top_artist = matching_artists[0]
        return render_template(
            "info.html",
            artist_id=artist_id,
            artist_name=top_artist["name"],
            artist_photo_url=spotify_artist["images"][0]["url"],
            artist_country=top_artist.get("country", "Unknown"),
            artist_genre=", ".join(spotify_artist["genres"]),
            artist_date=top_artist["life-span"].get("begin", "Unknown")
        )
    except Exception as e:
        return render_template("error.html", error_message=e)
    
@app.errorhandler(404)
def page_not_found(e):
    """
    Returns 404 error page
    """
    return render_template("404.html")

app.run("0.0.0.0", 8080)