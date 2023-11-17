import os

from functions.dynamodb import query
from functions.utils import parse_items, parse_query_string_parameters, get_current_year_month, create_pandas_data_frame

def handler(event, context):
    year_month, query_Type = parse_query_string_parameters(event)
    items = query(year_month)

    if len(items) != 0:
        parsed_items = parse_items(items)
        df = create_pandas_data_frame(parsed_items)
        print(df)

        return parsed_items 
    else:
        return {"result": "No results for that month."}

if __name__ == "__main__":
    event = {'queryStringParameters': {'year_month': get_current_year_month()}}
    items = handler(event, None)