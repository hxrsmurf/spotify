import os
import json

from functions.dynamodb import query, put, get
from functions.utils import parse_items, parse_query_string_parameters, get_current_year_month, create_pandas_data_frame

def handler(event, context):
    year_month = get_current_year_month()
    # If no query parameters
    try:
        year_month, query_type = parse_query_string_parameters(event)
    except:
        pass

    print(year_month)
    exists_top_year_month = get(year_month)
    if exists_top_year_month and not year_month == get_current_year_month():
        return exists_top_year_month

    items = query(year_month)

    if len(items) != 0:
        parsed_items = parse_items(items)

        top_devices = create_pandas_data_frame(parsed_items, "device")
        top_songs = create_pandas_data_frame(parsed_items, "song")
        top_artists = create_pandas_data_frame(parsed_items, "artist")
        top_albums = create_pandas_data_frame(parsed_items, "album")
        top_playlists = create_pandas_data_frame(parsed_items, "playlist_name")

        top_table_data = {
            "year_month": year_month,
            "top_devices": top_devices,
            "top_songs": top_songs,
            "top_artists": top_artists,
            "top_albums": top_albums,
            "top_playlists": top_playlists,
            "items": parsed_items
        }

        put(year_month, top_table_data)
        return top_table_data
    else:
        return {"result": "No results for that month."}

if __name__ == "__main__":
    for i in range(1, 13):
        year_month = '2023-{:02d}'.format(i)
        event = {'queryStringParameters': {'year_month': year_month}}
        items = handler(event, None)