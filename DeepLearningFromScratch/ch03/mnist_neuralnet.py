# 신경망 추론 처리
import sys, os
sys.path.append(os.pardir)     #부모 디렉토리의 파일을 가져올 수 있도록 설정
from DeepLearningFromScratch.dataset.mnist import load_mnist
import pickle
import numpy as np
import DeepLearningFromScratch.ch03.neural_lib as lib

def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=True, one_hot_label=False)
    return x_test, t_test

def init_network():
    with open("sample_weight.pkl", "rb") as f:
        network = pickle.load(f)
    return network

def predict(network, x):
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]

    a1 = np.dot(x, W1) + b1
    z1 = lib.sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = lib.sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = lib.softmax(a3)
    return y

# if __name__ == "__main__":
#     x, t = get_data()
#     network = init_network()
#
#     accuracy_cnt = 0
#     for i in range(len(x)):
#         y = predict(network, x[i])
#         p = np.argmax(y)    # 확률이 가장 높은 원소의 인덱스를 얻는다.
#         if p == t[i]:
#             accuracy_cnt += 1
#
#     print("정확도 : " + str(float(accuracy_cnt) / len(x)))

if __name__ == "__main__":
    x, t = get_data()
    network = init_network()

    batch_size = 100
    accuracy_cnt = 0

    for i in range(0, len(x), batch_size):
        x_batch = x[i:i+batch_size]
        y_batch = predict(network, x_batch)
        p = np.argmax(y_batch, axis=1)
        accuracy_cnt += np.sum(p == t[i:i+batch_size])

    print("정확도 : " + str(float(accuracy_cnt) / len(x)))