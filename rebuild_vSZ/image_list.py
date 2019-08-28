import requests
import json
import os

apiAccess = {
    'service': 'Image',
    'endpoint': 'http://10.206.5.12:9292',
    'api': '/v2/images',
    'fileName': 'vscg-' + os.environ['szVer'] + '.qcow2'
}

apiData = dict()

# read token from file
with open('token.json', 'rt') as fh:
    headers = json.load(fh)
    fh.close()


def get(apiAccess, headers):
    apiUrl = apiAccess['endpoint'] + apiAccess['api']
    try:
        resp = requests.get(url=apiUrl, headers=headers)
    except requests.exceptions.RequestException as err:
        print(err)
        exit(1)
    print('Status:\n', resp.status_code)
    print('Headers:\n', resp.headers)
    print('Content:\n', resp.content)
    resp.close()
    return resp


# start
resp = get(apiAccess, headers)
imageList = resp.json()['images']
print(json.dumps(imageList, indent=4))

nameList = list()
for image in imageList:
    nameList.append(image['name'])
if apiAccess['fileName'] in nameList:
    print('File exist. Skip')
else:
    print('Upload start')
