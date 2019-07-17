import json
import infrastructure.hello

def lambda_handler(event, context):
    req = json.loads(event['body'])
    body = infrastructure.hello.message(req['message'])
    return {
        "statusCode": 200,
        "body": body
    }