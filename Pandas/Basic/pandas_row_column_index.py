# 데이터 프레임에서 열이름은 없고 열 인덱스만 있는 경우
# 파이썬 스라이싱과 iloc[...] 함수를 이용해서 열 데이터를 추출
import pandas as pd

df = pd.read_csv("../data/data_03_no_header.csv", header=None)
print(df)

# 모든 행과 2~3열까지 출력
print(df.iloc[:, 2:4])
print('-' * 50)

# 1행부터 3행, 1열부터 끝까지
print(df.iloc[1:4, 1:])
print('-' * 50)

# 모든 행과 0, 2, 3 열
print(df.iloc[:, [0, 2, 3]])
print('-' * 50)

# 1, 3행, 1, 3열
print(df.iloc[[1,3], [1, 3]])
print('-' * 50)

#===========================
# 조건에 따른 추출
#===========================
df3 = pd.read_csv("../data/data_03_no_header.csv", header=None, names=['Name', 'Country', 'Age', 'Job'])
print(df3)
print('-'*50)

# Country가 Korea인 경우
print(df3[df3.Country == 'Korea'])
print('-' * 50)

# Age가 > 30인 경우
print(df3[df3.Age > 30])
print('-'*50)

# Country가 USA가 아니고 Age가 > 33 인 경우
print(df3[(df3.Country != 'USA') & (df3.Age >= 33)])
print('-'*50)

# Country가 Korea 또는 Job이 Chef 인 경우
print(df3[(df3.Country =='Korea') | (df3.Job == 'Chef')])
print('-'*50)