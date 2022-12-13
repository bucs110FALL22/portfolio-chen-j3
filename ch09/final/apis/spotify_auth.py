from os import environ
import requests as R
from base64 import b64encode

class SpotifyAuthAPI:
    REDIRECT_URI = "https://fe2c8b3d-4a98-4ff9-8c0b-b402f2f20bf6.id.repl.co/callback"
    
    def __init__(self):
        pass

    def get_login_url(self):
        """
        returns response.url
        """
        url_params = {
            "response_type": "code",
            "client_id": environ["SPOTIFY_CLIENT_ID"],
            "scope": " ".join([
                "user-library-read",
                "user-read-email",
                "user-top-read",
                "user-follow-read"
            ]),

            "redirect_uri": SpotifyAuthAPI.REDIRECT_URI
        }
        response = R.get(
            "https://accounts.spotify.com/authorize", 
            params=url_params
        )
        return response.url

    def get_access_token(self, code):
        """
        method called after start_authorization to finish logging the user into the app with the code we got from spotify api
        """
        client_id = environ["SPOTIFY_CLIENT_ID"]
        client_secret = environ["SPOTIFY_CLIENT_SECRET"]
        encoded_credentials = b64encode(f"{client_id}:{client_secret}".encode()).decode("utf-8")

        # get the access token
        response = R.post(
            "https://accounts.spotify.com/api/token", 
            data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": SpotifyAuthAPI.REDIRECT_URI
            }, 
            headers={
                "Authorization": f"Basic {encoded_credentials}",
                "Content-Type": "application/x-www-form-urlencoded"
            }
        )

        info = response.json()
        return info["access_token"]
