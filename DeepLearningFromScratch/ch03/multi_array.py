import numpy as np
A = np.array([1,2,3,4])
print(A)
# [1 2 3 4]

print(A.ndim)   # 차수
# 1

print(A.shape)  # 형상 -> 튜플로 반환
# (4,)

print(A.shape[0])   # 튜플 값 접근
# 4

B = np.array([[1,2], [3,4], [5,6]])
print(B)
# [[1 2]
#  [3 4]
#  [5 6]]

print(B.ndim)
# 2

print(B.shape)
# (3, 2)

# 행렬 곱
A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])
C = np.dot(A, B)        # 행렬 곱
print(C)
# [[19 22]
#  [43 50]]

print("행렬곱")
A = np.array([[1,2,3], [4,5,6]])
B = np.array([[[1,2], [3,4,], [5,6]]])
C = np.dot(A, B)
print(C)
# [[[22 28]]
#  [[49 64]]]

D = B.dot(A)
print(D)
# [[[ 9 12 15]
#   [19 26 33]
#   [29 40 51]]]

# 행렬 곱
A = np.array([[[1,2], [3,4,], [5,6]]])
B = np.array([7, 8])
C = np.dot(A, B)
print(C)
# [[23 53 83]]