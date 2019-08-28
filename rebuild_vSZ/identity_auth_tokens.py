import json
import requests

apiAccess = {
    'service': 'Identity',
    'endpoint': 'http://10.206.5.12:5000/',
    'api': '/v3/auth/tokens'
}

apiData = {
    "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "name": "jenkins",
                    "domain": {
                        "name": "Default"
                    },
                    "password": "jenkins"
                }
            }
        },
        "scope": {
            "project": {
                "domain": {
                    "name": "Default"
                },
                "name": "Datacenter"
            }
        }
    }
}


def post(apiAccess, apiData):
    apiUrl = apiAccess['endpoint'] + apiAccess['api']
    try:
        resp = requests.post(apiUrl, json=apiData)
    except requests.exceptions.RequestException as err:
        print(err)
        exit(1)
    print('Status:\n', resp.status_code)
    print('Headers:\n', resp.headers)
    print('Content:\n', resp.content)
    resp.close()
    return resp


# start
resp = post(apiAccess, apiData)
print('X-Subject-Token:', resp.headers['X-Subject-Token'])
fileData = {
    'X-Auth-Token': resp.headers['X-Subject-Token']
}
with open('token.json', 'wt') as fh:
    json.dump(fileData, fh)
    fh.close()
