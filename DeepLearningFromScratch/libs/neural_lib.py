# 신경망 라이브러리
import numpy as np

# 계단 함수
def step_function(x):
    y = x > 0
    return y.astype(np.int)

# 시그모이드 함수
def sigmoid(x):
    return 1/(1 + np.exp(-x))

# ReLU 함수
def relu(x):
    return np.maximum(0, x)

# softmax
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)     # 오버 플로우 해결
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

# 평균 제곱 오차 함수
def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

# 교차 엔트로피 오차 함수
# def cross_entropy_error(y, t):
#     if y.ndim == 1:
#         t = t.reshape(1, t.size)
#         y = y.reshape(1, t.size)
#
#     batch_size = y.shape[0]
#     delta = 1e-7
#
#     # 원-핫-인코딩 시 사용
#     #return -np.sum(t * np.log(y + delta)) / batch_size
#
#     # 훈련 데이터가 원-핫 벡터라면 정답 레이블의 인덱스로 반환
#     if t.size == y.size:
#         t = t.argmax(axis=1)
#
#     # print(t)                              # 정답 위치
#     # print(y[np.arange(batch_size), t])    # 정답 확률값
#
#     return -np.sum(np.log(y[np.arange(batch_size), t] + delta)) / batch_size
def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    # 훈련 데이터가 원-핫 벡터라면 정답 레이블의 인덱스로 반환
    if t.size == y.size:
        t = t.argmax(axis=1)

    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size

# 수치 미분
def numerical_diff(f, x):
     h = 1e-4 # 0.0001
     return (f(x+h) - f(x-h)) / (2*h)

# 기울기 계산
# def numerical_gradient(f, x):
#     h = 1e-4       # 0.0001
#     grad = np.zeros_like(x)     # x와 형상이 같은 배열 생성
#
#     for idx in range(x.size):
#         tmp_val = x[idx]
#
#         # f(x + h) 계산
#         x[idx] = tmp_val + h
#         fxh1 = f(x)
#
#         # f(x - h) 계산
#         x[idx] = tmp_val - h
#         fxh2 = f(x)
#
#         grad[idx] = (fxh1 - fxh2) / (2 * h)
#         x[idx] = tmp_val    # 값 복원
#
#     return grad

def numerical_gradient(f, x):
    h = 1e-4  # 0.0001
    grad = np.zeros_like(x)

    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x)  # f(x+h)

        x[idx] = tmp_val - h
        fxh2 = f(x)  # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2 * h)

        x[idx] = tmp_val  # 값 복원
        it.iternext()

    return grad


# 경사 하강법
# f : 최적화 하려는 함수
# init_x : 초깃값
# lr : learning rate 학습률
# step_num : 반복횟수
def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x

    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad

    return x