import numpy as np

# 일반적인 리스트
A = [[1, 0], [0, 1]]
B = [[1, 1], [1, 1]]
print(A + B)    # 리스트 접합

# numpy matrix
A = np.array([[1, 0], [0, 1]])
B = np.array([[1, 1], [1, 1]])
print(A + B)    # 행렬 덧셈

# 벡터 생성 - 일차원
A = np.array([1,2,3])
B = np.array([4,5,6])
print("A == ", A, "B == ", B)

# 벡터 형상 - shape
print("A.shape ==", A.shape, ", B.shape ==", B.shape)

# 벡터 차원 - ndim
print("A.ndim ==", A.ndim, ", B.ndim ==", B.ndim)

# 벡터 산술 연산
print("A + B = ", A + B)
print("A - B = ", A - B)
print("A * B = ", A * B)
print("A / B = ", A / B)
print("-" * 50)
# 행렬 생성
A = np.array([[1,2,3], [4,5,6]])
B = np.array([[-1,-2,-3], [-4,-5,-6]])

print("A == ", A)
print("B == ", B)

# 벡터 형상 - shape
print("A.shape ==", A.shape, ", B.shape ==", B.shape)

# 벡터 차원 - ndim
print("A.ndim ==", A.ndim, ", B.ndim ==", B.ndim)

# 벡터 산술 연산
print("A + B = ", A + B)
print("A - B = ", A - B)
print("A * B = ", A * B)
print("A / B = ", A / B)

# 형 변환
C = np.array([1, 2, 3])
print("C.shape == ", C.shape)

C = C.reshape(1, 3)
print("C.shape == ", C.shape)

print(A)
print("A.shape ==", A.shape)

# 형 변환
A2 = A.reshape(3,2)
print(A2)
print("A2.shape ==", A2.shape)

