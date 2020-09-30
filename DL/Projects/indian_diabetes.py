# 인디안 당뇨병 예측
import pandas as pd

# csv 파일 불러오기
df = pd.read_csv('./dataset/pima-indians-diabetes.csv')
# 컬럼 이름 추가하기
df.columns = ["pregnant", "plasma", "pressure", "thickness", "insulin", "BMI", "pedigree", "age", "class"]
print(df.head(4))
# 데이터 정보 확인
print(df.info())
print(df.describe())
print(df[['pregnant', 'class']])
# 임신 횟수당 당뇨병 발병 확률을 구하기
print(df[['pregnant', 'class']].groupby(['pregnant'], as_index=False).mean().sort_values(by='pregnant', ascending=True))

import matplotlib.pyplot as plt
import seaborn as sns

# 그래프의 크기를 결정
plt.figure(figsize=(12, 12))
# 그래프의 속성을 결정합니다. vmax의 값을 0.5로 지정해 0.5에 가까울 수록 밝은 색으로 표시되게 합니다.
sns.heatmap(df.corr(), linewidths=0.1, vmax=0.5, cmap=plt.cm.gist_heat, linecolor='white', annot=True)
plt.show()

grid = sns.FacetGrid(df, col='class')
grid.map(plt.hist, 'plasma', bins=10)   # 공복 혈당
plt.show()

import numpy as np
import tensorflow as tf

# seed 값 생성
np.random.seed(3)
tf.random.set_seed(3)

# 딥러닝을 구동하는 데 필요한 케라스 함수를 불러옵니다.
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 데이터를 불러 옵니다.
dataset = np.loadtxt("./dataset/pima-indians-diabetes.csv", delimiter=",")
X = dataset[:,0:8]
Y = dataset[:,8]

# 모델을 설정합니다.
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 모델을 컴파일합니다.
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 모델을 실행합니다.
model.fit(X, Y, epochs=200, batch_size=10)

# 결과를 출력합니다.
print("\n Accuracy: %.4f" % (model.evaluate(X, Y)[1]))
