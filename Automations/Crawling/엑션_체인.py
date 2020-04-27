#===============================================
# 엑션 체인 사용하기
#===============================================
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

url = 'https://www.google.co.kr'

# 웹브라우저 불러오고 최대 크기로 만들기
driver.get(url)
#driver.maximize_window()

# action을 사용해서 driver 제어를 위한 준비
action = ActionChains(driver)

# 아이디 처리하기
driver.find_element_by_css_selector("#gb_70").click()
action.send_keys('aqua0405').perform()
driver.find_element_by_css_selector(".CwaK9").click()

time.sleep(2)
driver.find_element_by_css_selector(".whsOnd.zHQkBf").send_keys('kjmkjm1@')
driver.find_element_by_css_selector(".CwaK9").click()

# Gmail
driver.find_element_by_css_selector(".gb_h.gb_i").click()
time.sleep(2)
#driver.close()