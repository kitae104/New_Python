# 시계열 데이터
# 특정한 시점을 기록하는 Timestamp와 두 시점 사이의 일정한 기간을 나타내는 Period
import pandas as pd

df = pd.read_csv("../../data/stock-data.csv")   # 헤더가 있는 경우는 header=None을 사용하지 않는다.

print(df.head())
print(df.info())

# 문자열 데이터(시리즈 객체)를 판다스 Timestamp로 변환
df['new_Date'] = pd.to_datetime(df['Date'])      #df에 새로운 열로 추가
print(df.head())
print(df.info())
print(type(df['new_Date'][0]))  # 개별 원소의 타입

# 시계열 값으로 변환된 열을 새로운 행 인덱스로 지정. 기존 날짜 열은 삭제
df.set_index('new_Date', inplace=True)
df.drop('Date', axis=1, inplace=True)       # 세로(열) 방향으로 제거
print(df.head())    # 내림차순으로 정렬(최신 날짜순)
print(df.info())