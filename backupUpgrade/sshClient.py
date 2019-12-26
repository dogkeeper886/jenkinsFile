import pexpect
import sys
from os import environ
from sys import argv


class sshClient:
    def __init__(self):
        self.szIp = argv[1]
        self.fileName = argv[2]
        self.sName = environ['BITBUCKET_COMMON_CREDS_USR']
        self.sPassword = environ['BITBUCKET_COMMON_CREDS_PSW']
        self.conn = None

    def __del__(self):
        pass

    def ssh_start(self):
        cmd = 'ssh ' + self.sName + '@' + self.szIp
        self.conn = pexpect.spawn(cmd, encoding='utf-8', logfile=sys.stdout)
        self.conn.expect('password:')
        self.conn.sendline(self.sPassword)
        self.conn.expect('>')
        self.conn.sendline('enable')
        self.conn.expect('Password:')
        self.conn.sendline(self.sPassword)
        self.conn.expect('#')

    def upgrade_start(self):
        print('Start upgrade')
        self.conn.sendline(
            'backup-upgrade ftp://scg:scg@10.206.5.22/' + self.fileName)
        self.conn.expect('[yes/no]')
        self.conn.sendline('yes')
        self.conn.expect('Starting to copy')
        self.conn.sendline('')
        self.conn.timeout = 300
        self.conn.expect('Succeed to copy')
        self.conn.sendline('')
        self.conn.expect('Upload upgrade file')
        self.conn.sendline('')
        self.conn.expect('Verify upgrade status')
        self.conn.sendline('')
        self.conn.timeout = 900
        self.conn.expect('[yes/no]')
        self.conn.sendline('yes')
        self.conn.expect('#')
        self.conn.sendline('show backup-upgrade-state')
        self.conn.expect('#')


if len(argv) != 3:
    print('[SZ_IP] [FILE_NAME]')
    exit(1)

mySsh = sshClient()
mySsh.ssh_start()
mySsh.upgrade_start()
