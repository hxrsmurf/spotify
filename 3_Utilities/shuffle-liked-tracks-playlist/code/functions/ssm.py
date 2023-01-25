import os
import boto3

client = boto3.client('ssm')

def get_parameter(parameter):
    return client.get_parameter(
        Name=parameter
    )['Parameter']['Value']

def put_parameter(parameter, value):
    client.put_parameter(
        Name = parameter,
        Value = value,
        Type = 'Standard',
        Overwrite = True
    )