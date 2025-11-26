from src.spotify.tools.base import base_api_request

def get_users_saved_albums() -> tuple[callable, dict]:
    def function(limit: int = None, offset: int = None) -> str:
        route = f"/me/albums"
        
        params = {}
        if limit:
            params["limit"] = limit
        if offset:
            params["offset"] = offset
    
        return base_api_request(route, "GET", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "spotify_get_users_saved_albums",
        "description": "Get a list of the albums saved in the current Spotify user's 'Your Music' library.",
        "parameters": {
            "type": "object",
            "properties": {
                "limit": {
                    "type": "integer",
                    "description": "The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50."
                },
                "offset": {
                    "type": "integer",
                    "description": "The index of the first item to return. Default: 0 (the first item). Use with limit to get the next set of items."
                }
            },
            "required": []
        }
    }
    
    return function, tool_definition
