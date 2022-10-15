import json
import os

import pandas as pd

from datetime import datetime


def current_utc_timestamp():
    return datetime.utcnow().strftime('%Y-%m-%H%M%S')

def current_utc_hour():
    return datetime.utcnow().strftime('%Y-%m-%H')

def parse(file):
    file_name = current_utc_hour()
    df = pd.read_json('endsong_0.json')
    df.to_csv(f'{file_name}.csv', mode='a', index=False)

def parse_json():
    files = os.listdir()
    for file in files:
        if '.json' in file:
            print('Parsing file:', file)
            parse(file)