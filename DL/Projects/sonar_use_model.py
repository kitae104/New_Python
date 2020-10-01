# 초음파 광물 예측하기(모델 저장과 재사용)

# 필요한 라이브러리 추가
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Dense


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

# 학습 셋과 테스트 셋의 구분
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=seed)

# 모델 불러오기
model = load_model('my_sonar.h5')       # 모델을 새로 불러옴

# 결과 출력
print("\n Accuracy: %.4f" % (model.evaluate(X_test, Y_test)[1]))  # 평가