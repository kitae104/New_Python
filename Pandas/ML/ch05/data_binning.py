# 연속적인 변수를 일정한 구간으로 나누고, 각 구간을 범주형 이산 변수로 변환하는 과정을 구간 분할(binning)이라 한다.
# 판다스 cut() 함수를 이용하면 연속 데이터를 여러 구간으로 나누고 범주형 테이터로 변환할 수 있다.
import pandas as pd
import numpy as np

# read_csv() 함수로 df 생성
df = pd.read_csv('../../data/auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# horsepower 열의 누락 데이터('?') 삭제하고 실수형으로 변환 (3단계 수행)
df['horsepower'].replace("?", np.nan, inplace=True)         # '?'을 np.nan으로 변경
df.dropna(subset=['horsepower'], axis=0, inplace=True)      # 누락데이터 행을 삭제
df['horsepower'] = df['horsepower'].astype('float')         # 문자열을 실수형으로 변환

# np.histogram 함수로 3개의 bin으로 나누는 경계 값의 리스트 구하기
count, bin_dividers = np.histogram(df['horsepower'], bins=3)    # 3개의 구간 생성
print(bin_dividers)

# 3개의 bin에 이름 지정(각 구간의 이름 설정)
bin_names = ['저출력', '보통출력', '고출력']

# pd.cut 함수로 각 데이터를 3개의 bin에 할당
df['hp_bin'] = pd.cut(x=df['horsepower'],       # 데이터 배열
                      bins=bin_dividers,        # 경계 값 리스트
                      labels=bin_names,         # bin 이름
                      include_lowest=True)      # 첫 경계값 포함

# horsepower 열, hp_bin 열의 첫 15행을 출력
print(df[['horsepower', 'hp_bin']].head(15))

# hp_bin 열의 범주형 데이터를 더미 변수로 변환 (one-hot-encoding) - 원-핫-벡터
horsepower_dummies = pd.get_dummies(df['hp_bin'])
print(horsepower_dummies.head(15))