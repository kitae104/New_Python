# MNIST 훈련 데이터에서 지정된 수의 데이터를 무작위로 추출하기
import sys, os
sys.path.append(os.pardir)     #부모 디렉토리의 파일을 가져올 수 있도록 설정
from DeepLearningFromScratch.dataset.mnist import load_mnist
import DeepLearningFromScratch.libs.neural_lib as lib
import numpy as np

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=True, one_hot_label=True)

print(x_train.shape)    # (60000, 784)
print(t_train.shape)    # (60000, 10)

# 훈련 데이터에서 무작위로 10장 뽑아오기
train_size = x_train.shape[0]   # 60000
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)   # 임의의 위치 출력
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]

# res = lib.cross_entropy_error(np.array(x_batch), np.array(t_batch))
# print(res)
