import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("LASTFM_API_KEY")

base_url = "https://ws.audioscrobbler.com/2.0/"

def base_api_request(method: str, route: str = "", params: dict = None, body: dict = None):
    
    if params is None:
        params = {}
        
    params["api_key"] = api_key
    params["format"] = "json"
    
    response = requests.request(method, f"{base_url}{route}", params=params, data=body)
    
    return response.text
