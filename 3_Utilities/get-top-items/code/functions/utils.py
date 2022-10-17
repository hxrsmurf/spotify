def handle_top_tracks(top_items):
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

def handle_top_artists(top_items):
    list_of_artists = []
    for item in top_items['items']:
        name = item['name']
        uri = item['uri']

        list_of_artists.append(
            {
                'name' : name,
                'uri': uri
            }
        )

    return list_of_artists