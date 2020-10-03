# LSTM을 이용한 로이터 뉴스 카테고리 분류
import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM, Embedding
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras.datasets import reuters

# 불러온 데이터를 학습셋, 테스트셋으로 나누기(빈도수가 1~1000 사이)
(X_train, Y_train), (X_test, Y_test) = reuters.load_data(num_words=1000, test_split=0.2)

# 데이터 확인 후에 출력
category = np.max(Y_train) + 1
print(category, '카테고리')
print(len(X_train), '학습용 뉴스 기사')
print(len(X_test), '테스트용 뉴스 기사')
print(X_train[0])           # 해당 단어가 몇번 나타나는지 세어 빈도에 따라 번호가 나타남
print(len(X_train[0]))      # 단어 갯수

# 데이터 전처리(단어수를 100개에 맞춘다)
x_train = sequence.pad_sequences(X_train, maxlen=100)
x_test = sequence.pad_sequences(X_test, maxlen=100)
print(x_train[0])           # 모자라는 부분은 0으로 채움

y_train = to_categorical(Y_train)
y_test = to_categorical(Y_test)

# LSTM 모델 설정하기
model = Sequential()
model.add(Embedding(1000, 100))
model.add(LSTM(100, activation='tanh'))
model.add(Dense(46, activation='softmax'))

# 모델 컴파일
model.compile(loss='categorical_crossentropy',      # 여러개중에 1개를 선택하는 경우
              optimizer='adam',
              metrics=['accuracy'])

# 모델 최적화 설정
MODEL_DIR = './model_lstm/'          # 폴더 설정
if not os.path.exists(MODEL_DIR):
    os.mkdir(MODEL_DIR)

# 모델 저장 조건 설정
modelpath="./model_lstm/{epoch:02d}-{val_loss:.4f}.hdf5"
checkpointer = ModelCheckpoint(filepath=modelpath, monitor='val_loss', verbose=1, save_best_only=True)

# 학습 자동 중단 설정 - 모니터링 대상과 기다릴 횟수 설정
early_stopping_callback = EarlyStopping(monitor='val_loss', patience=10)

# 모델 실행(verbose = 0/1(출력))
hist = model.fit(x_train, y_train, epochs=100, batch_size=100,
                 validation_data=(x_test, y_test), verbose=1, callbacks=[checkpointer, early_stopping_callback])

# 테스트 정확도 출력
print("\n Test Accuracy: %.4f" % (model.evaluate(x_test, y_test)[1]))

# 그래프 그리기
# 테스트 셋의 오차
y_vloss = hist.history['val_loss']

# 학습셋의 오차
y_loss = hist.history['loss']

# 그래프로 표현
x_len = np.arange(len(y_loss))
plt.plot(x_len, y_vloss, marker='.', c="red", label='Testset_loss')
plt.plot(x_len, y_loss, marker='.', c="blue", label='Trainset_loss')

# 그래프에 그리드를 주고 레이블을 표시
plt.legend(loc='upper right')
# plt.axis([0, 20, 0, 0.35])
plt.grid()
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()                      # 그래프 출력