import os
import json

from functions.dynamodb import query
from functions.utils import parse_items, parse_query_string_parameters, get_current_year_month, create_pandas_data_frame

def handler(event, context):
    year_month = get_current_year_month()
    # If no query parameters
    try:
        year_month, query_Type = parse_query_string_parameters(event)
    except:
        pass

    print(year_month)
    items = query(year_month)

    if len(items) != 0:
        parsed_items = parse_items(items)

        return {
            "year_month": year_month,
            "top_devices": create_pandas_data_frame(parsed_items, "device"),
            "top_songs": create_pandas_data_frame(parsed_items, "song"),
            "top_artists": create_pandas_data_frame(parsed_items, "artist"),
            "top_albums": create_pandas_data_frame(parsed_items, "album"),
            "top_playlists": create_pandas_data_frame(parsed_items, "playlist_name"),
            # "items": parsed_items
        }
    else:
        return {"result": "No results for that month."}

if __name__ == "__main__":
    year_month = "2023-10"
    event = {'queryStringParameters': {'year_month': year_month}}
    items = handler(event, None)
    print(items)