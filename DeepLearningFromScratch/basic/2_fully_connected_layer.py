# 신경망의 추론 구현
import numpy as np

x = np.random.randn(10, 2)  # 입력

W1 = np.random.randn(2, 4)  # 가중치 2X4
b1 = np.random.randn(4)     # 편향
W2 = np.random.randn(4, 3)  # 가중치 2X4
b2 = np.random.randn(3)     # 편향

h = np.matmul(x, W1) + b1   # 10 X 4 출력
print(h, '\n')

# 활성화 함수
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

a = sigmoid(h)      # 0~1사이의 값으로 변경
print(a, '\n')

s = np.matmul(a, W2) + b2
print(s, '\n')