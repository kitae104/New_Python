import pandas as pd

data = {'A1':[1,2,3], 'A2':[10, 20, 30], 'A3':[100, 200, 300]}

df = pd.DataFrame(data)
print(df)

df.index = ["AAA", "BBB", "CCC"]
df.columns = ["XXX", "YYY", "ZZZ"]
print(df)

df.rename(columns={"XXX":"숫자1", "ZZZ":"숫자3"}, inplace=True)
df.rename(index={"AAA":"행1", "BBB":"행2"}, inplace=True)
print(df)