import requests as R

class SpotifyAPI:
    def __init__(self, access_token):
        """
      takes access_token (string) to initialize spotify api
      """
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
      
    def get_artist(self, id):
        """
        uses id (integer) to return the artist from spotify api
        """
        response = R.get(
            f"https://api.spotify.com/v1/artists/{id}", 
            headers=self.headers
        )
        return response.json()
      
    def get_profile(self):
        """
        returns the spotify user profile
        """
        response = R.get(
            "https://api.spotify.com/v1/me", 
            headers=self.headers
        )
        return response.json()

    def get_top_artists(self):
        """
        returns the information of the user's top spotify artists
        """
        response = R.get(
            "https://api.spotify.com/v1/me/top/artists",
            headers=self.headers
        )
        return response.json()