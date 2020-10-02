# MNIST 손글씨 인식(데이터 전처리)
from tensorflow.keras.datasets import mnist

# MNIST데이터셋 불러오기
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

# 내용 확인하기
print("학습셋 이미지 수 : %d 개" % (X_train.shape[0]))
print("테스트셋 이미지 수 : %d 개" % (X_test.shape[0]))

# 그래프로 확인
import matplotlib.pyplot as plt
plt.imshow(X_train[0], cmap='Greys')
plt.show()

# 코드로 확인
import sys
for x in X_train[0]:                    # 28 X 28 데이터
    for i in x:
        sys.stdout.write('%d\t' % i)    # 0 ~ 255 사이의 숫자
    sys.stdout.write('\n')

# 차원 변환 과정 (reshape(샘플수, 1차원 속성 수) -> reshape(6000, 784))
X_train = X_train.reshape(X_train.shape[0], 784)
X_train = X_train.astype('float64')
X_train = X_train / 255                 # 0~1 사이의 값으로 변환(정규화)

X_test = X_test.reshape(X_test.shape[0], 784).astype('float64') / 255

# 클래스 값 확인
print("class : %d " % (Y_train[0]))

# 원-핫 인코딩 형태로 변환하기
from tensorflow.keras.utils import to_categorical
Y_train = to_categorical(Y_train, 10)
Y_test = to_categorical(Y_test, 10)
print(Y_train[0])
print(Y_test[0])
