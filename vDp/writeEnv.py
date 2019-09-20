from os import environ
from os.path import exists
from sys import argv
import json


class setupEnv:
    env = dict()
    fileName = str()

    def __init__(self, fileName):
        self.fileName = fileName
        if exists(fileName):
            self.readEnv()

    def readEnv(self):
        with open(self.fileName, 'rt') as fh:
            self.env = json.load(fh)

    def writeEnv(self):
        with open(self.fileName, 'wt') as fh:
            json.dump(self.env, fh)


envInfo = setupEnv('env.json')
envInfo.env[argv[1]] = argv[2]
envInfo.writeEnv()
print(envInfo.env)
