import os

from functions.dynamodb import db_export

def handler(event, context):
    table = os.environ['Table']
    print(f'Exporting {table}')

    db_export()

    # Run workflow