import openstack
from os import environ
import sys
import json


class opsk:
    conn = None
    imageName = str()
    instanceName = str()
    instanceId = str()

    def __init__(self, auth_url, domain, project_name, username, password):
        self.conn = openstack.connect(
            auth_url=auth_url,
            project_name=project_name,
            username=username,
            password=password,
            domain_name=domain,
            app_name='examples',
            app_version='1.0',
        )

    def __del__(self):
        self.conn.close()

    def findImage(self):
        imageInfo = self.conn.compute.find_image(self.imageName)
        return imageInfo.id

    def rebuildServer(self, imageName, instanceName, instanceId):
        self.imageName = imageName
        self.instanceName = instanceName
        self.instanceId = instanceId
        rebuildResult = self.conn.compute.rebuild_server(
            server=self.instanceId, image=nova.findImage(), name=self.instanceName, admin_password='')
        return rebuildResult

    def waitForServer(self, server):
        waitResult = self.conn.compute.wait_for_server(server)
        return waitResult


# openstack.connection
projectName = environ['projectName']

nova = opsk('http://10.206.6.112:5000/v3/', 'Default', projectName,
            environ['BITBUCKET_COMMON_CREDS_USR'], environ['BITBUCKET_COMMON_CREDS_PSW'])


with open('/var/lib/jenkins/.jenkins/workspace/rebuild_start/env.json', 'rt') as fh:
    envInfo = json.load(fh)
# openstack.compute.v2.server.Server.rebuild
rebuildInfo = nova.rebuildServer(
    envInfo['imgName'], environ['instanceName'], environ['instanceId'])
print(rebuildInfo)
# wait for server active
rebuildInfo = nova.waitForServer(rebuildInfo)
print(rebuildInfo)
