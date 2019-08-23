import os
import sys
import json

if len(sys.argv) !=3:
    print('Invalid parameter [KEY] [VALUE]')
    exit(1)

envInfo = dict()
if os.path.exists('env.json'):
    with open('env.json', 'rt') as fh:
        envInfo = json.load(fh)
        fh.close()

envInfo[sys.argv[1]] = sys.argv[2]

with open('env.json', 'wt') as fh:
    fh.write(json.dumps(envInfo))
    fh.close()
