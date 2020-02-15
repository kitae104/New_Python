# 미니 배치 - 훈련 데이터에서 지정한 수의 데이터를 무작위로 뽑아내기
import numpy as np
from DeepLearningFromScratch.dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=True)

print(x_train.shape)
print(t_train.shape)

train_size = x_train.shape[0]
print(train_size)
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)   # 무작위로 batch_size 만큼 추출
print(batch_mask)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]


