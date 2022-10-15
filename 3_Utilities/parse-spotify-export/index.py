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

def parse_csv():
    file = f'{current_utc_hour()}.csv'
    df = pd.read_csv(file)

    df[['full_date', 'full_time']] = df.ts.str.split('T', expand=True)
    df[['year', 'month', 'day']] = df.full_date.str.split('-', expand=True)
    df [['hour', 'minute', 'seconds']] =  df.full_time.str.split(':', expand=True)

    # Columns to skip
    df = df.drop(['conn_country', 'ms_played', 'ip_addr_decrypted', 'user_agent_decrypted', 'reason_start', 'reason_end', 'skipped','offline', 'offline_timestamp', 'incognito_mode'], axis=1)
    df.to_csv(f'parsed_{file}')