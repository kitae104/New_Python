#===============================================
# 셀레니움 새 탭 열기
#===============================================
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

#time.sleep(10)                          # 무조건 10초 대기
driver.implicitly_wait(10)              # 10초까지 기다리기
driver.get('https://www.google.co.kr')
time.sleep(2)

# 자바 스크립트를 이용해서 탭 열기
driver.execute_script('window.open("https://naver.com");')
time.sleep(1)

driver.switch_to.window(driver.window_handles[1])
time.sleep(1)

driver.close()

driver.switch_to.window(driver.window_handles[0])
time.sleep(1)


