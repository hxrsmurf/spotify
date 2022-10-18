def handle_playlist(playlists):
    list_of_playlists = []

    for playlist in playlists['items']:
        description = playlist['description']
        id = playlist['id']
        name = playlist['name']
        uri = playlist['uri']

        list_of_playlists.append({
            'description' : description,
            'id' : id,
            'name' : name,
            'uri' : uri
        })

    return list_of_playlists