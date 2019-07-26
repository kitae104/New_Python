# 네이버 크롤링하기
import urllib.request

url = "https://www.naver.com"
html = urllib.request.urlopen(url)

print(html.read())