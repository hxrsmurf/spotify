from datetime import datetime
import pandas as pd

def get_current_year_month():
    current_date = datetime.now()
    current_year = current_date.year
    current_month = current_date.month
    formatted_date = f"{current_year}-{current_month:02d}"
    return formatted_date

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

def parse_query_string_parameters(event):
    year_month, query_type = get_current_year_month(), 'songs'
    parameters = event['queryStringParameters']

    try:
        year_month = parameters['year_month']
    except:
        pass

    try:
        query_type = parameters['query_type']
    except:
        pass
    
    return year_month, query_type

def create_pandas_data_frame(items):
    df = pd.DataFrame(items)
    song_counts = df['song'].value_counts()
    print(song_counts)
    return df