import requests as R

class SpotifyAPI:
    def __init__(self, access_token):
        """
      This endpoint logs out the current user by emptying the token
      """
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
    def get_artist(self, id):
        response = R.get(
            f"https://api.spotify.com/v1/artists/{id}", 
            headers=self.headers
        )
        return response.json()
      
    def get_profile(self):
        response = R.get(
            "https://api.spotify.com/v1/me", 
            headers=self.headers
        )
        return response.json()

    def get_top_artists(self):
        response = R.get(
            "https://api.spotify.com/v1/me/top/artists",
            headers=self.headers
        )
        return response.json()