# SimpleConvNet으로 학습하기
import numpy as np
import matplotlib.pyplot as plt
from DeepLearningFromScratch.dataset.mnist import load_mnist
from DeepLearningFromScratch.ch07_CNN.simple_convnet import SimpleConvNet
from DeepLearningFromScratch.common.trainer import Trainer2

# 데이터 읽기 - CNN에서는 평탄화 수행하지 않음
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=False)


# 처음엔 데이터를 줄여 정상 동작 여부를 확인한다.
# x_train, t_train = x_train[:5000], t_train[:5000]
# x_test, t_test = x_test[:1000], t_test[:1000]

max_epochs = 20     # 전체 데이터에 대해 20회 수행

# 신경망 구성
network = SimpleConvNet(input_dim=(1, 28, 28),              # 입력 데이터의 차수
                        conv_param={'filter_num':30, 'filter_size':5, 'pad':0, 'stride':1}, # 합성곱 계층의 파라미터
                        hidden_size=100, output_size=10, weight_init_std=0.01)  # 은닉층, 출력 크기, 가중치 표준편차

trainer = Trainer2(network, x_train, t_train, x_test, t_test,
                  epochs=max_epochs, mini_batch_size=100,
                   optimizer='Adam', optimizer_param={'lr':0.001},
                   evaluate_sample_num_per_epoch=1000)

trainer.train()     # 학습 수행

# 매개변수 보준
network.save_params("params.pkl")
print("Saved Network Parameters!")

# 그래프 그리기
markers = {'train':'o', 'test':'s'}
x = np.arange(max_epochs)   # 수행 횟수
plt.plot(x, trainer.train_acc_list, marker='o', label='train', markevery=2)
plt.plot(x, trainer.test_acc_list, marker='s', label='test', markevery=2)

plt.xlabel("epochs")
plt.ylabel("accuracy")
plt.ylim(0, 1.0)
plt.legend(loc='lower right')

plt.show()