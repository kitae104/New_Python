from selenium import webdriver
import time
import pyautogui

driver = webdriver.Chrome()

driver.get("https://naver.com")

# 잠시 다른 동작을 하기 위해 사용
pyautogui.alert("계속하려면 클릭하세요.")

driver.find_element_by_css_selector('.an_a.mn_comic').click()

# 잠시 멈출 때 사용함
i = int(input('계속하려면 아무키나 입력하세요.'))
if i == 1:
    driver.find_element_by_css_selector('.an_a.mn_comic').click()
else:
    driver.find_element_by_css_selector('.an_a.mn_news').click()