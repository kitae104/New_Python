# 은닉층이 하나인 신경망 구현
import numpy as np
from DeepLearningFromScratch.ch01_2.layer_classes import Affine, Sigmoid, SoftmaxWithLoss

class TowLayerNet:

    # input_size : 입력층 뉴런수
    # hidden_size : 은닉층 뉴런수
    # output_size : 출력층 뉴런수
    def __init__(self, input_size, hidden_size, output_size):
        I, H, O = input_size, hidden_size, output_size

        # 가중치와 편향 초기화
        W1 = 0.01 * np.random.randn(I, H)       # 가중치는 무작위 값으로 초기화
        b1 = np.zeros(H)                        # 편향 벡터 0으로 초기화
        W2 = 0.01 * np.random.randn(H, O)
        b2 = np.zeros(O)

        # 계층 생성
        self.layers = [
            Affine(W1, b1),
            Sigmoid(),
            Affine(W2, b2)
        ]

        self.loss_layer = SoftmaxWithLoss()

        # 모든 가중치와 기울기를 리스트에 모은다.
        self.params, self.grads = [], []
        for layer in self.layers:
            self.params += layer.params
            self.grads += layer.grads

    # 추론 수행 - 순전파 진행
    def predict(self, x):
        for layer in self.layers:
            x = layer.forward(x)

        return x

    # 순전파
    def forward(self, x, t):
        score = self.predict(x)
        loss = self.loss_layer.forward(score, t)

        return loss

    # 역전파
    def backward(self, dout=1):
        dout = self.loss_layer.backward(dout)
        for layer in reversed(self.layers):         # 역순으로 진행
            dout =layer.backward(dout)

        return dout
