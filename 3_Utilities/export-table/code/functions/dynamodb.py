import boto3
import os

from .utils import current_day_time

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html

def db_export():
    table_arn = os.environ['TableArn']
    bucket = os.environ['Bucket']
    client = boto3.client('dynamodb')
    output_file = f'{current_day_time()}.csv'

    response = client.export_table_to_point_in_time(
        TableArn  = table_arn,
        S3Bucket = bucket,
        S3Prefix = f'output/{output_file}'
    )

    return response['ExportDescription']['ExportArn']

def db_describe_export(ExportArn):
    client = boto3.client('dynamodb')
    response = client.describe_export(
        ExportArn = ExportArn
    )

    return (response['ExportDescription']['ExportStatus'])