from src.lastfm.tools.base import base_api_request

def get_top_albums() -> tuple[callable, dict]:
    def function(user: str, period: str = None, limit: int = None, page: int = None) -> str:
        
        params = {
            "method": "user.gettopalbums",
            "user": user
        }
        
        if period:
            params["period"] = period
        if limit:
            params["limit"] = limit
        if page:
            params["page"] = page
            
        return base_api_request(method="GET", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "lastfm_get_top_albums",
        "description": "Get the top albums listened to by a user. You can stipulate a time period. Sends the overall chart by default.",
        "parameters": {
            "type": "object",
            "properties": {
                "user": {
                    "type": "string",
                    "description": "The user name to fetch top albums for."
                },
                "period": {
                    "type": "string",
                    "enum": ["overall", "7day", "1month", "3month", "6month", "12month"],
                    "description": "The time period over which to retrieve top albums for."
                },
                "limit": {
                    "type": "integer",
                    "description": "The number of results to fetch per page. Defaults to 50."
                },
                "page": {
                    "type": "integer",
                    "description": "The page number to fetch. Defaults to first page."
                }
            },
            "required": ["user"]
        }
    }
    
    return function, tool_definition