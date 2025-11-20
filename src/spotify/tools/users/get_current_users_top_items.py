from src.spotify.tools.base import base_api_request

def get_current_users_top_items() -> tuple[callable, dict]:
    def function(type: str, time_range: str = None, limit: int = None, offset: int = None) -> str:
        route = f"/me/top/{type}"
        
        params = {}
        if time_range:
            params["time_range"] = time_range
        if limit:
            params["limit"] = limit
        if offset:
            params["offset"] = offset
            
        return base_api_request(route, "GET", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "get_current_users_top_items",
        "description": "Get the current user's top artists or tracks based on calculated affinity.",
        "parameters": {
            "type": "object",
            "properties": {
                "type": {
                    "type": "string",
                    "description": "The type of entity to return. Allowed values: 'artists', 'tracks'"
                },
                "time_range": {
                    "type": "string",
                    "description": "Over what time frame the affinities are computed. Valid values: 'long_term' (calculated from several years of data and including all new data as it becomes available), 'medium_term' (approximately last 6 months), 'short_term' (approximately last 4 weeks). Default: 'medium_term'"
                },
                "limit": {
                    "type": "integer",
                    "description": "The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50. Example: 10"
                },
                "offset": {
                    "type": "integer",
                    "description": "The index of the first item to return. Use with limit to get the next page of results. Default: 0. Example: 5"
                }
            },
            "required": ["type"]
        }
    }
    
    return function, tool_definition