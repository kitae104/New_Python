import pickle

import numpy as np
from collections import OrderedDict

from DeepLearningFromScratch.common.gradient import numerical_gradient
from DeepLearningFromScratch.common.layers import *

class SimpleConvNet:
    """단순한 합성곱 신경망

    Parameters
    ----------
        input_size : 입력 크기（MNIST의 경우엔 784）
        hidden_size_list : 각 은닉층의 뉴런 수를 담은 리스트（e.g. [100, 100, 100]）
        output_size : 출력 크기（MNIST의 경우엔 10）
        activation : 활성화 함수 - 'relu' 혹은 'sigmoid'
        weight_init_std : 가중치의 표준편차 지정（e.g. 0.01）
       'relu'나 'he'로 지정하면 'He 초깃값'으로 설정
       'sigmoid'나 'xavier'로 지정하면 'Xavier 초깃값'으로 설정
    """
    def __init__(self, input_dim = (1, 28, 28),     # 입력 데이터의 차수
                 conv_param={'filter_num':30, 'filter_size':5, 'pad':0, 'stride':1}, # 합성곱 계층의 파라미터
                 hidden_size=100, output_size=10, weight_init_std=0.01):

        ######################################
        # 기본 정보 설정 - 초기화
        ######################################
        filter_num = conv_param['filter_num']
        filter_size = conv_param['filter_size']
        filter_pad = conv_param['pad']
        filter_stride = conv_param['stride']
        input_size = input_dim[1]
        conv_output_size = (input_size - filter_size + 2 * filter_pad) / filter_stride + 1      # 합성곱 출력 크기 설정
        pool_output_size = int(filter_num * (conv_output_size / 2) * (conv_output_size / 2))    # 풀링 출력 크기 설정

        ##############################################
        # 학습에 필요한 매개변수(가중치, 편향) 초기화
        ##############################################
        self.params = {}

        # 1층의 합성곱 계층(conv)의 가중치와 편향
        self.params['W1'] = weight_init_std * np.random.randn(filter_num, input_dim[0], filter_size, filter_size)
        self.params['b1'] = np.zeros(filter_num)

        # 2층 완전 연결 계층(affine)의 가중치와 편향
        self.params['W2'] = weight_init_std * np.random.randn(pool_output_size, hidden_size)
        self.params['b2'] = np.zeros(hidden_size)

        # 2층 완전 연결 계층(affine)의 가중치와 편향
        self.params['W3'] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params['b3'] = np.zeros(output_size)

        ######################################
        # CNN을 구성하는 계층 생성
        ######################################
        self.layers = OrderedDict()                 # 순서가 있는 딕셔너리

        # conv - relu - pool - affine - relu - affine - softmax 순서로 처리
        self.layers['Conv1'] = Convolution(self.params['W1'], self.params['b1'], conv_param['stride'], conv_param['pad'])
        self.layers['Relu1'] = Relu()
        self.layers['Pool1'] = Pooling(pool_h=2, pool_w=2, stride=2)
        self.layers['Affine1'] = Affine(self.params['W2'], self.params['b2'])
        self.layers['Relu2'] = Relu()
        self.layers['Affine2'] = Affine(self.params['W3'], self.params['b3'])
        self.last_layer = SoftmaxWithLoss()

    ######################################
    # 추론 수행
    ######################################
    def predict(self, x):
        for layer in self.layers.values():
            x = layer.forward(x)            # 앞에서 부터 순서대로 순전파 수행

        return x

    ######################################
    # 손실 함수의 값 계산
    ######################################
    def loss(self, x, t):
        """손실 함수를 구한다.

        Parameters
        ----------
        x : 입력 데이터
        t : 정답 레이블
        """
        y = self.predict(x)     # 추론 수행 (처음부터 마지막까지)
        # y:추론값, t 정답
        return self.last_layer.forward(y, t)    # 마지막 계층에 순전파 수행

    ######################################
    # 역전파를 사용하여 기울기 계산하기
    ######################################
    def gradient(self, x, t):
        # 순전파
        self.loss(x, t)

        # 역전파
        dout = 1
        dout = self.last_layer.backward(dout)      # 마지막 결과로 부터

        layers = list(self.layers.values())
        layers.reverse()                            # 처음까지 역순으로 역전파 수행
        for layer in layers:
            dout = layer.backward(dout)

        # 결과 저장
        grads = {}
        # 각 레이어에 기울기에 대한 미분 계산 후 저장
        grads['W1'] = self.layers['Conv1'].dW
        grads['b1'] = self.layers['Conv1'].db
        grads['W2'] = self.layers['Affine1'].dW
        grads['b2'] = self.layers['Affine1'].db
        grads['W3'] = self.layers['Affine2'].dW
        grads['b3'] = self.layers['Affine2'].db

        return grads    # 기울기 정보 반환

    ######################################
    # 정확도 출력
    ######################################
    def accuracy(self, x, t, batch_size=100):
        if t.ndim != 1:                 # 정답의 차수가 1이 아니면
            t = np.argmax(t, axis=1)    # 각 행에서 제일 큰 값을 추출

        acc = 0.0       # 정확도 초기화

        for i in range(int(x.shape[0] / batch_size)):
            tx = x[i*batch_size:(i+1)*batch_size]   # 배치 데이터
            tt = t[i*batch_size:(i+1)*batch_size]   # 배치 정답
            y = self.predict(tx)                    # 추축값 계산
            y = np.argmax(y, axis=1)                # 행에서 추축값 중에 제일 큰값 선택
            acc += np.sum(y == tt)

        return acc / x.shape[0]                       # 평균을 구해서 반환

    ######################################
    # 파리미터 pkl 파일로 저장
    ######################################
    def save_params(self, file_name="params.pkl"):
        params = {}
        for key, val in self.params.items():
            params[key] = val
        with open(file_name, 'wb') as f:
            pickle.dump(params, f)

    ######################################
    # pkl 파일로부터 파라미터 읽어오기
    ######################################
    def load_params(self, file_name="params.pkl"):
        with open(file_name, 'rb') as f:
            params = pickle.load(f)
        for key, val in params.items():
            self.params[key] = val

        for i, key in enumerate(['Conv1', 'Affine1', 'Affine2']):
            self.layers[key].W = self.params['W' + str(i + 1)]
            self.layers[key].b = self.params['b' + str(i + 1)]

    def numerical_gradient(self, x, t):
        """기울기를 구한다（수치미분）.

        Parameters
        ----------
        x : 입력 데이터
        t : 정답 레이블

        Returns
        -------
        각 층의 기울기를 담은 사전(dictionary) 변수
            grads['W1']、grads['W2']、... 각 층의 가중치
            grads['b1']、grads['b2']、... 각 층의 편향
        """
        loss_w = lambda w: self.loss(x, t)

        grads = {}
        for idx in (1, 2, 3):
            grads['W' + str(idx)] = numerical_gradient(loss_w, self.params['W' + str(idx)])
            grads['b' + str(idx)] = numerical_gradient(loss_w, self.params['b' + str(idx)])

        return grads

    def gradient(self, x, t):
        """기울기를 구한다(오차역전파법).

        Parameters
        ----------
        x : 입력 데이터
        t : 정답 레이블

        Returns
        -------
        각 층의 기울기를 담은 사전(dictionary) 변수
            grads['W1']、grads['W2']、... 각 층의 가중치
            grads['b1']、grads['b2']、... 각 층의 편향
        """
        # forward
        self.loss(x, t)

        # backward
        dout = 1
        dout = self.last_layer.backward(dout)

        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            dout = layer.backward(dout)

        # 결과 저장
        grads = {}
        grads['W1'], grads['b1'] = self.layers['Conv1'].dW, self.layers['Conv1'].db
        grads['W2'], grads['b2'] = self.layers['Affine1'].dW, self.layers['Affine1'].db
        grads['W3'], grads['b3'] = self.layers['Affine2'].dW, self.layers['Affine2'].db

        return grads