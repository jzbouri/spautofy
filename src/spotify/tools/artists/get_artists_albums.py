from src.spotify.tools.base import base_api_request

def get_artists_albums() -> tuple[callable, dict]:
    def function(id: str, include_groups: str = None, limit: int = None, offset: int = None) -> str:
        route = f"/artists/{id}/albums"
        
        params = {}
        if include_groups:
            params["include_groups"] = include_groups
        if limit:
            params["limit"] = limit
        if offset:
            params["offset"] = offset
        
        return base_api_request(route, "GET", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "get_artists_albums",
        "description": "Get Spotify catalog information about an artist's albums.",
        "parameters": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string",
                    "description": "The Spotify ID of the artist. Example: 0TnOYISbd1XYRBk9myaseg"
                },
                "include_groups": {
                    "type": "string",
                    "description": "A comma-separated list of keywords that will be used to filter the response. If not supplied, all album types will be returned. Valid values: 'album', 'single', 'appears_on', 'compilation'. For example: 'album,single'."
                },
                "limit": {
                    "type": "integer",
                    "description": "The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50. Example: 10"
                },
                "offset": {
                    "type": "integer",
                    "description": "The index of the first item to return. Default: 0 (the first item). Use with limit to get the next set of items. Example: 5"
                }
            },
            "required": ["id"]
        }
    }
    
    return function, tool_definition