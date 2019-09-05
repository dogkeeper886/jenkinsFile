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
imageList = list(listGen)
#print(json.dumps(imageList, indent=4))
for image in imageList:
    print(image.name)
