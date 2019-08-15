import boto3
import os
import json

def read(key):
    client = boto3.client('s3')
    bucket = os.environ['BUCKET_NAME']
    res = client.get_object(Bucket = bucket, Key = key)
    return json.loads(res['Body'].read())
