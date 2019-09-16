import pexpect
import sys


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

    def show_dp(self):
        with open('dp.info', 'wt') as fh:
            self.con.logfile = fh
            self.con.sendline('show data-plane')
            self.con.expect('#')
        self.con.logfile = sys.stdout


a = szcli('192.168.162.5', 'admin!234')
a.show_dp()
