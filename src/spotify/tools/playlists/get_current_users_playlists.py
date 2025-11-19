from src.spotify.tools.base import base_api_request

def get_current_users_playlists() -> tuple[callable, dict]:
    def function(limit: int = None, offset: int = None) -> str:
        route = f"/me/playlists"
        
        params = {}
        if limit:
            params["limit"] = limit
        if offset:
            params["offset"] = offset
            
        return base_api_request(route, "GET", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "get_current_users_playlists",
        "description": "Get a list of the playlists owned or followed by a Spotify user.",
        "parameters": {
            "type": "object",
            "properties": {
                "limit": {
                    "type": "integer",
                    "description": "The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50. Example: 10"
                },
                "offset": {
                    "type": "integer",
                    "description": "The index of the first playlist to return. Default: 0 (the first object). Maximum offset: 100000. Use with limit to get the next set of playlists."
                }
            },
            "required": []
        }
    }
    
    return function, tool_definition