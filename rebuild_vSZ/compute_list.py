import requests
import json
import os

apiAccess = {
    'service': 'Compute',
    'endpoint': 'http://10.206.5.12:8774/v2.1',
    'api': '/servers',
}

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
    resp.close()
    print('Status:\n', resp.status_code)
    print('Headers:\n', resp.headers)
    print('Content:\n', resp.content)
    # start
    servers = resp.json()['servers']
    for server in servers:
        print(server['id'], server['name'])


# start
get(apiAccess, headers)
