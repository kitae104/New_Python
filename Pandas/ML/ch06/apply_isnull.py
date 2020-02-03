# 데이터프레임의 각 열에 함수 매핑 - apply(axis=0) 적용
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
df['ten'] = 10
print(df.head())

# 사용자 함수 정의
def missing_value(series):  # 시리즈를 인자로 전달
    return series.isnull()  # 불린 시리즈 반환

# 데이터프레임의 각 열을 인수로 전달하면 데이터프레임을 반환
res = df.apply(missing_value, axis=0)
print(res.head())
print("-"*50)

def min_max(x):
    return x.max() - x.min()

# 데이터프레임의 각 열을 인수로 전달하면 시리즈를 반환
res = df.apply(min_max, axis=0)     # 각 열에 대해 처리
print(res.head())
print("-"*50)
# 데이터프레임의 각 행에 함수 매핑 - apply(axis=1) 적용
def add_obj(a, b):
    return a + b

df['add'] = df.apply(lambda x : add_obj(x['age'], x['ten']), axis=1)
print(df.head())

print("-"*50)
df['add2'] = add_obj(df['age'], df['ten'])
print(df.head())