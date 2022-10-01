import json
import os

files = os.listdir()

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
                        print(result)
                        try:
                            album = result['Item']['album']['S']
                            artist = result['Item']['artist']['S']
                            song_id = result['Item']['songID']['S']
                            song = result['Item']['song']['S']
                            device_id = result['Item']['deviceID']['S']
                            device_type = result['Item']['deviceType']['S']
                            device = result['Item']['device']['S']
                            id = result['Item']['id']['S']
                            album_id = result['Item']['albumID']['S']
                            total_result = f'{album}; {artist}; {song_id}; {song}; {device_id}; {device_type}; {device}; {id}; {album_id}'
                            print(total_result)
                            with open('output4.txt', 'a') as output:
                                output.write(f'{total_result}\n')

                        except Exception as e:
                            print
                except Exception as e:
                    print(e)
                    break