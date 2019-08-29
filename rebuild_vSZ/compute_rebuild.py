import requests
import json
import os

apiAccess = {
    'service': 'Compute',
    'endpoint': 'http://10.206.5.12:8774/v2.1',
    'api': '/servers',
    'instanceName': os.environ['instanceName']
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
        if server['name'] == apiAccess['instanceName']:
            print(server['name'], server['id'])
            apiAccess['instanceId'] = server['id']


def funcname(parameter_list):
    pass


# start
# get instance id
get(apiAccess, headers)
# rebuild
apiAccess['api'] = '/servers/' + apiAccess['instanceId'] + '/action'
apiData = {
    
}