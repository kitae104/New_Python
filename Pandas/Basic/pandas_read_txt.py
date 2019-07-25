# tab으로 분리된 파일 읽기 - 헤더 테일 사용
import pandas as pd

df = pd.read_csv("../data/data_02.txt")
print(df)
print('-'*50)

df2 = pd.read_csv("../data/data_02.txt", sep='\t')
print(df2)
print('-'*50)

# 가장 앞의 5개
print(df2.head())
print('-'*50)

# 가장 앞에 2개
print(df2.head(2))
print('-'*50)

# 가장 뒤에 5개
print(df2.tail())
print('-'*50)

# 가장 뒤에 1개
print(df2.tail(1))
print('-'*50)