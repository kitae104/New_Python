# 오차역전파법을 사용한 학습 구현
import numpy as np
import matplotlib.pyplot as plt

from DeepLearningFromScratch.dataset.mnist import load_mnist
from DeepLearningFromScratch.libs.two_layer_net import TwoLayerNet

# 데이터 읽기
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

# 신경망 구성하기
network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

# 하이퍼 파라미터
iters_num = 10000               #  반복 횟수
train_size = x_train.shape[0]   # 학습 사이즈
batch_size = 100                # 배치 사이즈
learning_rate = 0.1             # 학습률

# 학습 정보를 저장할 리스트
train_loss_list = []    # 비용 리스트
train_acc_list = []     # 학습 정확도 리스트
test_acc_list = []      # 테스트 정확도 리스트

# 반복 횟수(에폭)
iter_per_epoch = max(train_size / batch_size, 1)

for i in range(iters_num):
    batch_mask = np.random.choice(train_size, batch_size)   # 미니배치를 위해 임의의 값 선택
    x_batch = x_train[batch_mask]       # 입력 배치
    t_batch = t_train[batch_mask]       # 정답 배치

    # 오차역전파법으로 기울기 계산
    grad = network.gradient(x_batch, t_batch)   # 기울기

    # 갱신
    # 매개변수 갱신
    for key in ("W1", "b1", "W2", "b2"):    # 기울기 내부 항목
        network.params[key] -= learning_rate * grad[key]    # 갱신 수행

    # 학습 경과 기록
    loss = network.loss(x_batch, t_batch)   # 비용
    train_loss_list.append(loss)            # 비용 리스트

    # 1에폭당 정확도 계산
    if i % iter_per_epoch == 0:
        train_acc = network.accuracy(x_train, t_train)  # 학습 정확도
        test_acc = network.accuracy(x_test, t_test)     # 테스트 정확도
        train_acc_list.append(train_acc)                # 학습 정확도 리스트
        test_acc_list.append(test_acc)                  # 테스트 정확도 리스트
        print("train acc, test acc | " + str(train_acc) + ", " + str(test_acc))

# 그래프 그리기
markers = {'train': 'o', 'test': 's'}
x = np.arange(len(train_acc_list))
plt.plot(x, train_acc_list, label='train acc')
plt.plot(x, test_acc_list, label='test acc', linestyle='--')
plt.xlabel("epochs")
plt.ylabel("accuracy")
plt.ylim(0, 1.0)
plt.legend(loc='lower right')
plt.show()
