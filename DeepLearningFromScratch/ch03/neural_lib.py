# 신경망 라이브러리
import numpy as np

# 계단 함수
# def step_funtion(x):
#     if x > 0:
#         return 1
#     else:
#         return 0

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

# identity_function 함수(항등 함수)
def identity_function(x):
    return x

# softmax 함수
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y