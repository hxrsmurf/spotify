from audioop import add
from tkinter import N


def handle_saved_tracks(tracks):
    list_of_tracks = []
    for tracks in tracks['items']:
        track = tracks['track']
        name = track['name']
        id = track['id']
        uri = track['uri']
        track_number = track['track_number']
        added_at = track['added_at']
        artist = track['artists'][0]['name']

        list_of_tracks.append({
            'name': name,
            'id': id,
            'uri': uri,
            'track_number': track_number,
            'added_at': added_at,
            'artist': artist
        })

    return list_of_tracks