#===============================================
# 네이버 블로그 크롤링
#===============================================

import urllib.request
from bs4 import BeautifulSoup
import urllib.parse

baseUrl = "https://search.naver.com/search.naver?where=post&sm=tab_jum&query="
search = input("검색어를 입력하세요.")

# 한글 처리를 위해 urllib.parse.quote_plus 추가
url = baseUrl + urllib.parse.quote_plus(search)
print(url)
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# find_all 조건에 맞는거 다 찾기
title = soup.find_all(class_='sh_blog_title')
print(len(title))

for i in title:
    print(i.attrs['title'])
    print(i.attrs['href'])
    print()