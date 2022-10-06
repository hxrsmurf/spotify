import boto3
import os

from functions.dynamodb import db_query

def handler(event, context):
    results_db_query = db_query()
    return(results_db_query)