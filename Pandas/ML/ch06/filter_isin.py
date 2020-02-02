# isin() : 특정 값을 가진 행들을 따로 추출
import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')

# IPyhton 디스플레이 설정 변경 - 출력할 최대 열의 개수
pd.set_option('display.max_columns', 10)

# 함께 탑승한 형제 또는 배우자의 수가 3, 4, 5인 승객만 따로 추출 - 불린 인덱싱
mask1 = titanic['sibsp'] == 3
mask2 = titanic['sibsp'] == 4
mask3 = titanic['sibsp'] == 5

df = titanic[mask1|mask2|mask3]
print(df.head())

# isin() 사용하기
isin_filter = titanic['sibsp'].isin([3,4,5])
df2 = titanic[isin_filter]
print(df2.head())