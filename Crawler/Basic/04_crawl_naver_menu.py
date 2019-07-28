#네이버 메뉴 크롤링
import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)
bsObj = bs4.BeautifulSoup(html, "html.parser")

# 전체 문서 출력
# print(bsObj)

# 일부분만 출력 - find 특정 태그 찾기
# 특정한 부분만 출력하기 위해 class 사용
ul = bsObj.find("ul", {"class":"an_l"})
# print(ul)

# findAll을 사용하면 리스트로 출력 [<li></li>, <li></li>, ... ]
lis = ul.findAll("li")
print(lis)          # 하나의 리스트로 출력
print(len(lis))     # 리스트 안에 li 의 갯수
print("-" * 50)

for li in lis:      # 하나만 출력할 때는 lis[0]
    a_tag = li.find("a")
    span = a_tag.find("span", {"class":"an_txt"})
    print(span.text)    # 글자만 출력

# 메일
# 카페
# 블로그
# 지식인
# 쇼핑
# 네이버페이
# 네이버TV