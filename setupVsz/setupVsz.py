import pexpect
import sys
from os import environ


class setupVsz:
    def __init__(self, vszIp):
        self.vszIp = vszIp
        self.conn = pexpect.spawn(
            'ssh admin@' + self.vszIp, encoding='utf-8', logfile=sys.stdout)
        self.conn.timeout = 60
        self.conn.expect('password:')
        self.conn.sendline('admin')
        self.conn.expect('>')
        self.conn.sendline('enable')
        self.conn.expect('Password:')
        self.conn.sendline('admin')
        self.conn.expect('#')

    def __del__(self):
        self.conn.sendline('logout')
        self.conn.expect(pexpect.EOF)


vsz = setupVsz(environ['vszIp'])
