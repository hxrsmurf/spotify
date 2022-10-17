from functions.player import get_top_items
from functions.authorization import get_access_token
from functions.utils import handle_top_items

def handler(event, context):
    access_token = get_access_token()
    available_types = ['artists', 'tracks']

    time_ranges = {
        'short_term' : '4 weeks',
        'medium_term' : '6 months',
        'long_term' : 'several years of data'
    }

    for key, value in time_ranges.items():
        top_items = get_top_items(type='tracks', access_token=access_token, time_range=key)
        result_handle_items = handle_top_items(top_items)
        print(f'Time Range: {key} - {value}')
        print(result_handle_items)