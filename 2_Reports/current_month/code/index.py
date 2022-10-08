import pandas as pd

from functions.dynamodb import db_query
from functions.utils import parse_db
from functions.s3 import s3_upload

def handler(event, context):
    results_db_query = db_query()
    results_parse_db = parse_db(results_db_query)
    df = pd.DataFrame(results_parse_db)
    temp_file = '/tmp/file.csv'
    df.to_csv(temp_file, index=False, header=True, sep=';')
    s3_upload(temp_file)
    # Example change