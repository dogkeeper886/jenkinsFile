import ftplib
import os

ftpInfo = {
    'ip': '10.206.5.20',
    'userName': os.environ['BITBUCKET_COMMON_CREDS_USR'],
    'password': os.environ['BITBUCKET_COMMON_CREDS_PSW'],
    'fileName': 'vscg-' + os.environ['szVer'] + '.ximg',
}
# ftp start
try:
    ftp_connection = ftplib.FTP(
        host=ftpInfo['ip'],
        user=ftpInfo['userName'],
        passwd=ftpInfo['password']
    )
except ftplib.Error as err:
    print(err)
    exit(1)

fList = ftp_connection.nlst()

if ftpInfo['fileName'] in fList:
    print('File exist:', ftpInfo['fileName'])
else:
    print('File not exist:', ftpInfo['fileName'])
    with open(ftpInfo['fileName'], 'rb') as fh:
        try:
            ftp_connection.storbinary('STOR ' + ftpInfo['fileName'], fh)
        except ftplib.Error as err:
            print(err)
            exit(1)
        fh.close()
    ftp_connection.close()
