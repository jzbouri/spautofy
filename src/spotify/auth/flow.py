import subprocess
import webbrowser
import time
import os
from dotenv import load_dotenv
import json
import shutil

from src.spotify.auth.access_token import get_and_save_access_token
from src.spotify.auth.refresh_token import get_and_save_refresh_token

load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

if client_id is None or client_secret is None or redirect_uri is None:
    raise ValueError("SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, and SPOTIFY_REDIRECT_URI are required")

def auth_flow():
    if os.path.exists("src/spotify/auth/credentials") and "access_token.json" in os.listdir("src/spotify/auth/credentials"):
        with open("src/spotify/auth/credentials/access_token.json", "r") as f:
            if "refresh_token" in json.load(f):
                get_and_save_refresh_token(client_id, client_secret)
                return

    if os.path.exists("src/spotify/auth/credentials"):
        shutil.rmtree("src/spotify/auth/credentials")
    os.makedirs("src/spotify/auth/credentials")
    
    flask_process = subprocess.Popen(
        ["python", "src/spotify/auth/user_auth.py"],
        start_new_session=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    
    time.sleep(1)
    webbrowser.open("http://localhost:3000/login")
    
    while True:
        if os.path.exists("src/spotify/auth/credentials/user_auth.json"):
            flask_process.terminate()
            break
        time.sleep(1)

    get_and_save_access_token(client_id, client_secret, redirect_uri)
