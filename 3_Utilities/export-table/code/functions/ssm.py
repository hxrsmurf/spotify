import boto3
import os 

def ssm_put(value):
    ssm_client = boto3.client('ssm')
    parameter = os.environ['ExportArn']

    ssm_client.put_parameter(
        Name=parameter,
        Value=value,
        Tier='Standard',
        Overwrite=True
    )

    message = f'Successfully {value} saved to SSM'
    print(message)
    return(message)

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html
def ssm_get():
    ssm_client = boto3.client('ssm')
    parameter = os.environ['ExportArn']
    result = ssm_client.get_parameter(
        Name=parameter
    )['Parameter']['Value']

    return(result)