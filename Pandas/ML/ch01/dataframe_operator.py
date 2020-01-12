# 데이터프레임 연산
import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.head())        #첫 5행만 표시
print(type(df))

addition = df + 10
print(addition.head())

# 데이터프레임 연산
addition = df + 10
print(addition.tail())

substraction = addition - df
print(substraction.tail())
