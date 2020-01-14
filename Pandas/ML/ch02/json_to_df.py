# json 파일 읽기
import pandas as pd

file_path = "../../data/read_json_sample.json"

df1 = pd.read_json(file_path)
print(df1)
print(df1.index)
print(df1.columns)

