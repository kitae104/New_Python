# 네이버 뉴스 크롤링
from urllib.request import urlopen
import bs4

url = "https://news.naver.com/"
html = urlopen(url)
bsObj = bs4.BeautifulSoup(html, "html.parser")
#print(bsObj)

ul = bsObj.find("ul", {"class":"hdline_article_list"})
# print(ul)

lis = ul.findAll("li")

# 결과 출력하기
for li in lis:
    a_tag = li.find("a")
    print(a_tag.text.strip())   # 앞뒤 공백 제거하기

# 결과를 리스트로 생성하기
titles = [li.find("a").text.strip() for li in lis]
for title in titles:
    print("오늘의 뉴스 : ", title)
