import boto3
import os

from functions.dynamodb import db_query
from functions.utils import parse_db
import pandas as pd

def handler(event, context):
    results_db_query = db_query()
    results_parse_db = parse_db(results_db_query)
    df = pd.DataFrame(results_parse_db)
    df.to_csv('/tmp/file.csv', index=False, header=True, sep=';')
    return('kevin')