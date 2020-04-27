#===============================================
# 브라우저 매크로 만들기
#===============================================
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 셀레니엄 사용하기 ()에 크롬 드라이버 경로 설정
driver = webdriver.Chrome()
url = 'https://www.google.co.kr/'
driver.get(url)

# 검색어 입력하고 엔터
driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys('파이썬')
driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys(Keys.ENTER)

# 여러개 중에 세번째 내용 클릭
driver.find_elements_by_css_selector('.LC20lb')[2].click()

#driver.close()