from src.spotify.requests.base_request import base_request

def get_playback_state() -> tuple[callable, dict]:
    def function() -> str:
        route = f"/me/player"
        
        return base_request(route, "GET")
    
    tool_definition = {
        "type": "function",
        "name": "get_playback_state",
        "description": "Get information about the user's current playback state, including track or episode, progress, and active device.",
    }
    
    return function, tool_definition
