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
grouped = df.groupby(['class']) # 3개의 클래스로 나누어짐

# 각 그룹에 대한 모든 열의 표준편차를 집계하여 데이터프레임으로 반환
std_all = grouped.std()
print(std_all, '\n')

# 각 그룹에 대한 fare 열의 표준편차를 집계하여 시리즈로 반환
std_fare = grouped.fare.std()
print(std_fare, "\n")

print('-'*50)

# 그룹 객체에 agg() 메소드 적용 - 사용자 정의 함수를 인수로 전달
# 사용자 정의함수를 그룹 객체에 적용
# agg() : 각 그룹별 데이터에 연산을 위한 함수를 구분 적용하고, 그룹별로 연산 결과를 집계하여 반환
def min_max(x):
    return x.max() - x.min()

agg_minmax = grouped.agg(min_max)
print(agg_minmax.head(), '\n')

# 여러 함수를 각 열에 동일하게 적용하여 집계
agg_all = grouped.agg(['min', 'max'])
print(agg_all, '\n')

# 각 열마다 다른 함수를 적용하여 집계
agg_sep = grouped.agg({'fare':['min','max'], 'age':'mean'})
print(agg_sep)

# 그룹 연산 데이터 변환
# transform() : 그룹별로 구분하여 각 원소에 함수를 적용하지만
# 그룹별 집계 대신 각 원소의 본래 행 인덱스와 열 이름을 기준으로 연산 결과를 반환
age_mean = grouped.age.mean()
print(age_mean, '\n')

age_mean2 = grouped.agg({'age':'mean'})
print(age_mean2, '\n')

# 그룹별 age 열의 표준편차 집계 연산
age_std = grouped.age.std()
print(age_std, '\n')

# 그룹 객체의 age 열을 iteration으로 z-score를 계산하여 출력
for key, group in grouped.age:
    group_zscore = (group - age_mean.loc[key]) / age_std.loc[key]
    print('* origin :', key)
    print(group_zscore.head(3))
    print('\n')

# z-score를 계산하는 사용자 함수 정의
def z_score(x):
    return (x - x.mean()) / x.std()

# transform() 메소드를 이용하여 age 열의 데이터를 z-score로 변환
age_zscore = grouped.age.transform(z_score)
print(age_zscore.loc[[1, 9, 0]], '\n')
print(len(age_zscore), '\n')
print(age_zscore.loc[0:9], '\n')

# 그룹 객체 필터링
# filter() : 조건식을 가진 함수를 전달하면 조건이참인 그룹만을 남긴다.
# class 열을 기준으로 분할
grouped2 = df.groupby(['class'])

# 데이터 개수가 200개 이상인 그룹만을 필터링하여 데이터프레임으로 반환
grouped_filter = grouped2.filter(lambda x : len(x) > 200)
print(grouped_filter.head(), '\n')

# age 열의 평균이 30보다 작은 그룹만을 필터링하여 데이터프레임으로 반환
grouped_age = grouped2.filter(lambda x : x.age.mean() < 30)
print(grouped_age.tail(), '\n')

# 그룹 객체에 함수 매핑
# apply()는 객체의 개별 원소를 특정 함수에 일대일로 매핑한다.
# 집계 : 각 그룹별 요약 통계정보를 집계
agg_grouped = grouped2.apply(lambda x : x.describe())
print(agg_grouped, '\n')

# z-score를 계산하는 사용자 함수 정의
# 수집한 개별 데이터에서 그 데이터 집단 전체의 평균을 빼고 표준편차로 나누어줌
def z_score(x):
    return (x - x.mean()) / x.std()

age_zscore2 = grouped2.age.apply(z_score)
print(age_zscore.head(), '\n')

# 필터링 : age 열의 데이터 평균이 30보다 작은 그룹만을 필터링하여 출력
age_filter = grouped2.apply(lambda x : x.age.mean() < 30)
print(age_filter, '\n')

for x in age_filter.index:
    if age_filter[x] == True:
        age_filter_df = grouped2.get_group(x)
        print(age_filter_df.head())
        print('\n')
