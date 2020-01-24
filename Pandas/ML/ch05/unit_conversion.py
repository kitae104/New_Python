# 단위 환산
import pandas as pd
import numpy as np

df = pd.read_csv('../../data/auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

print(df.head())

# mpg(mile per gallon)를 kpl(kilometer per liter)로 변환 (mpg_to_kpl = 0.425)
mpg_to_kpl = 1.60934 / 3.78541

# mpg 열에 0.425를 곱한 결과를 새로운 열(kpl)에 추가(새로운 컬럼 추가)
df['kpl'] = df['mpg'] * mpg_to_kpl
print(df.head())

# kpl 열을 소수점 아래 둘째 자리에서 반올림
df['kpl'] = df['kpl'].round(2)
print(df.head())

# 각 열의 자료형 확인
print(df.dtypes)

# horsepower 열의 고유값 확인
print(df['horsepower'].unique())

df['horsepower'].replace('?', np.nan, inplace=True)         # '?'을 np.nan으로 변경
df.dropna(subset=['horsepower'], axis=0, inplace=True)      # 누락데이터 행을 삭제
df['horsepower'] = df['horsepower'].astype('float')         # 문자열을 실수형으로 변환

# horsepower 열의 자료형 확인
print(df['horsepower'].dtypes)

# origin 열의 고유값 확인
print(df['origin'].unique())

# 정수형 데이터를 문자형 데이터로 변환
df['origin'].replace({1:'USA', 2:'EU', 3:'JAPAN'}, inplace=True)

# origin 열의 고유값과 자료형 확인
print(df['origin'].unique())
print(df['origin'].dtypes)

# origin 열의 문자열 자료형을 범주형으로 변환
df['origin'] = df['origin'].astype('category')
print(df['origin'].dtypes)

# 범주형을 문자열로 다시 변환
df['origin'] = df['origin'].astype('str')
print(df['origin'].dtypes)

# model year 열의 정수형을 범주형으로 변환
print(df['model year'].sample(3))   # 임의의 값 3개 출력
print(df['model year'].dtypes)
df['model year'] = df['model year'].astype('category')
print(df['model year'].dtypes)
print(df['model year'].sample(3))   # 임의의 값 3개 출력