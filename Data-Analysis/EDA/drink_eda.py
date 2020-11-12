import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = '../data/drinks.csv'
drinks = pd.read_csv(file_path) # read_csv 함수로 데이터를 Dataframe 형태로 불러옵니다.
# drinks.info()
# print(drinks.head())
# print(drinks.describe())

# 항목 확인
drinks_column = drinks.columns.tolist()
# print(drinks_column)

# 상관 관계
corr = drinks[['beer_servings', 'wine_servings']].corr(method='pearson')
corr = drinks[drinks_column].corr(method='pearson')
# print(corr)
# print(drinks.isnull().sum())   # null 갯수 체크하기

drinks["continent"] = drinks['continent'].fillna('OT')
# print(drinks.head(5))
# print(drinks["continent"].head(5))

result = drinks.groupby('continent').spirit_servings.agg(['mean', 'min', 'max', 'sum'])
# print(result)

mean = result['mean'].tolist()
# print(mean)

# total_servings 피처를 생성합니다.
drinks['total_servings'] = drinks['beer_servings'] + drinks['wine_servings'] + drinks['spirit_servings']
# print(drinks['total_servings'])

# 술 소비량 대비 알콜 비율 피처를 생성합니다.
drinks['alcohol_rate'] = drinks['total_litres_of_pure_alcohol'] / drinks['total_servings']
drinks['alcohol_rate'] = drinks['alcohol_rate'].fillna(0)

country_with_rank = drinks[['country', 'alcohol_rate']]  # 국가와 알콜률
# print(country_with_rank)
country_with_rank = country_with_rank.sort_values(by=['alcohol_rate'], ascending=0)
# print(country_with_rank.head(16))   # 상위 5개 출력

# 값을 정렬한 후 특정 항목에 대해 리스트를 생성한 후 인덱스를 구하면 순위를 구할 수 있음
country_list = country_with_rank.country.tolist()
print(country_list.index("South Korea"))


kor_rank = country_with_rank.index[country_with_rank["country"] =="South Korea"].tolist()
print(kor_rank)