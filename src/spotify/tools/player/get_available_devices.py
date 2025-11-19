from src.spotify.tools.base import base_api_request

def get_available_devices() -> tuple[callable, dict]:
    def function() -> str:
        route = f"/me/player/devices"
        
        return base_api_request(route, "GET")
    
    tool_definition = {
        "type": "function",
        "name": "get_available_devices",
        "description": "Get information about a user's available Spotify Connect devices. Some device models are not supported and will not be listed in the API response."
    }
    
    return function, tool_definition