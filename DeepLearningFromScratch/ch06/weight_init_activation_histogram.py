# 은닉층의 활성화 값 분포
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def ReLU(x):
    return np.maximum(0, x)

def tanh(x):
    return np.tanh(x)

input_data = np.random.randn(1000, 100)     # 1000개의 데이터
node_num = 100                              # 각 은닉층의 노드(뉴런) 수
hidden_layer_size = 5                       # 은닉층이 5개
activations = {}                            # 이곳에 활성화 결과를 저장

x = input_data

for i in range(hidden_layer_size):
    if i != 0:
        x = activations[i - 1]

    # 가중치 초깃값을 다양하게 바꿔가며 실험해보자！
    # w = np.random.randn(node_num, node_num) * 1                           # 바람직하지 않음
    # w = np.random.randn(node_num, node_num) * 0.01

    # Xavier(사비에르) 초기값을 이용
    # w = np.random.randn(node_num, node_num) * np.sqrt(1.0 / node_num)
    w = np.random.randn(node_num, node_num) * np.sqrt(2.0 / node_num)     # ReLU를 사용할 경우 He 초기값 사용(좋은 사용)
    # w = np.random.randn(node_num, node_num) * np.sqrt(node_num)           # 바람직하지 않음

    a = np.dot(x, w)

    # 활성화 함수도 바꿔가며 실험해보자！
    # z = sigmoid(a)
    z = ReLU(a)
    # z = tanh(a)

    activations[i] = z

# 히스토그램 그리기
for i, a in activations.items():
    plt.subplot(1, len(activations), i + 1)
    plt.title(str(i + 1) + "-layer")
    if i != 0: plt.yticks([], [])
    # plt.xlim(0.1, 1)
    # plt.ylim(0, 7000)

    # x(필수 입력) -데이터를 넣고자하는 x축 위치 설정
    # bins - 해당 막대의 영역을 얼마나 채우는지 결정
    plt.hist(a.flatten(), 30, range=(0, 1))
plt.show()
