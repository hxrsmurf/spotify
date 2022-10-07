from datetime import datetime

def current_year_month():
    return datetime.utcnow().strftime('%Y-%m')

def parse_db(results_db_query):
    list_of_results = []
    for result in results_db_query:
        list_of_results.append(
            {
                "album": result['album']['S'],
                "artist": result['artist']['S'],
                "song": result['song']['S'],
                "songID": result['songID']['S'],
                "deviceID": result['deviceID']['S'],
                "epochTime": result['epochTime']['N'],
                "deviceType":result['deviceType']['S'],
                "device": result['device']['S'],
                "year_month": result['year_month']['S'],
                "id": result['id']['S'],
                "albumID": result['albumID']['S']
            }
        )
    return list_of_results