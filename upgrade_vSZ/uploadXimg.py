import ftplib
import sys

if len(sys.argv) != 5:
    print('Invalid parameter [IP] [USERNAME] [PASWORD] [szVer]')
    exit(1)

ftpInfo = {
    'server': sys.argv[1],
    'userName': sys.argv[2],
    'password': sys.argv[3],
    'fileName': 'vscg-' + sys.argv[4] + '.ximg',
}

try:
    ftp_connection = ftplib.FTP(ftpInfo['server'], ftpInfo['userName'], ftpInfo['password'])
    fList = ftp_connection.nlst()
except ftplib.Error as err:
    print(err)
    exit(1)

def fileUpload():
    fh = open(ftpInfo['fileName'],'rb')
    fhCmd = 'STOR ' + ftpInfo['fileName']
    try:
        ftp_connection.storbinary(fhCmd, fh)
        fh.close()
    except ftplib.Error as err:
        print(err)
        exit(1)
    

if ftpInfo['fileName'] in fList:
    print('File exist:', ftpInfo['fileName'])
else:
    #print('File not exist:', ftpInfo['fileName'])
    fileUpload()

ftp_connection.close()
