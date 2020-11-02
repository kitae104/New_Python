import pandas as pd

file_path = '../data/chipotle.tsv'
chipo = pd.read_csv(file_path, sep='\t')
print(chipo.head())
print(chipo.shape)
print(chipo.info())     # 행의 구성정보와 열의 구성정보
print(chipo.describe())
