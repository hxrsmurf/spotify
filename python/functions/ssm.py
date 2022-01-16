import boto3
# This updates the SSM Parameter for Refresh Token. Spotify says we might get a new one.

def put(parameter, value):
    ssm_client = boto3.client('ssm')    
    
    ssm_client.put_parameter(
        Name=parameter,
        Value=value,
        Tier='Standard',
        Overwrite=True
    )
    
    print('Successfully saved to SSM')
    return('Successfully saved to SSM')
    
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html
def get(parameter):
    ssm_client = boto3.client('ssm')
    result = ssm_client.get_parameter(
        Name=parameter
    )['Parameter']['Value']
    
    return(result)