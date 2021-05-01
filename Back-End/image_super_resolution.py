import urllib.request
import json

API_URL = 'https://api.deepai.org/api/torch-srgan'
# API_KEY 
IMAGE_URL = 'https://www.drupal.org/files/issues/sample-im-10.png'

data = urllib.parse.urlencode({'image': IMAGE_URL})
data = data.encode('ascii')

res = urllib.request.urlopen(urllib.request.Request(
        url=API_URL,
        data=data,
        headers={'api-key': API_KEY},
        method='POST'),
    timeout=5)

print(res.status)
print(res.reason)
print(json.loads(res.read()))
 
