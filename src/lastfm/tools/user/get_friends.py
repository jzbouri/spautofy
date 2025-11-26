from src.lastfm.tools.base import base_api_request

def get_friends() -> tuple[callable, dict]:
    def function(user: str, recenttracks: bool = None, limit: int = None, page: int = None) -> str:
        
        params = {
            "method": "user.getfriends",
            "user": user
        }
        
        if recenttracks:
            params["recenttracks"] = int(recenttracks)
        if limit:
            params["limit"] = limit
        if page:
            params["page"] = page
            
        return base_api_request(method="GET", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "lastfm_get_friends",
        "description": "Get a list of the user's friends on Last.fm.",
        "parameters": {
            "type": "object",
            "properties": {
                "user": {
                    "type": "string",
                    "description": "The last.fm username to fetch the friends of."
                },
                "recenttracks": {
                    "type": "boolean",
                    "description": "Whether or not to include information about friends' recent listening in the response."
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