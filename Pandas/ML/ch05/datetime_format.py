# 날짜 데이터 분리
import pandas as pd

df = pd.read_csv("../../data/stock-data.csv")

# 문자열인 날짜 데이터를 판다스 Timestamp로 변환
df['new_Date'] = pd.to_datetime(df['Date'])     # 새로운 열로 타입을 변경하여 생성
print(df.head())

# dt 속성을 이용하여 new_Date 열의 년월일 정보를 년, 월, 일로 구분
df['Year'] = df['new_Date'].dt.year
df['Month'] = df['new_Date'].dt.month
df['Day'] = df['new_Date'].dt.day
print(df.head())

# Timestamp를 Period로 변환하여 년월일 표기 변경하기
df['Date_yr'] = df['new_Date'].dt.to_period(freq='A')
df['Date_m'] = df['new_Date'].dt.to_period(freq='M')
print(df.head())

# 원하는 열을 새로운 행 인덱스로 지정
df.set_index('Date_m', inplace=True)
print(df.head())

# 날짜 인덱스 만들기
df.set_index('new_Date', inplace=True)
print(df.head())
print(df.index)

# 날짜 인덱스를 이용하여 데이터 선택하기
df_ym = df['2018-06']        # 해당 월
print(df_ym.head())

df_ym_cols = df.loc['2018-06', 'Close':'High']  # 열 범위 슬라이싱
print(df_ym_cols)

df_ymd = df['2018-06-29']       # 특정일의 정보
print(df_ymd)

df_ymd_range = df['2018-06-29':'2018-06-25']    # 날짜 범위 지정
print(df_ymd_range)

# 시간 간격 계산. 최근 180일 ~ 189일 사이의 값들만 선택하기
today = pd.to_datetime('2018-12-25')        # 기준일 생성
df['time_delta'] = today - df.index     # 날짜 차이 계산
df.set_index('time_delta', inplace=True)
df_180 = df['180 days':'189 days']
print(df_180)