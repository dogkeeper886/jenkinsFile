import requests
import json

def apiFormat(api, endpoint):
    apiUrl = endpoint + api
    return apiUrl
glanceApi = apiFormat('/v2/images', 'http://10.206.5.12:9292')

# read token from file
with open('token.json','rt') as readToken:
    token = json.load(readToken)


# request
try:
    res = requests.request('GET', url=glanceApi, headers=token)
except requests.exceptions.RequestException as err:
    print(err)
    exit(1)

def readContent(res):
    rawData = res.content.decode()
    jData = json.loads(rawData)
    #print(json.dumps(content, indent=4))
    imgInfo = jData['images']
    imgList = list()
    for img in imgInfo:
        imgList.append(img['name'])
    return imgList
imgList = readContent(res)

print(imgList)





