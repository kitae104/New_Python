# 2차원 배열
a=[[1,2,3], [4,5,6]]
print(a)
print(a[0][1])

a[0][1] = 100
print(a)

y = range(5, 10)
print(y[0])

z = list(range(5, 10))
print(z)

a = (1,2,3)
print(a)
print(a[1])

a = (1,)
print(type(a))

num=[2,4,6,8, 10]
for i, n in enumerate(num):
    num[i] = n * 2
print(num)

a = [1, 2] + [3, 4]
print(a)

import numpy as np
x = np.array([1,2,3])
print(x)

y = np.array([4,5,6])
print(x + y)

print(type(x))

x[0] = 100
print(x)

print(np.arange(10))

a = np.array([1, 1])
b = a
print("a=", str(a))
print("b=" + str(b))
b[0] = 100
print("a=", str(a))
print("b=", str(b))

a = np.array([1, 1])
b = a.copy()
print("a=", str(a))
print("b=" + str(b))
b[0] = 100
print("a=", str(a))
print("b=", str(b))
print("b=", b)

# 행렬
# 2차원 행렬
x = np.array([[1,2,3], [4,5,6]])
print(x)
print(x.shape)

w, h = x.shape
print(w)
print(h)

print(x[1,2])
x[1,2] = 100
print(x)

# 요소가 0/1인 ndarray 만들기
x = np.zeros(10)
print(x)

x = np.ones(10)
print(x)

x = np.zeros((2, 10))
print(x)

x = np.ones((2, 10))
print(x)

# 요소가 랜덤인 행렬 생성
x = np.random.rand(2, 10)
print(x)

# 행렬의 크기 변경
a = np.arange(10)
print(a)

a = a.reshape(2, 5)
print(a)

# 행렬의 사칙연산
x = np.array([[4,4,4], [8,8,8]])
y = np.array([[1,1,1], [2,2,2]])
print(x + y)

# 스칼라 X 행렬
x = np.array([[4,4,4], [8,8,8]])
print(x * 10)

# 산술 함수
x = np.array([[4,4,4], [8,8,8]])
print(np.exp(x))
print(np.sqrt(x))
print(np.round(x, 2))
print(np.mean(x))
print(np.std(x))
print(np.max(x))
print(np.min(x))

# 행렬곱 계산
v = np.array([[1,2,3], [4,5,6]])
w = np.array([[1,1], [2,2], [3,3]])
print(v.dot(w))

# 슬라이싱
x = np.arange(10)
print(x[2:5])
print(x[:5])
print(x[5:])
print(x[::2])
print(x[1::2])
print(x[::-1])

y = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(y)
print(y[:2, 1:2])

# bool 배열 사용
x = np.array([1,1,2,3,5,8,13])
print(x>3)
print(x[x>3])

# 조건을 충족하는 원소만 999로 변경
x[x>3] = 999
print(x)

# help 사용
#help(np.random.randint(5, 10, (3,2)))

