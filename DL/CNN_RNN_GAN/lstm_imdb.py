# LSTM을 이용한 영화 리뷰 분류하기
import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.layers import LSTM, Embedding
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Conv1D, MaxPooling1D
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras.datasets import imdb

# 불러온 데이터를 학습셋, 테스트셋으로 나누기(빈도수가 1~1000 사이)
(X_train, Y_train), (X_test, Y_test) = imdb.load_data(num_words=5000)

# 데이터 확인 후에 출력
category = np.max(Y_train) + 1
print(category, '카테고리')                 # 카테고리 갯수
print(len(X_train), '학습용 데이터')
print(len(X_test), '테스트용 데이터')
print(X_train[0])           # 해당 단어가 몇번 나타나는지 세어 빈도에 따라 번호가 나타남
print(len(X_train[0]))      # 단어 갯수

# 데이터 전처리(단어수를 100개에 맞춘다)
x_train = sequence.pad_sequences(X_train, maxlen=100)
x_test = sequence.pad_sequences(X_test, maxlen=100)
print(x_train[0])           # 모자라는 부분은 0으로 채움

# 클래스가 2개인 경우 원-핫-인코딩은 하지 않음
# y_train = to_categorical(Y_train)
# y_test = to_categorical(Y_test)

# LSTM 모델 설정하기
model = Sequential()
model.add(Embedding(5000, 100))
model.add(Dropout(0.5))
model.add(Conv1D(64, 5, padding='valid', activation='relu', strides=1))
model.add(MaxPooling1D(pool_size=4))
model.add(LSTM(55))
model.add(Dense(1))
model.add(Activation('sigmoid'))
model.summary()

# 모델 컴파일
model.compile(loss='binary_crossentropy',      # 여러개중에 1개를 선택하는 경우
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
hist = model.fit(x_train, Y_train, epochs=100, batch_size=100,
                 validation_data=(x_test, Y_test), verbose=1, callbacks=[checkpointer, early_stopping_callback])

# 테스트 정확도 출력
print("\n Test Accuracy: %.4f" % (model.evaluate(x_test, Y_test)[1]))

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