# 초음파 광물 예측하기

# 필요한 라이브러리 추가
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# seed 값 설정
np.random.seed(3)
tf.random.set_seed(3)

df = pd.read_csv("./dataset/sonar.csv", header=None)    # CSV형태의 파일 읽어 오기, 헤더는 없음
#print(df.head())        # 내용 확인  --> 전체 구조 208 rows x 61 columns
#print(df.info())        # 파일에 대한 정보 출력 - null 값은 없는 상태 (60개의 속성과 1개의 클래스)

# 데이터 분리
dataset = df.values
X = dataset[:, 0:60].astype(float)
Y_class = dataset[:, 60]

# 문자열 변환
e = LabelEncoder()
e.fit(Y_class)
Y = e.transform(Y_class)
# print(Y_class)
# print(Y)

# 모델 설정
model = Sequential()
model.add(Dense(24,  input_dim=60, activation='relu'))  # 60개의 입력 -> 24개 출력
model.add(Dense(10, activation='relu'))                 # 24개 입력 -> 10개 출력
model.add(Dense(1, activation='sigmoid'))               # 10개 입력 -> 1개 출력 (sigmoid 사용)

# 모델 컴파일
model.compile(loss='mean_squared_error',                # 카테고리 이용
            optimizer='adam',                           # Adam
            metrics=['accuracy'])                       # 정확도 측정

# 모델 실행 -> 반드시 컴파일 과정을 먼저 수행해야 한다.
model.fit(X, Y, epochs=200, batch_size=5)        # 학습

# 결과 출력
print("\n Accuracy: %.4f" % (model.evaluate(X, Y)[1]))  # 평가