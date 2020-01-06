import numpy as np

X = np.random.rand(2)       # 입력
print(X)
# 임의의 2 입력 값 [0.24165606 0.82969676]

W = np.random.rand(2, 3)    # 가중치
print(W)
# 임의의 2 X 3 가중치
# [[0.76232208 0.23336361 0.79421915]
#  [0.37263418 0.63819314 0.9971085 ]]

B = np.random.rand(3)
print(B)
# 임의의 2 편향 값  [0.2147239  0.28684187 0.62775917]

Y = np.dot(X, W) + B
print(Y)
# 출력값 [0.70811702 0.87274239 1.64698474]

X_dot_W = np.array([[0, 0, 0], [10, 10, 10]])
print(X_dot_W)
# [[ 0  0  0]
#  [10 10 10]]

B = np.array([1, 2, 3])
Y = X_dot_W + B
print(Y)
# [[ 1  2  3]
#  [11 12 13]]

dY = np.array([[1, 2, 3], [4, 5, 6]])
print(dY)

dB = np.sum(dY, axis=0)     # 세로로 더하기
print(dB)