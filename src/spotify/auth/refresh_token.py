import base64
import requests
import json

def get_and_save_refresh_token(client_id: str, client_secret: str) -> None:
    with open("src/spotify/auth/credentials/access_token.json", "r") as f:
        current_refresh_token = json.load(f)["refresh_token"]
    
    combined_auth = f"{client_id}:{client_secret}"
    encoded_auth = base64.b64encode(combined_auth.encode()).decode()
    
    url = "https://accounts.spotify.com/api/token"
    
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {encoded_auth}'
    }
    
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': current_refresh_token
    }
    
    response = requests.post(url, headers=headers, data=data)
    response_json = response.json()
    
    if "refresh_token" in response_json:
        with open("src/spotify/auth/credentials/access_token.json", "w") as f:
            json.dump(response.json(), f, indent=4)
