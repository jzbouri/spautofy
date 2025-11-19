from src.spotify.requests.base_request import base_request

def get_currently_playing_track() -> tuple[callable, dict]:
    def function() -> str:
        route = f"/me/player/currently-playing"
        
        return base_request(route, "GET")
    
    tool_definition = {
        "type": "function",
        "name": "get_currently_playing_track",
        "description": "Get the object currently being played on the user's Spotify account."
    }
    
    return function, tool_definition