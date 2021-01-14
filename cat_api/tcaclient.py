import os
import requests


class TCAClient:
    base_uri = "https://api.thecatapi.com/v1"
    headers = {"Content-Type": "application/json"}

    def __init__(self, api_key=None):
        self.headers.update(
            {"x-api-key": api_key or os.environ.get("CAT_API_KEY")}
        )

    def get_breeds(self):
        uri = self.base_uri + "/breeds"
        req = requests.get(uri, headers=self.headers)
        req.raise_for_status()
        
        return req.json()
