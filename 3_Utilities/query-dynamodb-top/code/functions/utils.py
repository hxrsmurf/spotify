def parse_items(items):
    list_items = []

    for item in items:
        parsed = {
            'artist': item['artist']['S'],
            'songID': item['songID']['S'],
            'deviceType': item['deviceType']['S'],
            'device': item['device']['S'],
            'albumID': item['albumID']['S'],
            'album': item['album']['S'],
            'playlist_name': item['playlist_name']['S'],
            'song': item['song']['S'],
            'contextType': item['contextType']['S'],
            'year_month': item['year_month']['S'],
            'id': item['id']['S'],
        }
        try:
            parsed['possibleDuplicate'] = item['possibleDuplicate']['BOOL']
        except:
            pass

        list_items.append(parsed)

    return list_items