import os

from functions.dynamodb import query
from functions.utils import parse_items

def handler(event, context):
    items = query('2023-10')
    parsed_items = parse_items(items)
    print(parsed_items)

if __name__ == "__main__":
    handler(None, None)