import boto3
import os

from functions.dynamodb import db_query
from functions.utils import parse_db

def handler(event, context):
    results_db_query = db_query()
    results_parse_db = parse_db(results_db_query)
    return(results_parse_db)