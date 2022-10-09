import os

from functions.dynamodb import db_export

def handler(event, context):
    table = os.environ['TableArn']
    print(f'Exporting {table}')

    result_export = db_export()
    ssm.put(result_export['ExportArn'])