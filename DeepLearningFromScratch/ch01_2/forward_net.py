# 2계층 순전파 구현하기
import numpy as np

# 시그모이드 함수에 의한 변환
class Sigmoid:
    def __init__(self):
        self.params = []

    def forward(self, x):
        return 1 / (1 + np.exp(-x))


# 완전연결계층에 의한 변환
class Affine:
    def __init__(self, W, b):   # 가중치, 편향
        self.params = [W, b]

    def forward(self, x):
        W, b = self.params
        out = np.dot(x, W) + b
        return out

# 2레이어의 신경망 계층
# X - Affine - Sigmoid - Affine - S
class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size):
        I, H, O = input_size, hidden_size, output_size

        # 가중치와 편향 초기화
        W1 = np.random.randn(I, H)
        b1 = np.random.randn(H)
        W2 = np.random.randn(H, O)
        b2 = np.random.randn(O)

        # 계층 생성
        self.layers = [
            Affine(W1, b1),
            Sigmoid(),
            Affine(W2, b2)
        ]

        # 모든 가중치를 리스트에 모은다.
        self.params = []
        for layer in self.layers:
            self.params += layer.params

    def predict(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x

x = np.random.randn(10, 2)      # 2차원 데이터 10개
model = TwoLayerNet(2, 4, 3)    # 입력(2) - 은닉(4) - 출력(3)
s = model.predict(x)            # 입력 x에 대한 점수s(예측 결과)
print(s)