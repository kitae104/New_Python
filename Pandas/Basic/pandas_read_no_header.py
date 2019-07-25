# 헤어가 없는 파일 읽기
import pandas as pd

# 그냥 읽으면 헤더에 첫번째 데이터가 나타남
df = pd.read_csv("../data/data_03_no_header.csv")
print(df)
print('-'*50)

# None으로 처리한 경우 숫자 0, 1, ... 이 나타남
df2 = pd.read_csv("../data/data_03_no_header.csv", header=None)
print(df2)
print('-'*50)

df3 = pd.read_csv("../data/data_03_no_header.csv", header=None, names=['Name', 'Country', 'Age', 'Job'])
print(df3)
print('-'*50)
