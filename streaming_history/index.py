import json
import os

files = os.listdir()

for file in files:
    if '.json' in file:
        with open(file, 'r', encoding='utf8') as json_file:
            while True:
                try:
                    loaded = json.load(json_file)
                    for load in loaded:
                        end_time = load['endTime']
                        year_month = end_time.split(' ')[0]
                        hour_minute = end_time.split(' ')[1]
                        artist_name = load['artistName']
                        track_name = load['trackName']
                        ms_played = load['msPlayed']

                        result = f'{end_time}; {year_month}; {hour_minute}; {artist_name}; {track_name}; {ms_played}; {file}'
                        print(result)
                        with open('output.csv', 'a') as output:
                            output.write(f'{result}\n')

                except Exception as e:
                    print(e, file, load)
                    break