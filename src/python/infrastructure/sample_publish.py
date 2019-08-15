import boto3
import os

def publish(message):
    sqs_endpoint_url = 'https://%s' % os.environ['SQS_ENDPOINT']
    client = boto3.client('sqs', endpoint_url = sqs_endpoint_url)
    queue_name = os.environ['QUEUE_NAME']
    res = client.get_queue_url(QueueName = queue_name)
    url = res['QueueUrl']
    client.send_message(QueueUrl = url, MessageBody = message)