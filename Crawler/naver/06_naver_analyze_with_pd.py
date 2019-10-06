#판다스를 이용해서 데이터 분석하기
import pandas as pd

df = pd.read_json("./gangname.json")
print(df.count())

dfSum = df.groupby("bloggername").count()
print(dfSum)

# bloggernames = df['bloggername'].groupby()
# print(bloggernames)