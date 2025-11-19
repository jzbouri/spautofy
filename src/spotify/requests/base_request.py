import requests
import json

with open("src/spotify/auth/credentials/access_token.json", "r") as f:
    access_token = json.load(f)["access_token"]

base_url = "https://api.spotify.com/v1"

def base_request(route: str, method: str, params: dict = None, body: dict = None):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    if body is not None:
        response = requests.request(method, f"{base_url}{route}", headers=headers, params=params, data=json.dumps(body))
    else:
        response = requests.request(method, f"{base_url}{route}", headers=headers, params=params)
    
    print(response.status_code)
    return response.text
