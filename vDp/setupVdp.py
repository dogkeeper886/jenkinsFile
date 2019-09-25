import pexpect
import sys
from os import environ


class vdpCli:
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

    def setup(self, pass_word, szIp):
        self.con.sendline('setup')
        # hostname
        self.con.expect('Do you want to modify the vSZ-D hostname')
        self.con.sendline('n')
        # ip version support
        self.con.expect('Select IP configuration')
        self.con.sendline('1')
        # management interface
        self.con.expect('Select IP configuration')
        self.con.sendline('2')
        self.con.expect('Do you want to apply this network configuration')
        self.con.sendline('y')
        # data interface
        self.con.expect('Select IP configuration')
        self.con.sendline('2')
        self.con.expect('Do you want to apply this network configuration')
        self.con.sendline('y')
        # dns
        self.con.expect('Primary DNS')
        self.con.sendline('10.10.10.10')
        self.con.expect('Secondary DNS')
        self.con.sendline('')
        # nat ip
        self.con.expect('Data Interface external NAT IP')
        self.con.sendline('')
        # cert
        self.con.expect('Do you want to upload vSZ server certificate chain')
        self.con.sendline('n')
        # option 43
        self.con.expect('Do you want to apply vSZ IP through DHCP Option 43')
        self.con.sendline('n')
        # vsz ip
        self.con.expect('Please input vSZ Control address')
        self.con.sendline(szIp)
        # connect
        self.con.expect('(y/n)')
        self.con.sendline('y')
        # change password
        self.con.expect('New password')
        self.con.sendline(pass_word)
        self.con.expect('Retype new password')
        self.con.sendline(pass_word)
        self.con.expect('New password')
        self.con.sendline(pass_word)
        self.con.expect('Retype')
        self.con.sendline(pass_word)
        self.con.expect('#')


vdp = vdpCli(environ['vdpIp'], 'admin')
vdp.setup(environ['BITBUCKET_COMMON_CREDS_PSW'], environ['vszIp'])
