import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../../data/auto-mpg.csv', header=None)

# 열이름 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 산점도 그리기
# df.plot(x='weight', y='mpg', kind='scatter')

# 열을 선택하여 박스 플롯 그리기
df[['mpg','cylinders']].plot(kind='box')

plt.show()