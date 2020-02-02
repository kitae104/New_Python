# 열 순서 변경
import seaborn as sns

# titanic 데이터셋의 부분을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[0:4, 'survived':'age']     # 4포함. age 포함
print(df)

# 열 이름의 리스트 만들기
columns = list(df.columns.values)   #기존 열 이름
print(columns)

# 열 이름을 알파벳 순으로 정렬하기
columns_sorted = sorted(columns)    # 정렬하기
df_sorted = df[columns_sorted]      # 새로운 컬럼으로 데이터프레임 설정
print(df_sorted)

# 열 이름을 기존 순서의 정반대 역순으로 정렬하기
columns_reversed = list(reversed(columns))  # 기존 순서에 대한 역순(역정렬 아님)
print(columns_reversed)
df_reversed = df[columns_reversed]
print(df_reversed)

# 열 이름을 사용자가 정의한 임의의 순서로 재배치하기
columns_customed = ['pclass', 'sex', 'age', 'survived']
df_customed = df[columns_customed]
print(df_customed)