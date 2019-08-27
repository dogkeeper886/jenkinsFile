import sys
import os
import urllib.request

if len(sys.argv) != 2:
    print('Invalid argument [SZ_VERSION]')
    exit(1)

def qcow2Info(szVer):
    qcow2 = {
        #'fileUrl': 'http://tdc-repository.arrisi.com:8081/nexus/content/repositories/releases/ruckus/official/mega/sz/5.1.2.0/sz_512/' + szVer + '/vscg/' + 'vscg-' + szVer + '.qcow2',
        'fileUrl': 'http://tdc-repository.arrisi.com:8081/nexus/content/repositories/releases/ruckus/official/mega/sz/5.2.0.0/ML/' + szVer + '/vscg/vscg-' + szVer + '.qcow2'
        'fileName': 'vscg-' + szVer + '.qcow2'
    }
    return qcow2

fileInfo = qcow2Info(sys.argv[1])

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