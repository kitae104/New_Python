# 초음파 광물 예측하기(k겹 교차 검증)

# 필요한 라이브러리 추가
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import StratifiedKFold
import matplotlib.pyplot as plt

# seed 값 설정
seed = 7
np.random.seed(seed)
tf.random.set_seed(seed)

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

# 10개의 파일로 쪼갬
n_fold = 10
skf = StratifiedKFold(n_splits=n_fold, shuffle=True, random_state=seed)

# 빈 accuracy 배열
accuracy = []

# 모델의 설정, 컴파일, 실행
for train, test in skf.split(X, Y):
    # 모델 설정
    model = Sequential()
    model.add(Dense(24, input_dim=60, activation='relu'))   # 60개의 입력 -> 24개 출력
    model.add(Dense(10, activation='relu'))                 # 24개 입력 -> 10개 출력
    model.add(Dense(1, activation='sigmoid'))               # 10개 입력 -> 1개 출력 (sigmoid 사용)

    # 모델 컴파일
    model.compile(loss='mean_squared_error',                # 카테고리 이용
            optimizer='adam',                               # Adam
            metrics=['accuracy'])                           # 정확도 측정

    # 모델 실행 -> 반드시 컴파일 과정을 먼저 수행해야 한다.
    hist = model.fit(X[train], Y[train], epochs=100, batch_size=5)        # 학습

    # 학습 상태 그래프로 그리기
    #
    plt.plot(hist.history['loss'])
    plt.plot(hist.history['accuracy'])
    #plt.ylim(0.0, 1.5)
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['loss', 'accuracy'], loc='upper right')

    k_acc = "%.4f" % (model.evaluate(X[test], Y[test])[1])
    accuracy.append(k_acc)

# 결과 출력
plt.show()

print("\n %.f fold accuracy:" % n_fold, accuracy)