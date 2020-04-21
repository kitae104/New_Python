#===============================================
# 구글 크롤링
#===============================================
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

baseUrl = 'https://www.google.com/search?q='
plusUrl = '파이썬'  # input('무엇을 검색할까요?')
url = baseUrl + quote_plus(plusUrl)
print(url)

# 셀레니엄 사용하기
driver = webdriver.Chrome()
driver.get(url)

# 열린 페이지 정보 가져오기
html = driver.page_source
soup = BeautifulSoup(html)

# 제목과 주소 가져오기
r = soup.select('.r')   # 리스트 형식으로 가져옴
for i in r:
    print(i.select_one('.LC20lb.DKV0Md').text)  # 제목
    print(i.a.attrs['href'])  # URL (해당 클래스안에서


driver.close()