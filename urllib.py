from urllib.request import urlopen
data = "language=python&framework=django"
f = urlopen("http://127.0.0.1:8000",bytes(data, encoding= 'utf-8'))
print(f.read(500).decode('utf-8'))



from urllib.request import urlopen, Request
from urllib.parse import urlencode

url = 'http://127.0.0.1:8000'
data = {
    'name': '김석훈',
    'email': 'shkim@naver.com',
    'url': 'http://www.naver.com'
}

encData = urlencode(data)
postData = bytes(encData, encoding='utf-8')
req = Request(url, data= postData)
req.add_header('Content-Type', 'application/x-www-form-urlencoded')
f = urlopen(req)
print(f.info())
print(f.read(500).decode('utf-8'))
Request()

from urllib.request import HTTPBasicAuthHandler, build_opener
auth_handler = HTTPBasicAuthHandler()
auth_handler.add_password(realm = 'ksh', user = 'shkim', passwd= ' shkimadmin',
                          uri= 'http://127.0.0.1:8000/auth/',)

opener = build_opener(auth_handler)
resp = opener.open('http://127.0.0.1:8000/auth/')
print(resp.read().decode('utf-8'))