import pexpect
import sys
from os import environ


class setupVsz:
    def __init__(self, vszIp, profle, natIp):
        self.vszIp = vszIp
        self.profile = profle
        self.natIp = natIp
        self.conn = pexpect.spawn(
            'ssh admin@' + self.vszIp, encoding='utf-8', logfile=sys.stdout)
        self.conn.timeout = 60
        self.conn.expect('Are you sure you want to continue connecting')
        self.conn.sendline('yes')
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

    def vszh(self):
        self.conn.sendline('2')
        self.conn.expect(
            'Are you sure you want to install the "High Scale" profile? (y/n)')
        self.conn.sendline('y')

    def vsze(self):
        self.conn.sendline('1')
        self.conn.expect(
            'Are you sure you want to install the "Essentials" profile? (y/n)')
        self.conn.sendline('y')

    def ipv4(self):
        self.conn.expect('Select address type')
        self.conn.sendline('1')
        self.conn.expect('Select IP configuration')
        self.conn.sendline('2')
        self.conn.expect('Are these correct')
        self.conn.sendline('y')

    def dns(self):
        self.conn.expect('Primary DNS')
        self.conn.sendline('10.10.10.10')
        self.conn.expect('Secondary DNS')
        self.conn.sendline('')
        self.conn.expect('Control NAT IP:')
        self.conn.sendline(self.natIp)
        self.conn.expect('press Enter to continue')
        self.conn.sendline('')
        self.conn.expect('#')

    def setupNetwork(self):
        self.conn.sendline('setup')
        self.conn.expect('Select vSZ Profile')

        if self.profile == '1':
            self.vsze
        elif self.profile == '2':
            self.vszh

        self.vszIp()
        self.ipv4()
        self.dns()


vsz = setupVsz(environ['vszIp'], environ['vszProfile'], environ['vszNatIp'])
vsz.setupNetwork()
