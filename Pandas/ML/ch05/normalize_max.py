# 각 열(변수)에 속하는 데이터 값을 동일한 크기 기준으로 나눈 비율로 나타내는 것을 정규화(normalization)라한다.
# 정규화를 거친 데이터의 범위는 0~1 또는 -1~1 이 된다.
import pandas as pd
import numpy as np
from sklearn import preprocessing

# read_csv() 함수로 df 생성
df = pd.read_csv('../../data/auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# horsepower 열의 누락 데이터('?') 삭제하고 실수형으로 변환 (3단계 수행)
df['horsepower'].replace("?", np.nan, inplace=True)         # '?'을 np.nan으로 변경
df.dropna(subset=['horsepower'], axis=0, inplace=True)      # 누락데이터 행을 삭제
df['horsepower'] = df['horsepower'].astype('float')         # 문자열을 실수형으로 변환

# horsepower 열의 통계 요약정보로 최대값(max)을 확인
print(df['horsepower'].describe())

print(df.horsepower.max())                  # 전체의 max
print(df['horsepower'].describe().max())    # describe 중 max

df['horsepower1'] = df.horsepower / abs(df['horsepower'].max())  # 최대값으로 나누어 정규화 수행
print(df.horsepower1.head())

print(df['horsepower1'].describe())

min_max = df.horsepower.max() - df.horsepower.min()
print(min_max)

df['horsepower2'] = (df.horsepower-df.horsepower.min()) / min_max  # 최대값으로 나누어 정규화 수행
print(df.horsepower2.head())

print(df['horsepower2'].describe())