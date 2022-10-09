import os

from functions.dynamodb import db_export, db_describe_export
from functions.ssm import ssm_put
from functions.sns import send_notfication

def handler(event, context):
    table = os.environ['TableArn']
    print(f'Exporting {table}')

    result_export = db_export()
    message = f'Started DB Export: {result_export['ExportArn']}'
    print(message)
    send_notfication(message)