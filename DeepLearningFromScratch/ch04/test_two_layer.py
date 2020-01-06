import sys, os
import numpy as np

from DeepLearningFromScratch.ch04.two_layer_nets import TwoLayerNet
sys.path.append(os.pardir)


if __name__ == "__main__":
    net = TwoLayerNet(input_size=784, hidden_size=100, output_size=10)
    print(net.params["W1"].shape)   # (784, 100)
    print(net.params["b1"].shape)   # (100,)
    print(net.params["W2"].shape)   # (100, 10)
    print(net.params["b2"].shape)   # (10,)

    # test = np.random.rand(2, 10)    # 2줄 X 10개의 임의의 데이터 생성
    # print(test)

    x = np.random.rand(100, 784)    # 더미 입력 데이터(100장 분량)
    t = np.random.rand(100, 10)     # 더미 정답 레이블(100장 분량)

    grads = net.numerical_gradient(x, t)
    print(grads["W1"].shape)        # (784, 100)
    print(grads["b1"].shape)        # (100,)
    print(grads["W2"].shape)        # (100, 10)
    print(grads["b2"].shape)        # (10,)

