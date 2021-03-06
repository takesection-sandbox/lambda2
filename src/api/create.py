import json
import infrastructure.sample_command

def lambda_handler(event, context):
    req = json.loads(event['body'])
    infrastructure.sample_command.create(req['id'], req['name'])
    body = {}
    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }