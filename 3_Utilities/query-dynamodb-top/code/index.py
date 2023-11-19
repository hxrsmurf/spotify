import os
import json

from functions.dynamodb import query, put, get, get_artist_id, get_album_id
from functions.utils import parse_items, parse_query_string_parameters, get_current_year_month, create_pandas_data_frame

def handler(event, context):
    year_month = get_current_year_month()

    # Handle artist lookup. Don't feel like doing a separate API...
    try:
        artist = event['queryStringParameters']['artist']
        artist_image = get_artist_id(artist)
        print(artist, artist_image)
        return {
            'artist_image': artist_image
        }
    except:
        pass

    # Handle album lookup. Don't feel like doing a separate API...
    try:
        album_id = event['queryStringParameters']['album_id']
        album_image = get_album_id(album_id)
        print(album_id, album_image)
        return {
            'album_image': album_image
        }
    except:
        pass

    # If no query parameters
    try:
        year_month, query_type, limit = parse_query_string_parameters(event)
    except:
        pass

    print(year_month, query_type, limit)
    exists_top_year_month = get(year_month)
    if exists_top_year_month and not year_month == get_current_year_month():
        return exists_top_year_month

    items = query(year_month)

    if len(items) != 0:
        parsed_items = parse_items(items)

        top_devices = create_pandas_data_frame(parsed_items, "device", 10)
        top_songs = create_pandas_data_frame(parsed_items, "song", 20)
        top_artists = create_pandas_data_frame(parsed_items, "artist", 10)
        top_albums = create_pandas_data_frame(parsed_items, "album", 10)
        top_playlists = create_pandas_data_frame(parsed_items, "playlist_name", 10)

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