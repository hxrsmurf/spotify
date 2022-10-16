from datetime import datetime

def calculate_duration_since_last_entry(previous, current):
    duration = float(current) - float(previous)
    minutes = datetime.utcfromtimestamp(duration).strftime('%M')
    seconds = datetime.utcfromtimestamp(duration).strftime('%S')
    seconds_milliseconds = convert_to_milliseconds(seconds, 'seconds')
    minutes_milliseconds = convert_to_milliseconds(minutes, 'minutes')
    return float(seconds_milliseconds + minutes_milliseconds)

def convert_to_milliseconds(string, type):
    if type == 'seconds':
        return float(string) * 1000
    elif type == 'minutes':
        return float(string) * 60000

def current_year_month():
    return datetime.utcnow().strftime('%Y-%m')

def current_year_month_day():
    return datetime.utcnow().strftime('%Y-%m-%d')

def current_timestamp_epoch():
    dt = datetime.utcnow()
    timestamp = dt.strftime('%Y-%m-%d, %H:%M:%S:%f')
    epoch_time = dt.timestamp()

    return timestamp, epoch_time