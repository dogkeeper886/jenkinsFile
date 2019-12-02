from ftplib import FTP
from sys import argv
import os
import urllib.request
from os import environ


class file_check:
    def __init__(self):
        self.fileName = argv[1]
        self.filePath = argv[2]
        self.ftpUname = environ['BITBUCKET_COMMON_CREDS_USR']
        self.ftpPword = environ['BITBUCKET_COMMON_CREDS_PSW']
        self.ftp = FTP()

    def __del__(self):
        self.ftp.close()

    def ftp_check(self):
        ftpStatus = bool()
        self.ftp = FTP('10.206.5.22')
        self.ftp.login(user='scg', passwd='scg')
        if self.fileName in self.ftp.nlst():
            print('File exist at FTP')
            ftpStatus = True
        else:
            print('File does not exist at FTP')
            ftpStatus = False
        return ftpStatus

    def disk_check(self):
        diskStatus = bool()
        if os.path.exists(self.fileName):
            print('File exist at local')
            diskStatus = True
        else:
            print('File does not exist at local')
            diskStatus = False
        return diskStatus

    def get(self):
        try:
            urllib.request.urlretrieve(self.filePath, filename=self.fileName)
        except urllib.error.URLError as err:
            print(err)
            exit(1)

    def upload(self):
        print('Upload start')
        self.ftp.storbinary("STOR " + self.fileName, open(self.fileName, 'rb'))

    def check(self):
        if self.ftp_check():
            print('Skip')
        else:
            if self.disk_check():
                print('Prepare upload')
            else:
                print('Prepare download and upload')
                self.get()
            self.upload()


if len(argv) != 3:
    print('[FILE_NAME] [FILE_PATH]')
    exit(1)

myFile = file_check()
myFile.check()
