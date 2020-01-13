# 엑셀 파일 읽기
import pandas as pd

file_path = "../../data/persons_02.xls"
df1 = pd.read_excel(file_path)  # 헤더가 있는 것이 기본 header=0 (default 옵션)
print(df1)

df2 = pd.read_excel(file_path, header=None)
print(df2)