import os

from functions.dynamodb import db_export, db_describe_export
from functions.ssm import ssm_put

def handler(event, context):
    table = os.environ['TableArn']
    print(f'Exporting {table}')

    result_export = db_export()
    print(result_export['ExportArn'])