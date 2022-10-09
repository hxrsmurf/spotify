import os

from functions.dynamodb import db_export, db_describe_export
from functions.ssm import ssm_put
from functions.sns import send_notfication

def handler(event, context):
    table = os.environ['TableArn']
    print(f'Exporting {table}')

    result_export = db_export()
    
    ssm_put(result_export)

    message = f'Started DB Export: {result_export['ExportArn']}'    
    send_notfication(message)

    print(message)