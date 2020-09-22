import pandas as pd

df = pd.read_csv('data.csv', encoding="MS949")
print(df)
df[::2].to_csv('even.csv')
df[1::2].to_csv('odd.csv')

kor_sum = df['국어'].sum()
print("국어 : ", kor_sum)

mem1 = df.loc[0][1:].sum()
print("ID1 :", mem1)

sum1 = df.sum(axis=0)
print("sum1:", sum1)

sum2 = df.sum(axis=1)
print("sum2:", sum2)


import matplotlib.pyplot as plt
plt.bar(df.ID, df['국어'])
plt.show()