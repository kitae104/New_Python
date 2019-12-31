# 3층 신경망 구현
import numpy as np
import DeepLearningFromScratch.ch03.neural_lib as lib

# 가중치와 편향을 초기화 하고 이들을 딕셔너리 변수인 network에 저장
def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])
    return network

# 입력 신호를 출력으로 변화하는 처리과정 구현
def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    a1 = np.dot(x, W1) + b1
    z1 = lib.sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = lib.sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = lib.identity_function(a3)
    return y

if __name__ == "__main__":
    network = init_network()
    x = np.array([1.0, 0.5])
    y = forward(network, x)
    print(y)