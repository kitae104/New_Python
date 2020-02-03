# pipe() : 데이터프레임 객체를 함수에 매핑할 때 사용
# 리턴값에 따라 데이터프레임, 시리즈, 개별 값을 각각 반환한다.
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]

# 각 열의 NaN 찾기 - 데이터프레임 전달하면 데이터프레임을 반환
def missing_value(x):
    return x.isnull()   # 불린 형태로 반환

# 각 열의 NaN 개수 반환 - 데이터프레임 전달하면 시리즈 반환
def missing_count(x):
    return missing_value(x).sum()   # 각 열의 누락 데이터 갯수

# 데이터프레임의 총 NaN 개수 - 데이터프레임 전달하면 값을 반환
def total_number_missing(x):
    return missing_count(x).sum()   # 각 열의 누락 데이터 갯수 합산

# 데이터프레임에 pipe() 메소드로 함수 매핑
res_df = df.pipe(missing_value)
print(res_df.head())

res_sr = df.pipe(missing_count)
print(res_sr)

res_val = df.pipe(total_number_missing)
print(res_val)