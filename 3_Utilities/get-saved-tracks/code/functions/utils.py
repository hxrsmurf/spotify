from datetime import datetime
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

def current_year_month_day():
    return datetime.utcnow().strftime('%Y-%m-%d')