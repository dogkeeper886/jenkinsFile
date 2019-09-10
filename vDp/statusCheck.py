import subprocess

cmd = 'ansible -u root kvm -m virt -a "name=vdp command=status"'
result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE)
print(result.stdout.decode())
