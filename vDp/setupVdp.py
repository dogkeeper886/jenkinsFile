import pexpect
import sys
from os import environ
kvmIp = '10.206.6.111'
kvmUser = environ['BITBUCKET_COMMON_CREDS_USR']
kvmPass = environ['BITBUCKET_COMMON_CREDS_PSW']
cmd = 'ssh ' + kvmUser + '@' + kvmIp
vszIp = '192.168.162.5'

child = pexpect.spawn(cmd, encoding='utf-8')
child.logfile = sys.stdout
child.timeout = 600
# login kvm
child.expect('Password')
child.sendline(kvmPass)
child.expect('#')
# enter consile
child.sendline('virsh console vdp')
child.expect('Escape character')
child.sendline('')
# login vdp
child.expect('login')
child.sendline('admin')
child.expect('Password')
child.sendline('admin')
child.expect('>')
# enable
child.sendline('enable')
child.expect('Password')
child.sendline('admin')
child.expect('#')
# setup
child.sendline('setup')
# hostname
child.expect('Do you want to modify the vSZ-D hostname')
child.sendline('n')
# ip version support
child.expect('Select IP configuration')
child.sendline('1')
# management interface
child.expect('Select IP configuration')
child.sendline('2')
child.expect('Do you want to apply this network configuration')
child.sendline('y')
# data interface
child.expect('Select IP configuration')
child.sendline('2')
child.expect('Do you want to apply this network configuration')
child.sendline('y')
# dns
child.expect('Primary DNS')
child.sendline('10.10.10.10')
child.expect('Secondary DNS')
child.sendline('')
# nat ip
child.expect('Data Interface external NAT IP')
child.sendline('')
# cert
child.expect('Do you want to upload vSZ server certificate chain')
child.sendline('n')
# option 43
child.expect('Do you want to apply vSZ IP through DHCP Option 43')
child.sendline('n')
# vsz ip
child.expect('Please input vSZ Control address')
child.sendline(vszIp)
# connect
child.expect('(y/n)')
child.sendline('y')
# change password
child.expect('New password')
child.sendline('admin!234')
child.expect('Retype new password')
child.sendline('admin!234')
child.expect('New password')
child.sendline('admin!234')
child.expect('Retype')
child.sendline('admin!234')
child.expect('#')
child.close()
