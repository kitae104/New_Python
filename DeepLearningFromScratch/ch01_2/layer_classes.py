# Layer 클래스 구현
import numpy as np
from DeepLearningFromScratch.common.functions import sigmoid

class MatMul:
    def __init__(self, W):
        self.params = [W]                   # 학습하는는 개변수 보관
        self.grads = [np.zeros_like(W)]     # 기울기 보관
        self.x = None

    def forward(self, x):
        W, = self.params
        out = np.matmul(x, W)
        self.x = x

        return out

    def backward(self, dout):
        W, = self.params
        dx = np.matmul(dout, W.T)
        dW = np.matmul(self.x.T, dout)
        self.grads[0][...] = dW             # 넘파이 배열의 덮어쓰기 수행(깊은 복사)

        return dx

class Sigmoid:
    def __init__(self):
        self.params, self.grads = [], []
        self.out = None

    def forward(self, x):
        out = sigmoid(x)
        self.out = out          # 출력을 out 변수에 저장

        return out

    def backward(self, dout):
        dx = dout * (1.0 - self.out) * self.out # 저장된 out 변수를 이용하여 처리

        return dx

class Affine:
    def __init__(self, W, b):
        self.params = [W, b]                                # 매개변수 저장
        self.grads = [np.zeros_like(W), np.zeros_like(b)]   # 기울기 저장
        self.x = None

    def forward(self, x):
        W, b = self.params
        out = np.matmul(x, W) + b
        self.x = x

        return out

    def backward(self, dout):
        W, b = self.params
        dx = np.matmul(dout, W.T)
        dW = np.matmul(self.x.T, dout)
        db = np.sum(dout, axis=0)

        self.grads[0][...] = dW
        self.grads[1][...] = db

        return dx