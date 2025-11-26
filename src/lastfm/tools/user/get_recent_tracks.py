from src.lastfm.tools.base import base_api_request

def get_recent_tracks() -> tuple[callable, dict]:
    def function(user: str, limit: int = None, page: int = None, from_date: int = None, to_date: int = None, extended: int = None) -> str:
        
        params = {
            "method": "user.getrecenttracks",
            "user": user,
        }
        
        if limit:
            params["limit"] = limit
        if page:
            params["page"] = page
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date
        if extended:
            params["extended"] = extended
            
        return base_api_request(method="GET", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "lastfm_get_recent_tracks",
        "description": "Get a list of the recent tracks listened to by this user. Also includes the currently playing track with the nowplaying=\"true\" attribute if the user is currently listening.",
        "parameters": {
            "type": "object",
            "properties": {
                "user": {
                    "type": "string",
                    "description": "The last.fm username to fetch the recent tracks of."
                },
                "limit": {
                    "type": "integer",
                    "description": "The number of results to fetch per page. Defaults to 50. Maximum is 200."
                },
                "page": {
                    "type": "integer",
                    "description": "The page number to fetch. Defaults to first page."
                },
                "from_date": {
                    "type": "integer",
                    "description": "Beginning timestamp of a range - only display scrobbles after this time, in UNIX timestamp format (integer number of seconds since 00:00:00, January 1st 1970 UTC)."
                },
                "to_date": {
                    "type": "integer",
                    "description": "End timestamp of a range - only display scrobbles before this time, in UNIX timestamp format (integer number of seconds since 00:00:00, January 1st 1970 UTC)."
                },
                "extended": {
                    "type": "integer",
                    "description": "Includes extended data in each artist, and whether or not the user has loved each track (0 or 1)."
                }
            },
            "required": ["user"]
        }
    }
    
    return function, tool_definition