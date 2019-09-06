from os import environ as env
import glanceclient.v2.client as glclient
import keystoneclient.v3 as keystoneclient
import json

keystone = keystoneclient.Client(
    username=env['BITBUCKET_COMMON_CREDS_USR'],
    password=env['BITBUCKET_COMMON_CREDS_PSW'],
    project_domain_name=env['OS_PROJECT_DOMAIN_NAME'],
    project_name=env['OS_PROJECT_NAME'],
    auth_url=env['OS_AUTH_URL']
)

glance_endpoint = keystone.service_catalog.url_for(service_type='image')
glance = glclient.Client(glance_endpoint, token=keystone.auth_token)
listGen = glance.images.list()
info = list(listGen)
imageList = list()
for imageInfo in info:
    imageList.append(imageInfo.name)
print(imageList)

fileName = 'vdp-' + env['szVer'] + '.qcow2'
if fileName in imageList:
    print('File exist', fileName)
else:
    print('File not found', fileName)
    with open(fileName) as fimage:
        glance.images.create(
            name="myimage",
            is_public=False,
            disk_format="qcow2",
            container_format="bare",
            data=fimage
        )

