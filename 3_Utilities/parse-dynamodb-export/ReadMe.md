# Procedure

1. Go to DynamoDB Table
2. Export to S3
3. Sync the S3 bucket to your workstation `aws s3 sync s3://example/ .`
4. Extract the `tar.gz` files
5. Copy the `.json` files
6. Run `python index.py`