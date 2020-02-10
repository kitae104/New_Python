# 피벗 테이블
import pandas as pd
import seaborn as sns

# IPyhton 디스플레이 설정 변경
pd.set_option('display.max_columns', 10)    # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', 20)    # 출력할 열의 너비

# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex', 'class', 'fare', 'survived']]
print(df.head())
print('\n')

# 행, 열, 값, 집계에 사용할 열을 1개씩 지정 - 평균 집계
pdf1 = pd.pivot_table(df,              # 피벗할 데이터프레임
                     index='class',    # 행 위치에 들어갈 열
                     columns='sex',    # 열 위치에 들어갈 열
                     values='age',     # 데이터로 사용할 열
                     aggfunc='mean')   # 데이터 집계 함수

print(pdf1.head(), '\n')

# 값에 적용하는 집계 함수를 2개 이상 지정 가능 - 생존율, 생존자 수 집계
pdf2 = pd.pivot_table(df,
                      index='class',
                      columns='sex',
                      values='survived',
                      aggfunc=['mean', 'sum']
                      )
print(pdf2.head(), '\n')

# 행, 열, 값에 사용할 열을 2개 이상 지정 가능 - 평균 나이, 최대 요금 집계
pdf3 = pd.pivot_table(df,
                      index=['class', 'sex'],
                      columns='survived',
                      values=['age', 'fare'],
                      aggfunc=['mean', 'max'])
pd.set_option('display.max_columns', 10)        # 출력할 열의 개수 한도
print(pdf3.head())
print('\n')

# 행, 열 구조 살펴보기
print(pdf3.index)
print(pdf3.columns)

# xs 인덱서 사용 - 행 선택(default: axis=0)
print(pdf3.xs('First'), '\n')

# 행 인덱스가 ('First', 'female')인 행을 선택
print(pdf3.xs(('First', 'female')), '\n')

# 행 인덱스의 sex 레벨이 male인 행을 선택
print(pdf3.xs('male', level='sex'), '\n')
print('-'*50)
# Second, male인 행을 선택
print(pdf3.xs(('Second', 'male'), level=[0, 'sex']), '\n')

print('-'*50)
# xs 인덱서 사용 - 열 선택(axis=1 설정)
# 열 인덱스가 mean인 데이터를 선택
print(pdf3.xs('mean', axis=1), '\n')

print('='*50)
# 열 인덱스가 ('mean', 'age')인 데이터 선택
print(pdf3.xs(('mean', 'age'), axis=1), '\n')

# survived 레벨이 1인 데이터 선택
print(pdf3.xs(1, level='survived', axis=1), '\n')

# max, fare, survived=0인 데이터 선택
# 반환되는 데이터는 구조받지 못한 승객들 객실 요금 최대값
print(pdf3.xs(('max', 'fare', 0), level=[0, 1, 2], axis=1))