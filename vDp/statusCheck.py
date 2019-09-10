import subprocess
import re
cmd = 'ansible -u root kvm -m virt -a "name=vdp command=status"'
result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE)
print(result.stdout.decode())

text = result.stdout.decode()
j = re.findall("\"status\": \"(.*)\"", text)

if j[0] != 'shutdown':
    print('Instance status is not shutdown')
    exit(1)
else:
    print('Instance status is shutdown')
