# 데이터프레임을 엑셀 형식으로 자장
import pandas as pd
import xlwt
import openpyxl

# 딕셔너리 데이터 타입 사용
persons_dict = {
    'Name' : ['John', 'Sabre', 'Kim', 'Sato'],
    'Country' : ['USA', 'France', 'Korea', 'Japan'],
    'Age' : [31, 33, 28, 40],
    'Job' : ['Student', 'Lawer', 'Developer', 'Chef']
}

df = pd.DataFrame(data=persons_dict, columns=['Name', 'Country', 'Age', 'Job'])
print(df)

# 엑셀 형식으로 저장 (.xls)
df.to_excel('../data/persons_02.xls')

# 엑셀 형식으로 저장 (.xlsx)
df.to_excel('../data/persons_03.xlsx')