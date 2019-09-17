import pexpect
import sys
from os import environ


class szcli:
    cmd = str()
    con = pexpect.spawn

    def __init__(self, ip, password):
        a = self.con('ssh admin@' + ip, encoding='utf-8', logfile=sys.stdout)
        a.expect('password:')
        a.sendline(password)
        a.expect('>')
        a.sendline('enable')
        a.expect('Password:')
        a.sendline(password)
        a.expect('#')
        self.con = a

    def __del__(self):
        self.con.sendline('logout')
        self.con.expect(pexpect.EOF)

    def upgrade(self):
        print('Start upgrade')
        self.con.sendline(
            'backup-upgrade ftp://scg:scg@10.206.20.107/vscg-' + environ['szVer'] + '.ximg')
        self.con.expect('[yes/no]')
        self.con.sendline('yes')
        self.con.expect('Starting to copy')
        self.con.sendline('')
        self.con.expect('Succeed to copy', timeout=300)
        self.con.sendline('')
        self.con.expect('Upload upgrade file')
        self.con.sendline('')
        self.con.expect('Verify upgrade status', timeout=300)
        self.con.sendline('')
        self.con.expect('[yes/no]', timeout=900)
        self.con.sendline('yes')
        self.con.expect('#')
        self.con.sendline('show backup-upgrade-state')
        self.con.expect('#')


a = szcli(environ['szIp'], environ['BITBUCKET_COMMON_CREDS_PSW'])
a.upgrade()
