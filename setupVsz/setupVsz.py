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

    def vszh(self):
        self.conn.sendline('2')
        self.conn.expect('you want to install the "High Scale" profile? (y/n)')
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

    def dns(self):
        self.conn.expect('Primary DNS')
        self.conn.sendline('10.10.10.10')
        self.conn.expect('Secondary DNS')
        self.conn.sendline('')
        self.conn.expect('Do you want to apply the settings')
        self.conn.sendline('y')

    def setup(self, passWord, profile):
        self.conn.sendline('setup')
        self.conn.expect('Select vSZ Profile (1/2)')

        if profile == 'e':
            self.vsze
        else:
            self.vszh

        self.vszIp()
        self.ipv4()
        self.dns()

        # nat ip
        self.conn.expect('Data Interface external NAT IP')
        self.conn.sendline('')
        # cert
        self.conn.expect('Do you want to upload vSZ server certificate chain')
        self.conn.sendline('n')
        # option 43
        self.conn.expect('Do you want to apply vSZ IP through DHCP Option 43')
        self.conn.sendline('n')
        # vsz ip
        self.conn.expect('Please input vSZ Control address')
        self.conn.sendline(self.vszIp)
        # connect
        self.conn.expect('(y/n)')
        self.conn.sendline('y')
        # change password
        self.conn.expect('New password')
        self.conn.sendline(passWord)
        self.conn.expect('Retype new password')
        self.conn.sendline(passWord)
        self.conn.expect('New password')
        self.conn.sendline(passWord)
        self.conn.expect('Retype')
        self.conn.sendline(passWord)
        self.conn.expect('#')


vsz = setupVsz(environ['vszIp'])
vsz.setup(environ['BITBUCKET_COMMON_CREDS_PSW'], environ['profile'])

