from datetime import datetime
import random

def handle_saved_tracks(all_tracks):
    list_of_tracks = []
    for tracks in all_tracks:
        for item in tracks['items']:
            track = item['track']
            name = track['name']
            id = track['id']
            uri = track['uri']
            track_number = track['track_number']
            added_at = item['added_at']
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

def shuffle_tracks(tracks):
    new_track_list = []
    random.shuffle(tracks)

    tracks_added = 0
    maximum_tracks = 100

    for track in tracks:
        new_track_list.append(track['uri'])
        tracks_added += 1

        if tracks_added == 100:
            break

    return new_track_list

def current_year_month_day():
    return datetime.utcnow().strftime('%Y-%m-%d')