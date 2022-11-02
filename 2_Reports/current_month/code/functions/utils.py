from datetime import datetime
from dateutil.relativedelta import relativedelta

def current_year_month():
    return datetime.utcnow().strftime('%Y-%m')

def current_day_time():
    return datetime.utcnow().strftime('%Y-%m-%d-%H%M%SS')

def previous_month():
    #https://stackoverflow.com/questions/9724906/python-date-of-the-previous-month
    now = datetime.utcnow()
    previous = now - relativedelta(months=1)
    print(previous)
    return previous.strftime('%Y-%m')

def parse_db(results_db_query):
    list_of_results = []
    for result in results_db_query:
        current_result = {}
        for key, value in enumerate(result.items()):
            column = value[0]
            field_value = list(value[1].values())[0]

            current_result[column] = field_value

        list_of_results.append(current_result)

    return list_of_results