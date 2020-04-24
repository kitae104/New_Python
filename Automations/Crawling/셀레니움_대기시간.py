#===============================================
# 셀레니움 시간 대기
#===============================================
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

#time.sleep(10)                          # 무조건 10초 대기
driver.implicitly_wait(10)              # 10초까지 기다리기
driver.get('https://www.naver.com')

#button = driver.find_element_by_css_selector('#search_btn')
button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#search_btn')))
button.click()
