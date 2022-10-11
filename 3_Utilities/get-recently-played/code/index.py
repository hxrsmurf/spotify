from functions.player import get_recently_played_tracks
from functions.utils import handle_recently_played_tracks

def handler(event, context):
    recently_played_tracks = handle_recently_played_tracks(get_recently_played_tracks())
    return recently_played_tracks