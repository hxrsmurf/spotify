from datetime import datetime

def current_year_month():
    return datetime.utcnow().strftime('%Y-%m')