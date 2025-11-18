import secrets
import os
import json
from flask import Flask, request, redirect
from urllib.parse import urlencode

app = Flask(__name__)

with open("src/spotify/auth/scopes.txt", "r") as f:
    scopes = f.read().splitlines()

@app.route("/login")
def login():
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")
    
    state = secrets.token_hex(16)
    scope = " ".join(scopes)

    url = "https://accounts.spotify.com/authorize?" + urlencode({
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "scope": scope,
        "state": state
    })

    return redirect(url)

@app.route("/")
def callback():
    code = request.args.get("code")
    state = request.args.get("state")

    with open("src/spotify/auth/credentials/user_auth.json", "w") as f:
        json.dump({"code": code, "state": state}, f, indent=4)

    return "User authorization complete"

if __name__ == "__main__":
    app.run(port=3000, debug=False, use_reloader=False)
