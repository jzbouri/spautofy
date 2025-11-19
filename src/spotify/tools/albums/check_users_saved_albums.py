from src.spotify.tools.base import base_api_request

def check_users_saved_albums() -> tuple[callable, dict]:
    def function(ids: list[str]) -> str:
        route = f"/me/albums/contains"
    
        params = {}
        params["ids"] = ids
        
        return base_api_request(route, "GET", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "check_users_saved_albums",
        "description": "Check if one or more albums is already saved in the current Spotify user's 'Your Music' library.",
        "parameters": {
            "type": "object",
            "properties": {
                "ids": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "An array of the Spotify IDs for the albums. Maximum: 20 IDs. Example: ['382ObEPsp2rxGrnsizN5TX', '1A2GTWGtFfWp7KSQTwWOyo', '2noRn2Aes5aoNVsU6iWThc']"
                }
            },
            "required": ["ids"]
        }
    }
    
    return function, tool_definition