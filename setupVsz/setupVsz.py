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

    def vszProfile(self, proFIle):
        self.conn.sendline('setup')
        self.conn.expect('(1/2)')
        self.conn.sendline(proFIle)
        self.conn.expect('(y/n)')
        self.conn.sendline('y')

    def vszIpMode(self, ipMode):
        self.conn.expect('(1/2)')
        self.conn.sendline(ipMode)

vsz = setupVsz(environ['vszIp'])
vsz.vszProfile(environ['vszProfile'])
vsz.vszIpMode(environ['vszIpMode'])
