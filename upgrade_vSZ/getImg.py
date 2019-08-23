import sys
import os
import urllib.request

if len(sys.argv) != 2:
    print('Invalid argument [SZ_VERSION]')
    exit(1)

def ximgInfo(szVer):
    ximg = {
        'fileUrl': 'http://tdc-repository.arrisi.com:8081/nexus/content/groups/ruckus-public/ruckus/official/mega/sz/ML/5.2.0.0/vscg/' + szVer + '/vscg-' + szVer + '.ximg',
        'fileName': 'vscg-' + szVer + '.ximg'
    }
    return ximg

fileInfo = ximgInfo(sys.argv[1])

def getImg():
    try:
        urllib.request.urlretrieve(fileInfo['fileUrl'], filename=fileInfo['fileName'])
    except urllib.error.URLError as err:
        print(err)
        exit(1)

if os.path.exists(fileInfo['fileName']): 
    print('File exist')
else:
    getImg()