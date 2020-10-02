# 보스턴 집값 예측
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split

# seed 값 설정
seed = 0
np.random.seed(seed)
tf.random.set_seed(3)

# CSV 읽어 오기(공백 제거, 헤더 없는 경우)
df = pd.read_csv('./dataset/housing.csv', delim_whitespace=True, header=None)
# 데이터 정보 확인
print(df.info())        # 506 X 14 (13개의 속성과 1개의 클래스로 구성)

# 데이터 처리
dataset = df.values
X = dataset[:,0:13]
Y = dataset[:,13]

# 데이터 분리
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=seed)

# 모델 설정
model = Sequential()
model.add(Dense(30,  input_dim=13, activation='relu'))  # 13개 입력 -> 30개 출력
model.add(Dense(6, activation='relu'))                  # 30개 입력 -> 6개 출력
model.add(Dense(1))                                     # 6개 입력 -> 1개 출력
model.summary()

#모델 컴파일
model.compile(loss='mean_squared_error',
              optimizer='adam')

# 모델 실행(verbose = 0/1)
model.fit(X_train, Y_train, epochs=200, batch_size=10)

# 예측 값과 실제 값의 비교
Y_prediction = model.predict(X_test).flatten()
for i in range(10):
    label = Y_test[i]
    prediction = Y_prediction[i]
    print("실제가격: {:.3f}, 예상가격: {:.3f}".format(label, prediction))