# 미니 배치 학습 구현하기
import numpy as np
import matplotlib.pyplot as plt
from DeepLearningFromScratch.dataset.mnist import load_mnist
from DeepLearningFromScratch.ch04.two_layer_nets import TwoLayerNet

if __name__ == "__main__":
    # flatten=True : 이미지를 1차원 배열로 평탄하게 만들지 결정 True : 784, False : 1 X 28 X 28 (3차원)
    # normalize=False : 0.0~1.0 사이의 값으로 정규화할지를 결정(False 일 경우 원래값 그대로 0~255사이값 유지)
    # one_hot_label(원-핫 인코딩) : 정답원소만 1이고 나머지는 0으로 처리 [0,0,1,0,0,0,0,0,0,0]
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=False, one_hot_label=True)

    train_loss_list = []
    train_acc_list = []
    test_acc_list = []

    # 하이퍼파라미터
    iters_num = 10000               #반복횟수
    train_size = x_train.shape[0]
    batch_size = 100                # 미니배치 크기
    learning_rate = 0.1             # 학습률

    # 1에폭당 반복 수
    iter_per_epoch = max(train_size / batch_size, 1)

    network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

    for i in range(iters_num):
        # 미니배치 획득
        batch_mask = np.random.choice(train_size, batch_size)   # train_size 범위에서 batch_size 만큼 추출
        x_batch = x_train[batch_mask]       # batch_mask 위치의 학습 데이터를 100개 추출
        t_batch = t_train[batch_mask]       # batch_mask 위치의 정답 레이블을 100개 추출

        # 기울기 계산
        grad = network.numerical_gradient(x_batch, t_batch)
        # grad = network.gradient(x_batch, t_batch) # 성능 개선판

        # 매개변수 갱신
        for key in ("W1", "b1", "W2", "b2"):
            network.params[key] -= learning_rate * grad[key]

        # 학습 경과 기록
        loss = network.loss(x_batch, t_batch)
        train_loss_list.append(loss)

        # 1에폭당 정확도 계산
        if i % iter_per_epoch == 0:
            train_acc = network.accuracy(x_train, t_train)
            test_acc = network.accuracy(x_test, t_test)
            train_acc_list.append(train_acc)
            test_acc_list.append(test_acc)
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
