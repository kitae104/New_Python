# 데이터프레임 병합
# merge() : SQL의 join과 비슷한 방식으로 어떤 기준에 의해 두 데이터프레임을 병합하는 개념
# 기준이 되는 열이나 인덱스를 키(key)라 한다. 키가 되는 열이나 인덱스는 반드시 양쪽 데이터프레임에 모두 존재해야 한다.
import pandas as pd

pd.set_option('display.max_columns', 10)                  # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', 20)                 # 출력할 열의 너비
pd.set_option('display.unicode.east_asian_width', True)   # 유니코드 사용 너비 조정

# 주식 데이터를 가져와서 데이터프레임 만들기
df1 = pd.read_excel("../../data/stock price.xlsx")
df2 = pd.read_excel("../../data/stock valuation.xlsx")

print(df1, '\n')
print(df2, '\n')

# 데이터프레임 합치기 - 교집합
merge_inner = pd.merge(df1, df2, how='inner', on=None)
print(merge_inner, '\n')

# 데이터프레임 합치기 - 합집합
merge_outer = pd.merge(df1, df2, how='outer', on='id')
print(merge_outer, '\n')

# 데이터프레임 합치기 - 왼쪽 데이터프레임 기준, 키 값 분리
# 왼쪽에 있는 stock_name이 기준이 된다.
merge_left = pd.merge(df1, df2, how='left', left_on='stock_name', right_on='name')
print(merge_left, '\n')

# 데이터프레임 합치기 - 오른쪽 데이터프레임 기준, 키 값 분리
# 오른쪽에 있는 name이 기준이 된다.
merge_right = pd.merge(df1, df2, how='right', left_on='stock_name', right_on='name')
print(merge_right, '\n')

# 불린 인덱싱과 결합하여 원하는 데이터 찾기
price = df1[df1['price'] < 50000]
print(price.head(), '\n')

value = pd.merge(price, df2)
print(value)