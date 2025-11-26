from src.spotify.tools.base import base_api_request

def start_or_resume_playback() -> tuple[callable, dict]:
    def function(device_id: str = None, context_uri: str = None, uris: list[str] = None, offset: dict = None, position_ms: int = None) -> str:
        route = f"/me/player/play"
        
        params = {}
        if device_id:
            params["device_id"] = device_id
            
        body = {}
        if context_uri:
            body["context_uri"] = context_uri
        if uris:
            body["uris"] = uris
        if offset:
            body["offset"] = offset
        if position_ms is not None:
            body["position_ms"] = position_ms
            
        print(body)
        
        return base_api_request(route, "PUT", params=params, body=body)
    
    tool_definition = {
        "type": "function",
        "name": "spotify_start_or_resume_playback",
        "description": "Start a new context or resume current playback on the user's active device. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.",
        "parameters": {
            "type": "object",
            "properties": {
                "device_id": {
                    "type": "string",
                    "description": "The id of the device this command is targeting. If not supplied, the user's currently active device is the target. Example: 0d1841b0976bae2a3a310dd74c0f3df354899bc8"
                },
                "context_uri": {
                    "type": "string",
                    "description": "Optional. Spotify URI of the context to play. Valid contexts are albums, artists & playlists. Example: {context_uri:spotify:album:1Je1IMUlBXcx1Fz0WE7oPT}"
                },
                "uris": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Optional. A JSON array of the Spotify track URIs to play. For example: {uris: ['spotify:track:4iV5W9uYEdYUVa79Axb7Rh', 'spotify:track:1301WleyT98MSxVHPZCA6M']}"
                },
                "offset": {
                    "type": "string",
                    "description": "Optional. Indicates from where in the context playback should start. Only available when context_uri corresponds to an album or playlist object. \"position\" is zero based and can't be negative. Example: {offset: {position: 5}} \"uri\" is a string representing the uri of the item to start at. Example: {offset: {uri: 'spotify:track:1301WleyT98MSxVHPZCA6M'}}"
                },
                "position_ms": {
                    "type": "integer"
                }
            },
            "required": ["device_id"]
        }
    }
    
    return function, tool_definition
