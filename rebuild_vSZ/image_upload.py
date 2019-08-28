import requests
import json
import sys

if len(sys.argv) != 2:
    print('Arg len not match 2')
    exit(1)

apiAccess = {
    'service': 'Image',
    'endpoint': 'http://10.206.5.12:9292',
    'api': '/v2/images'
}

apiData = {
    'container_format': 'bare',
    'disk_format': 'qcow2',
    'name': sys.argv[1]
}

# read token from file
with open('token.json', 'rt') as fh:
    headers = json.load(fh)
    fh.close()


def post(apiAccess, headers, apiData):
    apiUrl = apiAccess['endpoint'] + apiAccess['api']
    try:
        resp = requests.post(apiUrl, headers=headers, json=apiData)
    except requests.exceptions.RequestException as err:
        print(err)
        exit(1)
    print('Status:\n', resp.status_code)
    print('Headers:\n', resp.headers)
    print('Content:\n', resp.content)
    resp.close()
    return resp


# start
# create
resp = post(apiAccess, headers, apiData)
# upload
apiAccess['api'] = resp.json()['file']
print(apiAccess['api'])
headers['Content-Type'] = 'application/octet-stream'
print(headers)
def postFile(apiAccess, headers, apiData):
    apiUrl = apiAccess['endpoint'] + apiAccess['api']
    try:
        resp = requests.put(apiUrl, headers=headers, data=open(apiData['name'], 'rb'))
    except requests.exceptions.RequestException as err:
        print(err)
        exit(1)
    print('Status:\n', resp.status_code)
    print('Headers:\n', resp.headers)
    print('Content:\n', resp.content)
    resp.close()
    return resp

resp = postFile(apiAccess, headers, apiData)