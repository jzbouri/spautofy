from src.lastfm.tools.custom.get_current_user_username import get_current_user_username

from src.lastfm.tools.user.get_info import get_info
from src.lastfm.tools.user.get_recent_tracks import get_recent_tracks
from src.lastfm.tools.user.get_friends import get_friends
from src.lastfm.tools.user.get_top_artists import get_top_artists
from src.lastfm.tools.user.get_top_tags import get_top_tags
from src.lastfm.tools.user.get_top_tracks import get_top_tracks
from src.lastfm.tools.user.get_weekly_album_chart import get_weekly_album_chart
from src.lastfm.tools.user.get_weekly_artist_chart import get_weekly_artist_chart
from src.lastfm.tools.user.get_weekly_chart_list import get_weekly_chart_list
from src.lastfm.tools.user.get_weekly_track_chart import get_weekly_track_chart

tools_functions = [
    get_current_user_username,
    get_info,
    get_recent_tracks,
    get_friends,
    get_top_artists,
    get_top_tags,
    get_top_tracks,
    get_weekly_album_chart,
    get_weekly_artist_chart,
    get_weekly_chart_list,
    get_weekly_track_chart,
]

tools_dict = {}

for tool_function in tools_functions:
    function, tool_definition = tool_function()
    tools_dict[tool_definition["name"]] = {
        "function": function,
        "tool_definition": tool_definition
    }