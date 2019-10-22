import pexpect
import sys
from os import environ


class setupVdp:
    def __init__(self, vszIp, vdpIp):
        self.vszIp = vszIp
        self.vdpIp = vdpIp
        self.conn = pexpect.spawn(
            'ssh admin@' + self.vdpIp, encoding='utf-8', logfile=sys.stdout)
        self.conn.timeout = 120
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

    def setup(self, passWord):
        self.conn.sendline('setup')
        # hostname
        self.conn.expect('Do you want to modify the vSZ-D hostname')
        self.conn.sendline('n')
        # ip version support
        self.conn.expect('Select IP configuration')
        self.conn.sendline('1')
        # management interface
        self.conn.expect('Select IP configuration')
        self.conn.sendline('2')
        self.conn.expect('Do you want to apply this network configuration')
        self.conn.sendline('y')
        # data interface
        self.conn.expect('Select IP configuration')
        self.conn.sendline('2')
        self.conn.expect('Do you want to apply this network configuration')
        self.conn.sendline('y')
        # dns
        self.conn.expect('Primary DNS')
        self.conn.sendline('10.10.10.10')
        self.conn.expect('Secondary DNS')
        self.conn.sendline('')
        # nat ip
        self.conn.expect('Data Interface external NAT IP')
        self.conn.sendline('')
        # cert
        #self.conn.expect('Do you want to upload vSZ server certificate chain')
        #self.conn.sendline('n')
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


vdp = setupVdp(environ['vszIp'], environ['vdpIp'])
vdp.setup(environ['BITBUCKET_COMMON_CREDS_PSW'])
