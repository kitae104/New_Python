# 데이터 살펴보기
import pandas as pd

df = pd.read_csv("../../data/auto-mpg.csv", header=None)

# 컬럼 이름 설정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
print(df.head())    # 시작 부분 5개 확인
print()
print(df.tail())    # 마지막 부분 5개 확인

# df의 모양과 크기 확인: (행의 개수, 열의 개수)를 투플로 반환
print(df.shape)

# 데이터프레임 df의 내용 확인
print(df.info())

# 데이터프레임 df의 자료형 확인
print(df.dtypes)

# 시리즈(mpg 열)의 자료형 확인
print("mpg type : ", df.mpg.dtypes) # 개별 타입

# 데이터프레임 df의 기술통계 정보 확인
print(df.describe())
print(df.describe(include='all'))

# 데이터프레임 df의 각 열이 가지고 있는 원소 개수 확인
print(df.count())

# df.count()가 반환하는 객체 타입 출력
print(type(df.count()))

# 데이터프레임 df의 특정 열이 가지고 있는 고유값 확인
unique_values = df['origin'].value_counts()
print(unique_values)

# value_counts
print(type(unique_values))

# 평균값
print(df.mean())
print(df['mpg'].mean())
print(df.mpg.mean())
print(df[['mpg', 'weight']].mean())

# 중간값
print(df.median())
print(df['mpg'].median())
print(df.mpg.median())

# 최대값
print(df.max())
print(df['mpg'].max())
print(df.mpg.max())

# 최소값
print(df.min())
print(df['mpg'].min())
print(df.mpg.min())

# 표준 편차
print(df.std())
print(df['mpg'].std())
print(df.mpg.std())

# 상관 계수
print(df.corr())
print(df[['mpg', 'weight']].corr())