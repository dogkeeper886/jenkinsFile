import openstack
from os import environ
import sys
import json


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

    def imageList(self):
        i = list()
        for image in self.conn.image.images():
            i.append(image.name)
        return i

    def fileExist(self, file):
        if file in self.imageList():
            print(file, 'file exist')
            return True
        else:
            print(file, 'not exist')
            return False

    def uploadImage(self, name):
        result = None
        if self.fileExist(name):
            print('Upload skip')
        else:
            print('Upload Image')
            data = open(name, 'rb')
            image_attrs = {
                'name': name,
                'data': data,
                'disk_format': 'qcow2',
                'container_format': 'bare',
                # 'visibility': 'public',
            }
            result = self.conn.image.upload_image(**image_attrs)
        return result


glance = opsk('http://10.206.6.112:5000/v3/', 'Default', 'lab',
              environ['BITBUCKET_COMMON_CREDS_USR'], environ['BITBUCKET_COMMON_CREDS_PSW'])

with open('env.json', 'rt') as fh:
    envInfo = json.load(fh)
uploadResult = glance.uploadImage(envInfo['imgName'])

print(uploadResult)
