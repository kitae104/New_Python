import tensorflow as tf
print(tf.__version__)
import keras
print(keras.__version__)

from keras.datasets import mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
print(train_images.shape)
print(len(train_labels))

# 시각화
import matplotlib.pyplot as plt

d = train_images[4]
#plt.imshow(d, cmap=plt.cm.binary)
#plt.show()

print(train_labels[4])

from keras import models
from keras import layers    # dense
from keras.utils import to_categorical      # one-hot-encoding

# 모델 생성
network = models.Sequential()   # 순서대로 쌓아서 만들어 냄
network.add(layers.Dense(512,  activation='relu', input_shape=(28 * 28,)))  # 첫번째 계층에서 사용될 뉴런의 갯수
network.add(layers.Dense(10,  activation='softmax'))  # 마지막 계층- 10개의 출력

# 학습 정보에 대해 설정 - rmsprop (최소값 찾는 방법) , 측도 = 정확도
network.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=['accuracy'])

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255     # 정규화 수행(normalization) 0~1 사이의 실수값으로 변경

# plt.boxplot(train_images[0:5])
# plt.show()

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255       # 정규화 수행(normalization)

print(train_labels.shape)                               # 숫자 데이터
train_labels = to_categorical(train_labels)             # one-hot-encoding으로 변환
print(train_labels.shape)                               # one-hot 형태
test_labels = to_categorical(test_labels)

# 학습
network.fit(train_images, train_labels, epochs=5, batch_size=128)

# 평가
test_loss, test_acc = network.evaluate(test_images, test_labels)    # 모델에 대한 평가
print('\n')
print('test_acc :', test_acc, ", test_loss :", test_loss)