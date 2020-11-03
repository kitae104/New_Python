import pandas as pd

file_path = '../data/chipotle.tsv'
chipo = pd.read_csv(file_path, sep='\t')

# 컬럼과 데이터 타입 정보 확인하기
#print(chipo.info())

#print(chipo.index)
print(chipo.describe())

print(chipo['order_id'].unique())
