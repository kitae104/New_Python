#===============================================
# 이미지 다운로드
#===============================================

from urllib.request import  urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

# 검색할 사이트  + 검색어
baseUrl = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
search = "감자" #input("검색어를 입력하세요.")

# 한글 처리를 위해 urllib.parse.quote_plus 사용
url = baseUrl + quote_plus(search)
print(url)

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')   # HTML 형태로 읽어오기

# find_all 조건에 맞는거 다 찾기(클래스 명에서 찾기)
imgs = soup.find_all(class_='_img')
print(imgs[0])

n = 1

for i in imgs:
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f:     # 파일을 열고 f로 불러옴
        # 저장할 이름 생성
        with open('./img/' + search + str(n)+'.jpg', 'wb') as h: # wb 바이너리로 쓰기
            img = f.read()
            h.write(img)
    n = n + 1
    print(imgUrl)

print('다운로드 완료')