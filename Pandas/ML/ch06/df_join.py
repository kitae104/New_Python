# 데이터프레임 결합
# join() 메소드는 두 데이터프레임의 행 인덱스를 기준으로 결합 (merge와 유사)
import pandas as pd

pd.set_option('display.max_columns', 10)                  # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', 20)                 # 출력할 열의 너비
pd.set_option('display.unicode.east_asian_width', True)   # 유니코드 사용 너비 조정

# 주식 데이터를 가져와서 데이터프레임 만들기
df1 = pd.read_excel("../../data/stock price.xlsx", index_col='id')
df2 = pd.read_excel("../../data/stock valuation.xlsx", index_col='id')

print(df1, '\n')
print(df2, '\n')

# 데이터프레임 결합(join)
df3 = df1.join(df2)
print(df3, '\n')

# 데이터프레임 결합(join) - 교집합
# 'id'열을 기준으로 df1, df2에 공통적인 부분 추출
df4 = df1.join(df2, how='inner')
print(df4, '\n')