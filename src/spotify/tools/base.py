import requests
import json

with open("src/spotify/auth/credentials/access_token.json", "r") as f:
    access_token = json.load(f)["access_token"]

base_url = "https://api.spotify.com/v1"

def base_api_request(route: str, method: str, params: dict = None, body: dict = None, content_type: str = None):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    if content_type:
        headers["Content-Type"] = content_type
        
    if body and content_type != "image/jpeg":
        response = requests.request(method, f"{base_url}{route}", headers=headers, params=params, data=json.dumps(body))
    elif body:
        response = requests.request(method, f"{base_url}{route}", headers=headers, params=params, data=body)
    else:
        response = requests.request(method, f"{base_url}{route}", headers=headers, params=params)
  
    return response.text
