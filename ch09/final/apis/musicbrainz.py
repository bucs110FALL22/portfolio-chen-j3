import requests as R

class MusicbrainzAPI:
    def __init__(self, artistName):
    """
    transfers randomized artist name (string) to musicbrainz api
    """
        self.url = f"https://musicbrainz.org/ws/2/artist?query={artistName}&fmt=json"
        self.headers = {
            "Content-Type": "application/json"
        }

    def get(self):
      """
      returns response from musicbrainz api (information on randomized artist)
      """
        response = R.get(
            self.url, 
            headers=self.headers
        )
        return response.json()