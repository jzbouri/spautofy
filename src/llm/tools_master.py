from src.spotify.tools.tools_manager import tools_dict as spotify_tools_dict
from src.lastfm.tools.tools_manager import tools_dict as lastfm_tools_dict

tools_dict = {
    **spotify_tools_dict,
    **lastfm_tools_dict
}

tools_definitions = [tool["tool_definition"] for tool in tools_dict.values()]
tools_definitions.append({"type": "web_search"})