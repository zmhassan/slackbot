import json
from urllib import parse
import boto3

def handle(event, context):
    try:
        headers = event['headers']
        raw_data = event['body']
        if 'challenge' in raw_data:
            payload = json.loads(raw_data)
            return {
                'statusCode': 200,
                'body': json.dumps(payload['challenge'])
            }
        else:
            print('Event')
            print(event)
            req = dict(parse.parse_qsl(raw_data))
            if req['text'] == 'help':
                return {
                    'statusCode': 200,
                    'body': 'You summoned for help....'
                }

    except:
        print("exception thrown")
    return {
        'statusCode': 200,
        'body': 'Error: invalid input '
    }
