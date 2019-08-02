# array 생성과 기본값 채우기
import numpy as np

# 0으로 채운 배열 생성
a = np.zeros((3,2))
print(a)

# 1로 채운 배열 생성
b = np.ones((4,2))
print(b)

# 지정값으로 채운 배열 생성
c = np.full((2, 3), 8)
print(c)

# 대각선만 1인 배열 생성
d = np.eye(5)
print(d)

# 랜덤 값으로 채운 배열 생성
e = np.random.random((2, 3))
print(e)