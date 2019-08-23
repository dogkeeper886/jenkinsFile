import pexpect
import sys

if len(sys.argv) != 5:
    print('Invalid parameter [IP] [USER_NAME] [PASSWORD] [SZ_VER]')
    exit(1)

szInfo = {
    'ip': sys.argv[1],
    'userName': sys.argv[2],
    'passphrase': sys.argv[3],
    'szVer': sys.argv[4]
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








