import seaborn as sns

# titanic 데이터셋 가져오기
df = sns.load_dataset('titanic')

# deck 열의 NaN 개수 계산하기
nan_deck = df['deck'].value_counts(dropna=False)
print(nan_deck)

# isnull() 메서드로 누락 데이터 찾기
print(df.head().isnull())

# notnull() 메서드로 누락 데이터 찾기 - 반대
print(df.head().notnull())

# isnull() 메서드로 누락 데이터 개수 구하기
print(df.head().isnull().sum(axis=0))

# for 반복문으로 각 열의 NaN 개수 계산하기
missing_df = df.isnull()

for col in missing_df.columns:
    missing_count = missing_df[col].value_counts()   # 각 열의 NaN 개수 파악

    try:
        print(col, ' : ', missing_count[True])  # NaN 값이 있으면 개수를 출력
    except:
        print(col, ' : ', 0)

# NaN 값이 500개 이상인 열을 모두 삭제 - deck 열(891개 중 688개의 NaN 값)
df_thresh = df.dropna(axis=1, thresh=500)
print(len(df.columns))
print(len(df_thresh.columns))

# age 열에 나이 데이터가 없는 모든 행을 삭제 - age 열(891개 중 177개의 NaN 값)
df_age = df.dropna(subset=['age'], how='any', axis=0) # any 하나라도 NaN이 존재하면 삭제
print(len(df_age))

# 누락 데이터 치환
print(df['age'].head(10))

# age 열의 NaN값을 다른 나이 데이터의 평균으로 변경하기
mean_age = df['age'].mean(axis=0)   # age 열의 평균 계산 (NaN 값 제외)
print(mean_age)
df['age'].fillna(mean_age, inplace=True)

print(df['age'].head(10))