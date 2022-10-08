import os

from functions.dynamodb import db_delete

def handler(event, context):
    table = os.environ['Table']
    print(f'Accessing {table}')

    with open('ids.txt', 'r') as ids_to_delete:
        for id in ids_to_delete:
            print(f'Deleting {id}...')
            db_delete(id.strip())