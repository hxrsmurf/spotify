import os
import pandas as pd
from datetime import datetime

def current_utc_timestamp():
    return datetime.utcnow().strftime('%Y-%m-%H%M%S')

def current_utc_hour():
    return datetime.utcnow().strftime('%Y-%m-%H')

def current_year():
    return datetime.utcnow().strftime('%Y')

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

def parse_year(input_year):
    file = f'parsed_{current_utc_hour()}.csv'

    df = pd.read_csv(file)

    df = df[df['year'] == str(input_year)]

    #print(df)

    group = df.groupby(['year', 'master_metadata_track_name', 'master_metadata_album_artist_name'])['year'].count().nlargest(n=20, keep='all')

    #print(group)

    with pd.ExcelWriter(f'all_data.xlsx', mode='a') as writer:
        group.to_excel(writer, sheet_name=str(input_year))

def create_xlsx():
    start = 2011
    end = int(current_year()) + 1
    years = range(start,end)

    for year in years:
        print(f'Checking year: {year}')
        try:
            parse_year(year)

        except Exception as e:
            print(e)
            print(f'This year has no data: {year}')
            pass