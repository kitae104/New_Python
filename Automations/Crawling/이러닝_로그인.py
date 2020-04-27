#===============================================
# 브라우저 매크로 만들기
#===============================================
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

url = 'https://cyber.inhatc.ac.kr/Main.do?cmd=viewHome&userDTO.localeKey=ko'

# 웹브라우저 불러오고 최대 크기로 만들기
driver.get(url)
#driver.maximize_window()

print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
# action을 사용해서 driver 제어를 위한 준비
action = ActionChains(driver)
time.sleep(1)

# 아이디 처리하기
driver.find_element_by_css_selector("#id").click()
driver.find_element_by_css_selector("#id").send_keys('2019010')

# 패스워드 처리하기
driver.find_element_by_css_selector("#pw").click()
driver.find_element_by_css_selector("#pw").send_keys('aqua0405@')

time.sleep(1)
# 버튼 클릭
driver.find_element_by_css_selector('.loginBtn').click()

print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])

driver.find_element_by_css_selector('.ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-icon-only.ui-dialog-titlebar-close').click()

#driver.close()