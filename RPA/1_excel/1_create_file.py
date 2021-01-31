# 엑셀 파일 만들기
from openpyxl import Workbook
wb = Workbook()             # 새 워크북 생성
ws = wb.active              # 현재 활성화된 sheet 가져옴
ws.title = "기태_파일"      # sheet 이름 변경
wb.save("sample.xlsx")      # 파일 저장
wb.close()
