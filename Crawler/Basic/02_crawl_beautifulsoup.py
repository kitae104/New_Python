# BeautifulSoup을 이용하여 크롤링하기
import bs4

html_str = "<html><div></div></html>"
bsObj = bs4.BeautifulSoup(html_str, "html.parser")

# 객체 타입 확인
print(type(bsObj))

# 전체 문서 출력
print(bsObj)

# 해당 요소 출력
print(bsObj.find("div"))