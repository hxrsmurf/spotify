from datetime import datetime

def convert_to_milliseconds(string, type):
    if type == 'seconds':
        return int(string) * 1000
    elif type == 'minutes':
        return int(string) * 60000