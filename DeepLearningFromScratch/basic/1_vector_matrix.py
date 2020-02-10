# 벡터와 행렬
import numpy as np

# 모양 확인 하기
x = np.array([1,2,3])
print(x)    # [1 2 3]
print(x.__class__)  # 클래스 이름 표시

print(x.shape)  # (3,)  (모양)

print(x.ndim)   # 1 차원수

W = np.array([[1,2,3], [4,5,6]])
print(W.shape)  # (2, 3) (모양)
print(W.ndim)   # 2 차원수

# 행렬의 원소별 연산
W = np.array([[1,2,3], [4,5,6]])
X = np.array([[0,1,2], [3,4,5]])
print(W + X)    # 각 원소 위치별로 계산 수행
print(W * X)

# 브로드 캐스트
A = np.array([[1,2], [3,4]])
print(A * 10)
# [[10 20]
#  [30 40]]

b = np.array([10, 20])
print(A * b)
# [[10 40]
#  [30 80]]

# 벡터의 내적과 행렬 곱
# 벡터의 내적
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.dot(a, b))
# 32

# 행렬 곱
A = np.array([[1,2], [3,4]])
B= np.array([[5,6], [7,8]])
print(np.dot(A, B))
# [[19 22]
#  [43 50]]

print(np.matmul(A, B))  # np.dot(A, B)와 동일
# [[19 22]
#  [43 50]]