from datetime import datetime

def calculate_duration_between_last_entry(previous, current):
    duration = current - previous
    minutes = datetime.utcfromtimestamp(duration).strftime('%M')
    seconds = datetime.utcfromtimestamp(duration).strftime('%S')
    seconds_milliseconds = convert_to_milliseconds(seconds, 'seconds')
    minutes_milliseconds = convert_to_milliseconds(minutes, 'minutes')
    return int(seconds_milliseconds + minutes_milliseconds)

def convert_to_milliseconds(string, type):
    if type == 'seconds':
        return int(string) * 1000
    elif type == 'minutes':
        return int(string) * 60000