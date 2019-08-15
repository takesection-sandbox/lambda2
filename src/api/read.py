import json
import infrastructure.sample_read

def lambda_handler(event, context):
    req = json.loads(event['body'])
    body = infrastructure.sample_read.read(req['key'])
    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }