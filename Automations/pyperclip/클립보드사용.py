# 클립보드 사용하기
import pyperclip
pyperclip.copy('hello world')   # 클립보드 저장
pyperclip.paste()                   # 붙여넣기

i = '안녕하세요.'
pyperclip.copy(i)
