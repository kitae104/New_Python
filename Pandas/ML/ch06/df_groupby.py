# 그룹 연산은 데이터를 집계, 변환, 필터링하는데 효율적
# 1단계 - 분할(split)
# 2단계 - 적용(apply)
# 3단계 - 결합(combine)
import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex', 'class', 'fare', 'survived']]

print('승객수 :', len(df))
print(df.head(), '\n')

# class 열을 기준으로 분할
grouped = df.groupby(['class'])
print(grouped)

# 그룹 객체를 iteration으로 출력: head() 메소드로 첫 5행만을 출력
for key, group in grouped:
    print('key :', key)
    print('number :', len(group))
    print(group.head())
    print('\n')

# 연산 메소드 적용 - 연산이 가능한 열에 대해서만 선택적으로 적용
average = grouped.mean()
print(average, '\n')

# 개별 그룹 선택하기
group3 = grouped.get_group('Third')
print(group3.head())

# 여러 열을 기준으로 그룹화
# class 열, sex 열을 기준으로 분할
grouped2 = df.groupby(['class', 'sex']) # 모든 조합으로 key 생성

# grouped2 그룹 객체를 iteration으로 출력
for key, group in grouped2:
    print('key :', key)     # 2중 멀티 인덱스
    print('number :', len(group))
    print(group.head())
    print('\n')

# grouped2 그룹 객체에 연산 메소드 적용
average2 = grouped2.mean()
print(average2, '\n')

# grouped2 그룹 객체에서 개별 그룹 선택하기
group3f = grouped2.get_group(('Third', 'female'))
print(group3f.head(), '\n')

