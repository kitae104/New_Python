# array 연산
import numpy as np

a = np.array([[1,2], [3,4]])
b = np.array([[5,6], [7,8]])

print(a + b)
print("-"*50)

print(b - a)
print("-"*50)

print(a * b)
print("-"*50)

print(a / b)
print("-"*50)

# 행렬 곱셈
print(a@b)