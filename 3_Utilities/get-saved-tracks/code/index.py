from functions.authorization import get_access_token
from functions.player import get_saved_tracks
from functions.utils import handle_saved_tracks
from functions.playlist import create_playlist

import random

def handler(event, context):
    tracks = get_saved_tracks(get_access_token())
    result_saved_tracks = handle_saved_tracks(tracks)
    random.shuffle(result_saved_tracks)
    #new_playlist_id = create_playlist(get_access_token())
    for track in result_saved_tracks:
        print(track)