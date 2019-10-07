import openstack
import sys
import urllib.request
import os


class opstk:
    def __init__(self):
        self.conn = None
        self.fileName = sys.argv[1]
        self.fileUrl = sys.argv[2]

    def create_connection(self, auth_url, domain, project_name, username, password):
        self.conn = openstack.connect(
            auth_url=auth_url,
            project_name=project_name,
            username=username,
            password=password,
            domain_name=domain,
            app_name='examples',
            app_version='1.0',
        )

    def list_images(self):
        imageList = list()
        for image in self.conn.image.images():
            imageList.append(image.name)
        return imageList

    def upload(self):
        try:
            data = open(self.fileName, 'rb')
        except IOError as err:
            print(err)
            exit(1)

        words = self.fileName.split('.')
        diskFormat = words[len(words)-1]
        print(diskFormat)
        image_attrs = {
            'name': self.fileName,
            'data': data,
            'disk_format': diskFormat,
            'container_format': 'bare',
            # 'visibility': 'public',
        }
        try:
            self.conn.image.upload_image(**image_attrs)
        except (openstack.exceptions.BadRequestException, openstack.exceptions.HttpException) as err:
            print(err)
            exit(1)
        data.close()

    def upload_image(self):
        if self.fileName not in self.list_images():
            print('File upload')
            if not os.path.exists(self.fileName):
                print('Download from remote')
                self.get_file()
            else:
                print('File at local')
            self.upload()
        else:
            print('File exist')

    def get_file(self):
        try:
            urllib.request.urlretrieve(self.fileUrl, filename=self.fileName)
        except urllib.error.URLError as err:
            print(err)
            exit(1)

if len(sys.argv) != 3:
    print('[FILE_NAME] [FILE_URL]')
    exit(1)

myConnect = opstk()
myConnect.create_connection(
    auth_url='http://10.206.6.112:5000/v3/',
    domain='Default',
    project_name='lab',
    username='environ['BITBUCKET_COMMON_CREDS_USR'],
    password='environ['BITBUCKET_COMMON_CREDS_PSW']'
)

myConnect.upload_image()
