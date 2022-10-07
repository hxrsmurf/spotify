from datetime import datetime

def current_year_month():
    return datetime.utcnow().strftime('%Y-%m')

def current_day():
    return datetime.utcnow().strftime('%Y-%m-%d-%H%M%SS')

def parse_db(results_db_query):
    list_of_results = []
    for result in results_db_query:
        id = result['id']['S']
        album =  None
        artist =  None
        song =  None
        songID =  None
        deviceID =  None
        epochTime =  None
        deviceType =  None
        device =  None
        year_month =  None
        id =  None
        albumID =  None
        contextType =  None
        contextUri =  None
        trackDurationMS =  None
        possibleDuplicate =  None

        # Some entries in the DB may not have these new values
        try:
            context_type = result['contextType']['S']
            context_uri = result['contextUri']['S']
            track_duration_ms = result['trackDurationMS']['N']
            possible_duplicate = result['possibleDuplicate']['BOOL']
            epochTime = result['epochTime']['N']
            album = result['album']['S']
            artist = result['artist']['S']
            song =  result['song']['S']
            songID = result['songID']['S']
            deviceID = result['deviceID']['S']
            deviceType = result['deviceType']['S']
            device = result['device']['S']
            year_month = result['year_month']['S']
            id = result['id']['S']
            albumID = result['albumID']['S']
        except Exception as e:
            print(f'{id} empty due to error: {e}')

        list_of_results.append(
            {
                "album": album,
                "artist": artist,
                "song": song,
                "songID": songID,
                "deviceID": deviceID,
                "epochTime": epochTime,
                "deviceType": deviceType,
                "device": device,
                "year_month": year_month,
                "id": id,
                "albumID": albumID,
                "contextType" : context_type,
                "contextUri" : context_uri,
                "trackDurationMS" : track_duration_ms,
                "possibleDuplicate" : possible_duplicate
            }
        )
    return list_of_results