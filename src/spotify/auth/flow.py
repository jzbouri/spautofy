import subprocess
import webbrowser
import time
import os
import shutil
from dotenv import load_dotenv

from src.spotify.auth.access_token import get_and_save_access_token

load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

if client_id is None or client_secret is None or redirect_uri is None:
    raise ValueError("SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, and SPOTIFY_REDIRECT_URI are required")

def auth_flow():
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
