# 키보드 마우스 자동으로 움직이기
import pyautogui
import time

# 좌표 알아내기
print(pyautogui.position())

# 움직이기(픽셀 단위로 이동)
pyautogui.moveTo(100, 300, 2)   # 절대 위치 x, y, 시간
pyautogui.moveRel(0, 300)    # 상대 위치
pyautogui.moveRel(300, 0)    # 상대 위치

pyautogui.moveTo(47, 16)     # 파일 메뉴 위치로 이동

# 클릭하기 - 2초 후 클릭하기(메뉴 열었다 닫기)
pyautogui.click(clicks=2, interval=1)

# 파일 열기
pyautogui.moveTo(1164, 138, 1)
pyautogui.doubleClick()

# 잠시 기다리기 (파일이 열릴때까지)
time.sleep(2)

# 한자씩 입력하기와 문자열 입력하기
pyautogui.typewrite(['a','b','c', 'enter'])
pyautogui.typewrite('Hello World')