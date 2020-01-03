# 간단한 신경망 작성
import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import DeepLearningFromScratch.libs.neural_lib as lib

class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2, 3)

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = lib.softmax(z)
        loss = lib.cross_entropy_error(y, t)

        return loss

if __name__ == "__main__":
    x = np.array([0.6, 0.9])
    t = np.array([0, 0, 1])

    net = simpleNet()
    print(net.W)    # 가중치 매개변수

    p = net.predict(x)
    print(p)

    res = np.argmax(p)  # 최대값의 인덱스
    print(res)

    loss = net.loss(x, t)
    print(loss)

    f = lambda w: net.loss(x, t)

    dw = lib.numerical_gradient(f, net.W)
    print(dw)

