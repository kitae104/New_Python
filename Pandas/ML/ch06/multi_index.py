# 멀티 인덱스
import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex', 'class', 'fare', 'survived']]

# class 열, sex 열을 기준으로 분할
grouped = df.groupby(['class', 'sex'])

# 그룹 객체에 연산 메서드 적용
gdf = grouped.mean()
print(gdf, '\n')      # 그룹별로 결과를 보여줌

# class 값이 First인 행을 선택하여 출력
print(gdf.loc['First'], '\n')

# class 값이 First이고, sex 값이 female인 행을 선택하여 출력
print(gdf.loc['First', 'female'], '\n')

# sex 값이 male인 행을 선택하여 출력
print(gdf.xs('male', level='sex'))