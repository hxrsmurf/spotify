from functions.authorization import get_access_token
from functions.player import get_saved_tracks
from functions.utils import handle_saved_tracks

def handler(event, context):
    access_token = get_access_token()
    tracks = get_saved_tracks()
    result_saved_tracks = handle_saved_tracks(tracks)
    print(result_saved_tracks)