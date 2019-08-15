import json
import infrastructure.sample_publish

def lambda_handler(event, context):
    message = event['body']
    infrastructure.sample_publish.publish(message)
    body = {}
    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }