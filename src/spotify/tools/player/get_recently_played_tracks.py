from src.spotify.tools.base import base_api_request

def get_recently_played_tracks() -> tuple[callable, dict]:
    def function(limit: int = None, after: int = None, before: int = None) -> str:
        route = f"/me/player/recently-played"
        
        params = {}
        if limit:
            params["limit"] = limit
        if after:
            params["after"] = after
        if before:
            params["before"] = before
            
        return base_api_request(route, "GET", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "spotify_get_recently_played_tracks",
        "description": "Get the tracks recently played by the user. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.",
        "parameters": {
            "type": "object",
            "properties": {
                "limit": {
                    "type": "integer",
                    "description": "The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50. Default: limit=20.Range: 0 - 50. Example: 10"
                },
                "after": {
                    "type": "integer",
                    "description": "A Unix timestamp in milliseconds. Returns all items after (but not including) this cursor position. If after is specified, before must not be specified. Example: 1484811043508"
                },
                "before": {
                    "type": "integer",
                    "description": "A Unix timestamp in milliseconds. Returns all items before (but not including) this cursor position. If before is specified, after must not be specified."
                }
            },
            "required": []
        }
    }
    
    return function, tool_definition
