# Repeat 노드와 Sum 노드
# 서로간의 순전파와 역전파가 반대관계
import numpy as np

# Repeat 노드
D, N = 8, 7
x = np.random.randn(1, D)       # 입력
print(x, '\n')
y = np.repeat(x, N, axis=0)     # 순전파, axis=0 열에 대해 처리
print(y, '\n')

dy = np.random.randn(N, D)      # 무작위 기울기
print(dy, "\n")
dx = np.sum(dy, axis=0, keepdims=True)  # 역전파, 2차원 배열의 차원수 유지
print(dx, '\n')

# Sum 노드
D, N = 8, 7
x = np.random.randn(N, D)
print(x, '\n')
y = np.sum(x, axis=0, keepdims=True)    # 순전파, axis=0 열에 대해 처리, 차원수 유지
print(y, '\n')

dy = np.random.randn(1, D)
print(dy, '\n')
dx = np.repeat(dy, N, axis=0)   # 역전파
print(dy, '\n')