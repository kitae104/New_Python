import pandas as pd
bank_data = pd.read_csv('./data/bank.csv', sep=';')

# 내용 출력
print(bank_data.head(20))   # 20 rows x 17 columns

# 모양 출력
print(bank_data.shape)  # (4521, 17)

# 정보 출력
print(bank_data.info())

feats = bank_data.drop('y', axis = 1)       # 'y' 컬럼만 제거
print(feats)
target = bank_data['y']
print(target.head())
print(f'Features table has {feats.shape[0]} rows and {feats.shape[1]} columns')
print(f'Target table has {target.shape[0]} rows')

# CSV 파일로 저장하기
feats.to_csv("./data/bank_data_feats.csv")
target.to_csv('./data/bank_data_target.csv', header='y')