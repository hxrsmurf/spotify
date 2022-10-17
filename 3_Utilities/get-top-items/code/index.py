from functions.player import get_top_items
from functions.authorization import get_access_token
from functions.utils import handle_top_tracks, handle_top_artists

def handler(event, context):
    access_token = get_access_token()
    available_types = ['artists', 'tracks']

    time_ranges = {
        'short_term' : '4 weeks',
        'medium_term' : '6 months',
        'long_term' : 'several years of data'
    }

    for type in available_types:
        for key, value in time_ranges.items():
            top_items = get_top_items(type=type, access_token=access_token, time_range=key)
            if type == 'tracks':
                result = handle_top_tracks(top_items)

            if type == 'artists':
                result = handle_top_artists(top_items)

            print(f'Time Range: {key} - {value}')
            print(result)