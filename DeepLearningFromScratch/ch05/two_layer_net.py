# 2층 신경망 클래스
import numpy as np
from collections import OrderedDict
from DeepLearningFromScratch.libs.layers import *
from DeepLearningFromScratch.libs.gradient import *
class TwoLayerNet:

    # input_size : 입력층 뉴런수
    # hidden_size : 은닉층 뉴런수
    # output_size : 출력층 뉴런수
    # weight_init_std : 가중치 초기화시 정규분포의 스케일
    def __init__(self, input_size, hidden_size, output_size, weight_init_std = 0.01):
        # 가중치 초기화
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)

        # 계층 생성 - 계층을 순서대로 유지
        self.layers = OrderedDict()     # 순서가 있는 디셔너리 사용 
        self.layers['Affine1'] = Affine(self.params["W1"], self.params["b1"])
        self.layers['Relu1'] = Relu()
        self.layers['Affine2'] = Affine(self.params["W2"], self.params["b2"])
        self.lastLayer = SoftmaxWithLoss()      # 신경망 마지막 계층 SoftmaxWithLoss를 이용

    # 예측 수행 - forward 방식으로 수행
    # x : 이미지 데이터
    def predict(self, x):
        for layer in self.layers.values():
            x = layer.forward(x)

        return x

    # 손실 함수의 값을 구하기
    # x : 이미지 데이터
    # t : 정답 레이블
    def loss(self, x, t):
        y = self.predict(x)
        return self.lastLayer.forward(x, t)

    # 정확도 구하기
    # x : 이미지 데이터
    # t : 정답 레이블
    def accuracy(self, x, t):
        y = self.predict(x)             # 예측 값 구하고
        y = np.argmax(y, axis=1)        # 예측값 중에 가장 큰 값 선택
        if t.ndim != 1 :
            t = np.argmax(t, axis=1)    # 정답 중에 큰 값 선택

        # 예측값과 정답이 같은 경우를 합해서 전체갯수로 나눠 정확도 계산
        accuracy = np.sum(y == t) / float(x.shape[0])

        return accuracy

    # 가중치 매개변수의 기울기를 수치미분방식으로 구하기
    # x : 이미지 데이터
    # t : 정답 레이블
    def numerical_gradient(self, x, t):
        loss_W = lambda W : self.loss(x, t)

        grads = {}      # 기울기 저장
        grads['W1'] = numerical_gradient(loss_W, self.params['W1'])
        grads['b1'] = numerical_gradient(loss_W, self.params['b1'])
        grads['W2'] = numerical_gradient(loss_W, self.params['W2'])
        grads['b2'] = numerical_gradient(loss_W, self.params['b2'])

        return grads

    # 가중치 매개변수의 기울기를 오차역전파법으로 구하기
    # x : 이미지 데이터
    # t : 정답 레이블
    def gradient(self, x, t):
        # forward (순전파)
        self.loss(x, t)

        # backward(역전파)
        dout = 1
        dout = self.lastLayer.backward(dout)

        layers = list(self.layers.values())
        layers.reverse()    # 역순으로 바꾸기

        for layer in layers:
            dout = layer.backward(dout) # 역전파 수행

        # 결과 저장 - 기울기 갱신
        grads = {}
        grads["W1"], grads["b1"] = self.layers['Affine1'].dW, self.layers["Affine1"].db
        grads["W2"], grads["b2"] = self.layers['Affine2'].dW, self.layers["Affine2"].db

        return grads