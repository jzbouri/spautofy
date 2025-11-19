from src.spotify.tools.base import base_api_request

def toggle_playback_shuffle() -> tuple[callable, dict]:
    def function(state: bool, device_id: str = None) -> str:
        route = f"/me/player/shuffle"
        
        params = {}
        params["state"] = state
        if device_id:
            params["device_id"] = device_id
            
        return base_api_request(route, "PUT", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "toggle_playback_shuffle",
        "description": "Toggle shuffle on or off for the user's playback. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.",
        "parameters": {
            "type": "object",
            "properties": {
                "state": {
                    "type": "boolean",
                    "description": "true : Shuffle user's playback. false : Do not shuffle user's playback. Example: true"
                },
                "device_id": {
                    "type": "string",
                    "description": "The id of the device this command is targeting. If not supplied, the user's currently active device is the target. Example: 0d1841b0976bae2a3a310dd74c0f3df354899bc8"
                }
            },
            "required": ["state"]
        }
    }
    
    return function, tool_definition