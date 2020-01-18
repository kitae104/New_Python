# 웹에서 표 정보 읽기
import pandas as pd

url = "../../data/sample.html"
tables = pd.read_html(url)

print(len(tables))

for i in range(len(tables)):
    print("tables[%s]" % i)
    print(tables[i])
    print("\n")

df = tables[1]
df.set_index(['name'], inplace=True) # name 열을 인덱스로 설정
print(df)