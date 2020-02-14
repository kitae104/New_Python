# mnist 신경망 처리(배치처리)
import tensorflow as tf
import numpy as np
import pickle
from DeepLearningFromScratch.dataset.mnist import load_mnist
from DeepLearningFromScratch.common.functions import sigmoid, softmax

# normalize - True의 경우 0~255의 범위가 0.0~1.0 번위로 변환됨
def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=True, one_hot_label=False)
    return x_test, t_test

def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)

    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)

    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y

if __name__ == "__main__":
    x, t = get_data()
    network = init_network()

    batch_size = 100        # 배치 크기
    accuracy_cnt = 0

    for i in range(0, len(x), batch_size):
        x_batch = x[i:i+batch_size]
        y_batch = predict(network, x_batch)
        p = np.argmax(y_batch, axis=1)    # 1번째 차원축으로 최대값 인덱스
        accuracy_cnt += np.sum(p == t[i:i+batch_size])  # True인 갯수를 합한다.

    print("정확도 :" + str(float(accuracy_cnt) / len(x)))