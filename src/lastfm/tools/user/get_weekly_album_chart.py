from src.lastfm.tools.base import base_api_request

def get_weekly_album_chart() -> tuple[callable, dict]:
    def function(user: str, from_date: int = None, to_date: int = None) -> str:
        
        params = {
            "method": "user.getweeklyalbumchart",
            "user": user
        }
        
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date
            
        return base_api_request(method="GET", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "lastfm_get_weekly_album_chart",
        "description": "Get an album chart for a user profile, for a given date range. If no date range is supplied, it will return the most recent album chart for this user.",
        "parameters": {
            "type": "object",
            "properties": {
                "user": {
                    "type": "string",
                    "description": "The last.fm username to fetch the charts of."
                },
                "from_date": {
                    "type": "integer",
                    "description": "The date at which the chart should start from. (UNIX timestamp)"
                },
                "to_date": {
                    "type": "integer",
                    "description": "The date at which the chart should end on. (UNIX timestamp)"
                }
            },
            "required": ["user"]
        }
    }
    
    return function, tool_definition