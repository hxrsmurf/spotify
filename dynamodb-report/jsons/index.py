import json
import os

from datetime import datetime

current = datetime.utcnow().strftime('%Y-%M-%H%M%S')

files = os.listdir()

output_file = f'{current}.csv'

with open(output_file, 'a') as output:
    output.write('{album}; {artist}; {song_id}; {song}; {device_id}; {device_type}; {device}; {album_id}; {id}; {contextUri}; {contextType}; {trackDurationMS}; {year_month}; {epoch_time}\n')

for file in files:
    if '.json' in file:
        with open(file, 'r', encoding='utf8') as json_file:
            while True:
                try:
                    line = json_file.readline()
                    if not line:
                        break
                    else:
                        result = json.loads(line)
                        try:

                            if not 'contextUri' in result:
                                contextUri = None
                            else:
                                contextUri = result['Item']['contextUri']['S']

                            if not 'contextType' in result:
                                contextType = None
                            else:
                                contextType = result['Item']['contextType']['S']

                            if not 'trackDurationMS' in result:
                                trackDurationMS = None
                            else:
                                trackDurationMS = result['Item']['trackDurationMS']['N']

                            if not 'year_month' in result:
                                year_month = None
                            else:
                                year_month = result['Item']['year_month']['S']

                            if not 'album' in result:
                                album = None
                            else:
                                album = result['Item']['album']['S']

                            if not 'album' in result:
                                device_id = None
                            else:
                                device_id = result['Item']['deviceID']['S']

                            if not 'device' in result:
                                device = None
                            else:
                                device = result['Item']['device']['S']

                            if not 'device_type' in result:
                                device_type = None
                            else:
                                device_type = result['Item']['deviceType']['S']

                            if not 'album_id' in result:
                                album_id = None
                            else:
                                album_id = result['Item']['albumID']['S']

                            if not 'epoch_time' in result:
                                epoch_time = None
                            else:
                                epoch_time = result['Item']['epoch_time']['N']

                            artist = result['Item']['artist']['S']
                            song_id = result['Item']['songID']['S']
                            song = result['Item']['song']['S']
                            id = result['Item']['id']['S']

                            total_result = f'{album}; {artist}; {song_id}; {song}; {device_id}; {device_type}; {device}; {album_id}; {id}; {contextUri}; {contextType}; {trackDurationMS}; {year_month}; {epoch_time}'

                            with open(output_file, 'a') as output:
                                output.write(f'{total_result}\n')

                        except Exception as e:
                            print(result)
                            print(e)
                            break

                except Exception as e:
                    print(e)
                    break