from datetime import datetime
import pandas as pd
import json

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

    try:
        limit = parameters['limit']
    except:
        limit = None
        pass
    
    return year_month, query_type, limit

def create_pandas_data_frame(items, query_type='song', limit=10, year=None):
    df = pd.DataFrame(items)

    df['count'] = df.groupby(query_type)[query_type].transform('count')
    df.sort_values(by='count', ascending=False, inplace=True)

    if query_type == 'songID':
        new_df = df[['artist', 'song', 'album', 'count']].drop_duplicates()

    if query_type == 'artist':
        new_df = df[['artist','count']].drop_duplicates()

    if query_type == 'album':
        new_df = df[['album', 'albumID', 'count']].drop_duplicates()
        new_df = new_df.groupby(['album']).first().reset_index()
        new_df = new_df.sort_values(by='count', ascending=False)

    if query_type == 'playlist_name':
        new_df = df[['playlist_name', 'count']].drop_duplicates()

    if query_type == 'device':
        new_df = df[['device', 'count']].drop_duplicates()
    
    print(query_type)
    with pd.option_context('display.min_rows', 30):
        print(new_df)
    return json.loads(new_df.head(limit).to_json(orient='records'))