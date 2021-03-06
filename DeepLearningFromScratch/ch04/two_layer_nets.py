# 2층 신경망 클래스 구현하기
import sys, os
import numpy as np
sys.path.append(os.pardir)
from DeepLearningFromScratch.libs.functions import *
from DeepLearningFromScratch.libs.gradient import *

class TwoLayerNet:

    # 생성자 - 초기화 수행
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        #가중치 초기화
        self.params = {}    # 신경망 매개변수를 보관하는 딕셔너리

        self.params["W1"] = weight_init_std * np.random.randn(input_size, hidden_size)  # 1번째 층 가중치 - 임의의 값
        self.params["b1"] = np.zeros(hidden_size)                                       # 1번째 층 편향 - 임의의 값
        self.params["W2"] = weight_init_std * np.random.randn(hidden_size, output_size) # 2번째 층 가중치
        self.params["b2"] = np.zeros(output_size)                                       # 2번째 층 편향

    # 예측 추론을 수행
    def predict(self, x):   # 인수 x는 이미지 데이터
        W1, W2 = self.params["W1"], self.params["W2"]
        b1, b2 = self.params["b1"], self.params["b2"]

        a1 = np.dot(x, W1) + b1
        z1 = sigmoid(a1)            # 활성화 함수
        a2 = np.dot(z1, W2) + b2
        y = softmax(a2)             # 확률로 변경

        return y

    # 손실함수
    def loss(self, x, t):   # x: 입력 데이터(이미지 데이터), t : 정답 레이블
        y = self.predict(x)

        return cross_entropy_error(y, t)

    # 정확도 구하기
    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)    # 각 행에서 큰 값 위치
        t = np.argmax(t, axis=1)

        accuracy = np.sum(y == t) / float(x.shape[0])   # 예측값과 정답이 같은 경우를 전체 갯수로 나누어 정확도 계산
        return accuracy

    # 가중치 매개변수의 기울기 구하기 -> 이후에는 역전파를 사용하는 gradient() 로 변경
    def numerical_gradient(self, x, t):      # x: 입력 데이터, t : 정답 레이블
        loss_W = lambda W: self.loss(x, t)

        grads = {}  # 기울기를 보관하는 딕셔너리 변수
        # numerical_gradient(f, X) - f: loss_W 함수, X : params[]
        grads["W1"] = numerical_gradient(loss_W, self.params["W1"]) # 1번째 층 가중치의 기울기
        grads["b1"] = numerical_gradient(loss_W, self.params["b1"]) # 1번째 층 편향의 기울기
        grads["W2"] = numerical_gradient(loss_W, self.params["W2"]) # 2번째 층 가중치의 기울기
        grads["b2"] = numerical_gradient(loss_W, self.params["b2"]) # 2번째 층 편향의 기울기

        return grads

    def gradient(self, x, t):
        W1, W2 = self.params['W1'], self.params['W2']
        b1, b2 = self.params['b1'], self.params['b2']

        grads = {}  # 기울기

        batch_num = x.shape[0]  # 배치 크기

        # forward
        a1 = np.dot(x, W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        y = softmax(a2)

        # backward
        dy = (y - t) / batch_num
        grads['W2'] = np.dot(z1.T, dy)
        grads['b2'] = np.sum(dy, axis=0)

        da1 = np.dot(dy, W2.T)
        dz1 = sigmoid_grad(a1) * da1
        grads['W1'] = np.dot(x.T, dz1)
        grads['b1'] = np.sum(dz1, axis=0)

        return grads

if __name__ == "__main__":
    net = TwoLayerNet(input_size=784, hidden_size=100, output_size=10)
    print(net.params['W1'].shape)
    print(net.params['b1'].shape)
    print(net.params['W2'].shape)
    print(net.params['b2'].shape)

    x = np.random.rand(100, 784)    # 더미 입력 데이터 100장 분량
    t = np.random.rand(100, 10)     # 정답 레이블 100장 분량

    grads = net.numerical_gradient(x, t)
    print(grads['W1'].shape)
    print(grads['b1'].shape)
    print(grads['W2'].shape)
    print(grads['b2'].shape)

    y = net.predict(x)


