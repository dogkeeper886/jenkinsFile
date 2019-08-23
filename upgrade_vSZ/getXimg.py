import sys
import os
import urllib.request

if len(sys.argv) != 2:
    print('Invalid argument [SZ_VERSION]')
    exit(1)

def ximgInfo(szVer):
    ximg = {
        'fileUrl': 'http://tdc-repository.arrisi.com:8081/nexus/content/repositories/releases/ruckus/official/mega/sz/5.1.2.0/sz_512/' + szVer + '/vscg/' + szVer + '.ximg',
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