import openstack
from os import environ
import sys


class opsk:
    conn = None

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

    def findImage(self, imageName):
        imageInfo = self.conn.compute.find_image(imageName)
        return imageInfo.id

    def rebuildServer(self, imageName):
        rebuildResult = self.conn.compute.rebuild_server(
            server='53d98b98-adf8-40b8-83e5-f5caf7151ce7', image=nova.findImage(imageName), name='vdp', admin_password='')
        return rebuildResult

    def waitForServer(self, server):
        waitResult = self.conn.compute.wait_for_server(server)
        return waitResult


# openstack.connection
nova = opsk('http://10.206.6.112:5000/v3/', 'Default', 'lab',
            environ['BITBUCKET_COMMON_CREDS_USR'], environ['BITBUCKET_COMMON_CREDS_PSW'])

imageName = 'vdp-' + environ['szVer'] + '.qcow2'
# openstack.compute.v2.server.Server.rebuild
rebuildInfo = nova.rebuildServer(imageName)
print(rebuildInfo)
# wait for server active
rebuildInfo = nova.waitForServer(rebuildInfo)
print(rebuildInfo)
