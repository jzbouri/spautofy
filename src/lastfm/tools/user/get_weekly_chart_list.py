from src.lastfm.tools.base import base_api_request

def get_weekly_chart_list() -> tuple[callable, dict]:
    def function(user: str) -> str:
        
        params = {
            "method": "user.getweeklychartlist",
            "user": user
        }
        
        return base_api_request(method="GET", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "lastfm_get_weekly_chart_list",
        "description": "Get a list of available charts for this user, expressed as date ranges which can be sent to the chart services.",
        "parameters": {
            "type": "object",
            "properties": {
                "user": {
                    "type": "string",
                    "description": "The last.fm username to fetch the charts list for."
                }
            },
            "required": ["user"]
        }
    }
    
    return function, tool_definition