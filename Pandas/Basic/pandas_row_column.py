# 행 데이터 추출 하기
# 연속적인 경우에는 Slicing 기능 사용
# 불연속적인 경우에는 loc[] 함수를 이용
import pandas as pd

df = pd.read_csv("../data/data_01.csv")
# 전체 출력
print(df)
print("-"*50)

#=================================
# 행 추출 하기
#=================================
# 처음부터 3전까지 0, 1, 2
print(df[:3])
print("-"*50)

# 3, 4행
print(df[3:5])
print("-"*50)

# 4행 이후 모두
print(df[4:])
print("-"*50)

# 불연속 데이터는 loc을 사용
print(df.loc[0])
print("-"*50)

# 0과 3행 출력
print(df.loc[[0, 3]])
print("-"*50)

# 1, 2, 5행 출력
print(df.loc[[1,2,5]])
print("-"*50)

#=================================
# 열 추출 하기
#=================================
# 열 이름을 이용해서 가져오기
print(df['Country'])
print("-"*50)

# 하나의 열 데이터 추출
print(df.Country)
print("-"*50)

# 2개의 열 데이터 출력
print(df[['Name', 'Country']])
print("-"*50)