import requests
import json

def apiFormat(api, endpoint):
    apiUrl = endpoint + api
    return apiUrl
authApi = apiFormat('/auth/tokens', 'http://10.206.5.12:5000/v3')

def authFormat(uName, uPassword, uProject):
    authData = {
        "auth": {
            "identity": {
                "methods": ["password"],
                "password": {
                    "user": {
                        "domain": {
                            "name": "Default"
                        },
                        "name": uName,
                        "password": uPassword
                    }
                }
            },
            "scope": {
                "project": {
                    "domain": {
                        "name": "Default"
                    },
                    "name":  uProject
                }
            }
        }
    }
    return authData
authInfo = authFormat('jenkins', 'jenkins', 'Datacenter')

try:
    res = requests.post(authApi, json=authInfo)
except requests.exceptions.RequestException as err:
    print(err)
    exit(1)

#print(res.status_code)
#print(res.headers['X-Subject-Token'])
token = {
    'X-Auth-Token': res.headers['X-Subject-Token']
}

with open('token.json', 'wt') as writeToken:
    writeToken.write(json.dumps(token))