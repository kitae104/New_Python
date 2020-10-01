# 와인 종류 예측(모델 업데이트)
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import ModelCheckpoint
import os

# seed 값 설정
seed = 0
np.random.seed(seed)
tf.random.set_seed(3)

# 데이터 입력
df_pre = pd.read_csv('./dataset/wine.csv', header=None)
df = df_pre.sample(frac=1)      # 전체 데이터 다 가져오기 (0.5 면 50%)
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
checkpointer = ModelCheckpoint(filepath=modelpath, monitor='val_loss', verbose=1, save_best_only=True)

# 모델 실행(verbose = 0/1)
model.fit(X, Y, validation_split=0.2, epochs=200, batch_size=200, verbose=1, callbacks=[checkpointer])

# 결과 출력
print("\n Accuracy: %.4f" % (model.evaluate(X, Y)[1]))