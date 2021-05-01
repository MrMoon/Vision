import urllib.request
import json
import os

def lambda_handler(event, context):
    API_URL = 'https://api.deepai.org/api/torch-srgan'
    API_KEY = os.environ['API_KEY']
    IMAGE_URL = event['image']
    
    data = urllib.parse.urlencode({'image': IMAGE_URL})
    data = data.encode('ascii')
    res = urllib.request.urlopen(urllib.request.Request(
            url=API_URL,
            data=data,
            headers={'api-key': API_KEY},
            method='POST'),
        timeout=5)
    return json.loads(res.read())
 

