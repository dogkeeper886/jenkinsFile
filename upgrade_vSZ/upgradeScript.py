import pexpect
import os

szInfo = {
    'ip': os.environ['szIp'],
    'userName': os.environ['BITBUCKET_COMMON_CREDS_USR'],
    'passphrase': os.environ['BITBUCKET_COMMON_CREDS_PSW'],
    'szVer': os.environ['szVer']
}

cmd = 'ssh ' + szInfo['userName'] + '@' + szInfo['ip']
try:
    child = pexpect.spawn(cmd, encoding='utf-8')
except:
    exit(1)

child.logfile = sys.stdout
child.timeout = 600

child.expect('password:')
child.sendline(szInfo['passphrase'])
child.expect('>')
child.sendline('enable')
child.expect('Password:')
child.sendline(szInfo['passphrase'])
child.expect('#')

ftpInfo = {
    'userName': 'jack',
    'passphrase': 'jack1234',
    'ip': '10.206.5.20'
}

sendCmd = 'backup-upgrade ftp://' + ftpInfo['userName'] + ':' + ftpInfo['passphrase'] + '@' + ftpInfo['ip'] + '/vscg-' + szInfo['szVer'] + '.ximg'
child.sendline(sendCmd)

child.expect('[yes/no]')
child.sendline('yes')
child.expect('Starting to copy')
child.expect('Succeed to copy')
child.expect('Upload upgrade file')
child.expect('Verify upgrade status')
child.expect('[yes/no]')
child.sendline('yes')
child.expect('#')
child.sendline('show backup-upgrade-state')
child.expect('#')








