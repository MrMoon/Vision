# AWS Lambda function to call the DeepAI Super Resolution API

import urllib.request
import json
import os

def lambda_handler(event, context):
    
    API_URL = 'https://api.deepai.org/api/torch-srgan'
    API_KEY = os.environ['API_KEY']
    IMAGE_URL = json.loads(event['body'])['image']
    
    data = urllib.parse.urlencode({'image': IMAGE_URL})
    data = data.encode('ascii')
    res = urllib.request.urlopen(urllib.request.Request(
        url=API_URL,
        data=data,
        headers={'api-key': API_KEY},
        method='POST'),
    timeout=5)
    
    return {
      "isBase64Encoded": False,
      "statusCode": res.status,
      "body": json.loads(res.read())['output_url']
    }
