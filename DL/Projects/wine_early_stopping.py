# 와인 종류 예측(그래프로 확인하기)
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
import os

# seed 값 설정
seed = 3
np.random.seed(seed)
tf.random.set_seed(3)

# 데이터 입력
df_pre = pd.read_csv('./dataset/wine.csv', header=None)
df = df_pre.sample(frac=0.15)      # 전체 데이터 다 가져오기 (0.15 면 15%)
# print(df.head())            # 데이터 형태 5 rows x 13 columns
# print(df.info())            # 전체 정보 출력 12개의 정보를 가지고 클래스 맞추기

# 데이터 분리
dataset = df.values
X = dataset[:,0:12]
Y = dataset[:,12]

# 모델 설정
model = Sequential()
model.add(Dense(30,  input_dim=12, activation='relu'))  # 12개 입력 -> 30개 출력
model.add(Dense(12, activation='relu'))                 # 30개 입력 -> 12개 출력
model.add(Dense(8, activation='relu'))                  # 12개 입력 -> 8개 출력
model.add(Dense(1, activation='sigmoid'))               # 8개 입력 -> 1개 출력

#모델 컴파일
model.compile(loss='binary_crossentropy',
           optimizer='adam',
           metrics=['accuracy'])

# 모델 저장 폴더 설정
MODEL_DIR = './model/'          # 폴더 설정
if not os.path.exists(MODEL_DIR):
    os.mkdir(MODEL_DIR)

# 모델 저장 조건 설정
modelpath="./model/{epoch:02d}-{val_loss:.4f}.hdf5"
checkpointer = ModelCheckpoint(filepath=modelpath, monitor='val_loss', verbose=0, save_best_only=True)

# 학습 자동 중단 설정 - 모니터링 대상과 기다릴 횟수 설정
early_stopping_callback = EarlyStopping(monitor='val_loss', patience=100)

# 모델 실행(verbose = 0/1)
hist = model.fit(X, Y, validation_split=0.2, epochs=3500, batch_size=500,
                 verbose=0, callbacks=[early_stopping_callback, checkpointer])

# y_vloss에 테스트셋으로 실험 결과의 오차 값을 저장
y_vloss = hist.history['val_loss']

# y_acc 에 학습 셋으로 측정한 정확도의 값을 저장
y_acc = hist.history['accuracy']

# x값을 지정하고 정확도를 파란색으로, 오차를 빨간색으로 표시
x_len = np.arange(len(y_acc))
plt.plot(x_len, y_vloss, "o", c="red", markersize=3)
plt.plot(x_len, y_acc, "o", c="blue", markersize=3)

plt.show()

# 결과 출력
print("\n Accuracy: %.4f" % (model.evaluate(X, Y)[1]))