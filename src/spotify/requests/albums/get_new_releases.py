from src.spotify.requests.base_request import base_request

def get_new_releases() -> tuple[callable, dict]:
    def function(limit: int = None, offset: int = None) -> str:
        route = f"/browse/new-releases"
        
        params = {}
        if limit:
            params["limit"] = limit
        if offset:
            params["offset"] = offset
        
        return base_request(route, "GET", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "get_new_releases",
        "description": "Get a list of new album releases featured in Spotify (shown, for example, on a Spotify player's “Browse” tab).",
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