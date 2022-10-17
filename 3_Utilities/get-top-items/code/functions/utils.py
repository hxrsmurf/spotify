def handle_top_items(top_items):
    list_of_tracks = []
    for track in top_items['items']:
        name = track['name']
        artist = track['artists'][0]['name']
        uri = track['uri']

        list_of_tracks.append(
            {
                'name': name,
                'artist' : artist,
                'uri' : uri
            }
        )
    return list_of_tracks