import pandas as pd

# DataFrame
df = pd.read_csv('../data/data_01.csv')
print(df)
print('-'*50)

print(df.columns)
print(df.index)
print(df.shape)
print('-'*50)

print(type(df))
print(type(df.Name))
print('-'*50)

# Job열 데이터 추출하기
df_job = df['Job']
print(df_job)

# 2개 이상의 데이터열 추출 하기
df_contry_job = df[['Country', 'Job']]
print(df_contry_job)

# 행 추출하기
df_1st_row = df.loc[0]
print(df_1st_row)

# 2개 이상의 행 추출 - 리스트 이용
df_1st_4st_row = df.loc[[0 , 3]]
print(df_1st_4st_row)

# 그룹핑
df_country_group = df.groupby('Country')
# 그룹핑 후 특정 필드의 평균 구하기
age_avg = df_country_group['Age'].mean()

print('나라별 나이 평균 :', age_avg)

df.columns = ['이름', '국가', '나이', '직업']
df.index = ['일', '이', '삼', '사', '오', '육', '칠']
print(df)
print('-'*50)