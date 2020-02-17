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

    def cluster(self, clusterName, conDes):
        self.conn.sendline('setup')
        self.conn.expect('(y/n)')
        self.conn.sendline('n')
        self.conn.expect('(c/j)')
        self.conn.sendline('c')
        self.conn.expect('Cluster Name')
        self.conn.sendline(clusterName)
        self.conn.expect('Controller Description')
        self.conn.sendline(conDes)
        self.conn.expect('(y/n)')
        self.conn.sendline('y')

    def nat(self, natIp):
        pass
        self.conn.expect('(y/n)')
        self.conn.sendline('y')
        self.conn.expect('NAT IP')
        self.conn.sendline(natIp)
        self.conn.expect('NTP Serve')
        self.conn.sendline('tock.stdtime.gov.tw')
        self.conn.expect('(y/n)')
        self.conn.sendline('n')

    def admPwd(self, admPwd):
        self.conn.expect('admin password')
        self.conn.sendline(admPwd)
        self.conn.expect('password again')
        self.conn.sendline(admPwd)
        self.conn.expect('command password')
        self.conn.sendline(admPwd)
        self.conn.expect('password again')
        self.conn.sendline(admPwd)
        self.conn.expect(' password done')

    def monitor(self):
        self.conn.expect('Starting setup')
        self.conn.timeout = 2700
        self.conn.expect('Press the enter key to continue')
        self.conn.sendline('')


vsz = setupVsz(environ['vszIp'])
vsz.cluster(environ['vszClusterName'], environ['vszConDes'])
vsz.nat(environ['vszNatIp'])
vsz.admPwd(environ['BITBUCKET_COMMON_CREDS_PSW'])
vsz.monitor()
