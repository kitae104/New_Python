# 히스토그램
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../datas/auto-mpg.csv', header=None)  # read_csv() 함수로 df 생성
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']   # 열 이름을 지정

# 그래프 관련 설정
plt.style.use('classic')     # 스타일 서식 지정
df['mpg'].plot(kind='hist', bins=10, color='coral', figsize=(10, 5)) # 연비(mpg) 열에 대한 히스토그램 그리기

# 그래프 꾸미기
plt.title('Histogram')
plt.xlabel('mpg')
plt.show()