import os
import urllib.request

apiAccess = {
    'endpoint': 'http://tdc-repository.arrisi.com:8081/nexus/content/repositories/releases/ruckus/official/mega/sz',
    'api': '/5.2.0.0/ML/' + os.environ['szVer'] + '/vscg/vscg-' + os.environ['szVer'] + '.qcow2',
    'fileName': 'vscg-' + os.environ['szVer'] + '.qcow2'
}


# start
if os.path.exists(apiAccess['fileName']):
    print('File exist. Skip')
else:
    apiUrl = apiAccess['endpoint'] + apiAccess['api']
    urllib.request.urlretrieve(apiUrl, filename=apiAccess['fileName'])
