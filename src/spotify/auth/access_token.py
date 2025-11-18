import base64
import requests
import json
from dotenv import load_dotenv

load_dotenv()

def get_and_save_access_token(client_id: str, client_secret: str, redirect_uri: str):
    combined_auth = f"{client_id}:{client_secret}"
    encoded_auth = base64.b64encode(combined_auth.encode()).decode()
    
    with open("src/spotify/auth/credentials/user_auth.json", "r") as f:
        auth_data = json.load(f)
        code = auth_data["code"]
    
    url = 'https://accounts.spotify.com/api/token'
    
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {encoded_auth}'
    }
    
    data = {
        'code': code,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code'
    }
    
    response = requests.post(url, headers=headers, data=data)
    
    with open("src/spotify/auth/credentials/access_token.json", "w") as f:
        json.dump(response.json(), f, indent=4)
