from src.spotify.tools.base import base_api_request

def get_playback_state() -> tuple[callable, dict]:
    def function() -> str:
        route = f"/me/player"
        
        return base_api_request(route, "GET")
    
    tool_definition = {
        "type": "function",
        "name": "spotify_get_playback_state",
        "description": "Get information about the user's current playback state, including track or episode, progress, and active device.",
    }
    
    return function, tool_definition
