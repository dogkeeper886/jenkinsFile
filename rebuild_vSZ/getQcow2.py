import os
import requests

apiAccess = {
    'endpoint': 'http://tdc-repository.arrisi.com:8081/nexus/content/repositories/releases/ruckus/official/mega/sz',
    'api': '/5.2.0.0/ML/' + os.environ['szVer'] + '/vscg/vscg-' + os.environ['szVer'] + '.qcow2',
    'fileName': 'vscg-' + os.environ['szVer'] + '.qcow2'
}


def getQcow2(apiAccess):
    apiUrl = apiAccess['endpoint'] + apiAccess['api']
    try:
        resp = requests.get(url=apiUrl, stream=True)
    except requests.exceptions.RequestException as err:
        print(err)
        exit(1)
    print('Status:\n', resp.status_code)
    print('Headers:\n', resp.headers)
    print('Content:\n', resp.content)
    resp.close()
    return resp


# start
if os.path.exists(apiAccess['fileName']):
    print('File exist. Skip')
else:
    resp = getQcow2(apiAccess)
