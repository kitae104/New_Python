import pyautogui as gui

# # 특정 좌표로 이동 후 클릭하기
# gui.moveTo(44, 17)
# gui.click()
#
# # 특정 좌표 바로 클릭하기
# gui.click(44, 17)
#
# # 이미지 위치 알아내기
# i = gui.locateOnScreen('txt.png')
# print(i)
# # 이미지의 가운데 좌표 알아내기
# q = gui.center(i)
# gui.click(q)
#
# # 이미지의 가운데 좌표 한번에 알아내기
# i = gui.locateCenterOnScreen('txt.png')
# gui.click(i)

# 현재 마우스 위치 알아오기
print(gui.position())

# 계산기 번호 별로 이미지 만들기
#gui.screenshot('7.png', region=(1065, 477, 30, 30))
num7 = gui.locateCenterOnScreen('7.png')
num1 = gui.locateCenterOnScreen('1.png')

gui.click(num7)
gui.click(num1)
gui.click(num1)