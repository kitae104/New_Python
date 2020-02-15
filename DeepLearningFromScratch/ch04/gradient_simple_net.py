# 간단한 신경망
import numpy as np
from DeepLearningFromScratch.common.functions import softmax, cross_entropy_error
from DeepLearningFromScratch.common.gradient import numerical_gradient

class simpleNet:

    def __init__(self):
        self.W = np.random.randn(2, 3)  # 정규분포로 초기화

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)
        return loss

# def f(W):
#     return net.loss(x, t)

if __name__ == "__main__":
    net = simpleNet()
    print(net.W)    # 가중치 매개변수

    x = np.array([0.6, 0.9])
    p = net.predict(x)
    print(p)

    idx = np.argmax(p)
    print(idx)

    t = np.array([0, 0, 1])
    res = net.loss(x, t)
    print(res, '\n')

    f = lambda w : net.loss(x, t)

    dW = numerical_gradient(f, net.W)
    print(dW)