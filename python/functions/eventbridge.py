import boto3

def update(value):
    client = boto3.client('events')
    schedule_expression = f'rate({value} minutes)'
    response = client.put_rule(
        Name='EventBridge',
        ScheduleExpression=schedule_expression
    )