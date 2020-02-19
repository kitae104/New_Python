# Layer 클래스 구현
import numpy as np
from DeepLearningFromScratch.common.functions import sigmoid, softmax, cross_entropy_error


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

class SoftmaxWithLoss:
    def __init__(self):
        self.params, self.grads = [], []
        self.y = None  # softmax의 출력
        self.t = None  # 정답 레이블

    def forward(self, x, t):
        self.t = t
        self.y = softmax(x)     # 소프트 맥스 사용

        # 정답 레이블이 원핫 벡터일 경우 정답의 인덱스로 변환
        if self.t.size == self.y.size:
            self.t = self.t.argmax(axis=1)

        loss = cross_entropy_error(self.y, self.t)  # 교차 엔트피 오류 사용 
        return loss

    def backward(self, dout=1):
        batch_size = self.t.shape[0]

        dx = self.y.copy()
        dx[np.arange(batch_size), self.t] -= 1
        dx *= dout
        dx = dx / batch_size

        return dx