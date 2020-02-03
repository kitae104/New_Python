# 개별 원소에 함수 매핑하기
# 시리즈 객체에 apply() 메소드를 적용하면 전달하는 매핑 함수에 시리즈의 모든 원소를 하나씩 입력하고 함수의 리턴값을 돌려받는다.
import seaborn as sns

# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]

# 새로운 'ten'열 추가
df['ten'] = 10
print(df.head())

# 사용자 함수 정의
def add_10(n):
    return n + 10

def add_two_obj(a, b):
    return a + b

print(add_10(10))
print(add_two_obj(10, 10))
print(add_two_obj("AB", "CD"))

# 시리즈 객체에 적용
sr1 = df['age'].apply(add_10)
print(sr1.head())

# 시리즈 객체와 숫자에 적용 : 2개의 인수(시리즈 + 숫자)
sr2 = df['age'].apply(add_two_obj, b=10)
print(sr2.head())

# 람다 함수 활용: 시리즈 객체에 적용
sr3 = df['age'].apply(lambda x: add_10(x)) # x=df['age']
print(sr3.head())

# applymap() : 데이터프레임에 개별 원소에 특정 함수를 매핑하기
df_map = df.applymap(add_10)
print(df_map.head())