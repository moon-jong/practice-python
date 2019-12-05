from bs4 import BeautifulSoup as bs

html = """
<html><body>
<h1> body의 h1 </h1>
<p1> body의 p1 </p1>
<p2> body의 p2 </p2>
</body></html>
"""
soup = bs(html,'html.parser')

h1 = soup.html.body.h1
p1 = soup.html.body.p1
p2 = soup.html.body.p2

print("h1 =" + h1.string)
print("p1 =" + p1.string)
print("p2 =" + p2.string)


##id를 이용하여 html구문 찾기 find 매서드

html_2 = """
<html><body>
<h1 id = title> body의 h1 </h1>
<p1 id = text> body의 p1 </p1>
<p2 id = text> body의 p2 </p2>
</body></html>
"""
soup_2 = bs(html_2, 'html.parser')

title = soup_2.find(id = 'title')
text = soup_2.find(id = 'text')

print("#title" + title.string)
print('#text' + text.string)

#파이썬으로 로그인 하기

import requests
from urllib.parse import urljoin

USER = 'eg12555'
PASS = 'tlsans12'

session = requests.session()

user_data = {
    'm_id'     :USER,
    'm_passwd' : PASS
}
login_url = 'https://www.hanbit.co.kr/member/login_proc.php'

res = session.post(login_url, data= user_data)
res.raise_for_status()

mypage_url = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res = session.get(mypage_url)
res.raise_for_status()

soup = bs(res.text, 'html.parser')
mileage = soup.select_one(".mileage_section1 span").get_text()
ecoin = soup.select_one(".mileage_section2 span").get_text()
print("마일리지" + mileage)
print("이 코인" + ecoin)


request = requests.get('http://www.naver.com').text
print(request)
bin = requests.get('http://www.naver.com').content
print(bin)

#기상청 날씨 띄우기
import os.path
import urllib.request as req
url = 'http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnid=108'
savename = 'forecast.xml'
if not os.path.exists(savename):
    req.urlretrieve(url, savename)


xml = open(savename, "r", encoding= 'UTF-8')
soup = bs(xml, 'html.parser')

info = {}

for location in soup.find_all("location"):
    name = location.find('city').string
    weather = location.find('wf').string
    if not (weather in info):
        info[weather] = []
    info[weather].append(name)

for weather in info.keys():
    print("+",weather)
    for name in info[weather]:
        print("| - ",name)
