import json

def handle_recently_played_tracks(recently_played_tracks_json):
    list_of_tracks = []
    for tracks in recently_played_tracks_json['items']:
        track = tracks['track']
        name = track['name']
        artist_name = track['artists'][0]['name']
        artist_id = track['artists'][0]['id']
        played_at = tracks['played_at']
        context_type = tracks['context']['type']
        context_uri = tracks['context']['uri']

        #print(name, artist_id, artist_name, played_at, context_type, context_uri)

        list_of_tracks.append(
            {
                'name': name,
                'artist_name': artist_name,
                'artist_id': artist_id,
                'played_at': played_at,
                'context_type': context_type,
                'context_uri': context_uri
            }
        )
    return list_of_tracks