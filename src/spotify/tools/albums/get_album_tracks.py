from src.spotify.tools.base import base_api_request

def get_album_tracks() -> tuple[callable, dict]:
    def function(id: str, limit: int = None, offset: int = None) -> str:
        route = f"/albums/{id}/tracks"
        
        params = {}
        if limit:
            params["limit"] = limit
        if offset:
            params["offset"] = offset
        
        return base_api_request(route, "GET", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "get_album_tracks",
        "description": "Get Spotify catalog information about an album's tracks. Optional parameters can be used to limit the number of tracks returned.",
        "parameters": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string",
                    "description": "The Spotify ID of the album. Example: 4aawyAB9vmqN3uQ7FjRGTy"
                },
                "limit": {
                    "type": "integer",
                    "description": "The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50."
                },
                "offset": {
                    "type": "integer",
                    "description": "The index of the first item to return. Default: 0 (the first item). Use with limit to get the next set of items."
                }
            },
            "required": ["id"]
        }
    }
    
    return function, tool_definition