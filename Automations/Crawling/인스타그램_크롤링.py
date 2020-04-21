#===============================================
# 인스타그램 크롤링
#===============================================
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time

baseUrl = "https://www.instagram.com/explore/tags/"
plusUrl = "programmer" # input("검색할 태그를 입력하세요 : ")
url = baseUrl + quote_plus(plusUrl)

# 셀레니엄 이용하기 - 드라이버 버전 확인
driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)   # 3초 기다림

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 태그에 해당하는 모두 다 가져옴
insta = soup.select("v1Nh3.kIKUG._bz0w")
print(insta)

driver.close()