from src.spotify.tools.base import base_api_request

def skip_to_next() -> tuple[callable, dict]:
    def function(device_id: str = None) -> str:
        route = f"/me/player/next"
        
        params = {}
        if device_id:
            params["device_id"] = device_id
            
        return base_api_request(route, "POST", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "skip_to_next",
        "description": "Skips to next track in the user's queue. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.",
        "parameters": {
            "type": "object",
            "properties": {
                "device_id": {
                    "type": "string",
                    "description": "The id of the device this command is targeting. If not supplied, the user's currently active device is the target. Example: 0d1841b0976bae2a3a310dd74c0f3df354899bc8"
                }
            },
            "required": []
        }
    }
    
    return function, tool_definition