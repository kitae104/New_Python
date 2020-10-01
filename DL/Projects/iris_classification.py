# 아이리스 품종 예측
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 데이터 입력(CSV 읽기)
df = pd.read_csv('./dataset/iris.csv', names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"])
print(df.head())

# 그래프로 확인 - 전체 그래프로 확인 하기
sns.pairplot(df, hue='species');
plt.show()

# 데이터 분류 (X, Y로 분리)
dataset = df.values
X = dataset[:, 0:4].astype(float)
Y_obj = dataset[:, 4]                   # 문자로 된 형태

# 문자열을 숫자로 변환
e = LabelEncoder()                      # 라벨을 숫자로  A, B, C
e.fit(Y_obj)
Y = e.transform(Y_obj)                  # 숫자 형태로 변환 0, 1, 2
Y_encoded = to_categorical(Y)
print(Y_encoded)                        # 원-핫-인코딩 형태로 변환 [0 0 1]

# 모델의 설정
model = Sequential()
model.add(Dense(16,  input_dim=4, activation='relu'))   # 4개 입력 16개 출력
model.add(Dense(3, activation='softmax'))               # 16개 입력 3개 출력 (softmax 확률 사용)
model.summary()

# 모델 컴파일
model.compile(loss='categorical_crossentropy',          # 카테고리 이용
            optimizer='adam',                           # Adam
            metrics=['accuracy'])                       # 정확도 측정

# 모델 실행
model.fit(X, Y_encoded, epochs=50, batch_size=1)        # 학습

# 결과 출력
print("\n Accuracy: %.4f" % (model.evaluate(X, Y_encoded)[1]))  # 평가
