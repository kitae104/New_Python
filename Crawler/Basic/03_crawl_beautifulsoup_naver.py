# BeautifulSoup을 이용하여 크롤링하기
import bs4
import urllib.request

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bsObj = bs4.BeautifulSoup(html, "html.parser")

# print(html.read())
# print(bsObj)

# 필요한 부분만 출력 시작은 div, 클래스 area_links 에 있는 자료
top_right = bsObj.find("div", {"class":"area_links"})
# print(top_right)

# a 태그만 뽑아오기
first_a = top_right.find("a")
print(first_a)

# 글짜만 뽑아오기
print(first_a.text)