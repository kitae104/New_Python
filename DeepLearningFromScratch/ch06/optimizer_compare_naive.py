# 최적화 방식 비교
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict
from DeepLearningFromScratch.common.optimizer import *

def f(x, y):
    return x**2 / 20.0 + y**2


def df(x, y):
    return x / 10.0, 2.0*y

init_pos = (-7.0, 2.0)              # 시작 위치
params = {}                         # 파라미터
params['x'], params['y'] = init_pos[0], init_pos[1]
grads = {}                          # 기울기
grads['x'], grads['y'] = 0, 0

# 최적화 방식들
optimizers = OrderedDict()                        # 순서를 갖는 딕셔너리
optimizers["SGD"] = SGD(lr=0.95)                 # SGD
optimizers["Momentum"] = Momentum(lr=0.1)       # Momentum
optimizers["AdaGrad"] = AdaGrad(lr=1.5)         # AdaGrad
optimizers["Adam"] = Adam(lr=0.3)               # Adam

idx = 1

plt.figure(figsize=(8,8))     # 전체 그래프 크기 설정

for key in optimizers:
    optimizer = optimizers[key]
    x_history = []
    y_history = []
    params['x'], params['y'] = init_pos[0], init_pos[1]

    for i in range(30):
        x_history.append(params['x'])
        y_history.append(params['y'])

        grads['x'], grads['y'] = df(params['x'], params['y'])
        optimizer.update(params, grads)

    # 그래프 범위 설정
    x = np.arange(-10, 10, 0.01)
    y = np.arange(-5, 5, 0.01)

    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    # 외곽선 단순화
    mask = Z > 7
    Z[mask] = 0

    # 그래프 그리기

    plt.subplot(2, 2, idx)      # 서브 플롯 그리기
    idx += 1
    plt.plot(x_history, y_history, 'o-', color='red')
    plt.contour(X, Y, Z)
    plt.ylim(-10, 10)
    plt.xlim(-10, 10)
    plt.plot(0, 0, '+')
    plt.title(key)
    plt.xlabel("x")
    plt.ylabel("y")


plt.show()