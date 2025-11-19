from src.spotify.requests.base_request import base_request

def get_album() -> tuple[callable, dict]:
    def function(id: str) -> str:
        route = f"/albums/{id}"
        
        return base_request(route, "GET")
    
    tool_definition = {
        "type": "function",
        "name": "get_album",
        "description": "Get Spotify catalog information for a single album.",
        "parameters": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string",
                    "description": "The Spotify ID of the album. Example: 4aawyAB9vmqN3uQ7FjRGTy"
                }
            },
            "required": ["id"]
        }
    }
    
    return function, tool_definition