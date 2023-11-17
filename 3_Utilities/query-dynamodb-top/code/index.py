import os

from functions.dynamodb import query
from functions.utils import parse_items, parse_query_string_parameters

def handler(event, context):
    year_month, query_Type = parse_query_string_parameters(event)
    items = query(year_month)

    if len(items) != 0:
        parsed_items = parse_items(items)
        return parsed_items 
    else:
        return {"result": "No results for that month."}

if __name__ == "__main__":
    items = handler(None, None)