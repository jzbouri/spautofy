import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("LASTFM_USERNAME")

def get_current_user_username() -> tuple[callable, dict]:
    def function() -> str:
        return username
    
    tool_definition = {
        "type": "function",
        "name": "lastfm_get_current_user_username",
        "description": "Get the last.fm username of the current user."
    }
    
    return function, tool_definition