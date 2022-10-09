from datetime import datetime

def current_year_month():
    return datetime.utcnow().strftime('%Y-%m')

def current_day_time():
    return datetime.utcnow().strftime('%Y-%m-%d-%H%M%SS')