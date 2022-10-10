import boto3

client = boto3.client('ssm')

def get_parameter(parameter):
    return client.get_parameter(
        Name=parameter
    )['Parameter']['Value']
