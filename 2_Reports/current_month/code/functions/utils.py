from datetime import datetime

def current_year_month():
    return datetime.utcnow().strftime('%Y-%m')

def current_day_time():
    return datetime.utcnow().strftime('%Y-%m-%d-%H%M%SS')

def parse_db(results_db_query):
    list_of_results = []
    for result in results_db_query:
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

        try:
            id = result['id']['S']
        except:
            pass

        # Some entries in the DB may not have these new values
        try:
            contextType = result['contextType']['S']
            contextUri = result['contextUri']['S']
            trackDurationMS = result['trackDurationMS']['N']
            possibleDuplicate = result['possibleDuplicate']['BOOL']
            epochTime = result['epochTime']['N']
            album = result['album']['S']
            artist = result['artist']['S']
            song =  result['song']['S']
            songID = result['songID']['S']
            deviceID = result['deviceID']['S']
            deviceType = result['deviceType']['S']
            device = result['device']['S']
            year_month = result['year_month']['S']
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
                "contextType" : contextType,
                "contextUri" : contextUri,
                "trackDurationMS" : trackDurationMS,
                "possibleDuplicate" : possibleDuplicate
            }
        )
    return list_of_results