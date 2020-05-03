# 101에서 110까지 구하기
## 0. 관련 모듈 불러오기
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

## 1. 데이터 준비
#### 데이터와 정답(학습과 테스트)
x_train = np.array([1,2,3,4,5,6,7,8,9,10])
y_train = np.array([1,2,3,4,5,6,7,8,9,10])
x_test = np.array([101,102,103,104,105,106,107,108,109,110])
y_test = np.array([101,102,103,104,105,106,107,108,109,110])

## 2. 모델 구성
#### 모델 생성
# * 얼마나 많은 레이어와 노드를 준비할 것인가 설계
# * Dense(5, input_dim=1) : 1개의 입력으로 5개의 노드로 출력한다는 의미
model = Sequential()
#model.add(Dense(5, input_dim=1, activation='relu'))
model.add(Dense(5, input_dim=1))
model.add(Dense(3))
#model.add(Dense(1, activation='relu'))
model.add(Dense(1))
model.summary()

## 3. 컴파일 및 훈련
#### 모델 컴파일
# * 모델을 실행시키지 전에 머신이 이해할 수 있도록 컴파일 시킴
model.compile(optimizer='adam',loss='mse', metrics=['accuracy'])

#### 모델 실행
hist = model.fit(x_train, y_train, epochs=100, batch_size=1,validation_data = (x_test, y_test))

#### 그래프 확인
import matplotlib.pyplot as plt

plt.plot(hist.history['loss'])
plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_loss'])
plt.plot(hist.history['val_accuracy'])
#plt.ylim(0.0, 1.5)
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['loss', 'accuracy', 'val_loss', 'val_accuracy'], loc='upper right')
plt.show()

## 4. 평가 및 예측
#### 모델 평가

loss, acc = model.evaluate(x_test, y_test, batch_size=1)
print("loss :", loss)
print("acc :", acc)

#### 예측하기
output = model.predict(x_test)
print("결과물 : \n", output)
