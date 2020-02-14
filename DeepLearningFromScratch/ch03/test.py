import numpy as np

x = np.array([-1.0, 1.0, 2.0])
print(x)

y = x > 0
print(y)

y = y.astype(np.int)
print(y)

x = np.array([[0.1, 0.8, 0.1], [0.3, 0.1, 0.6], [0.2, 0.5, 0.3], [0.8, 0.1, 0.1]])
y = np.argmax(x, axis=0)    # 각 열에서 큰 값 찾기
print(y)
# [3 0 1]

y = np.argmax(x, axis=1)    # 각 행에서 큰 값 찾기
print(y)
# [1 2 1 0]

a = np.array([1,2,1,0])
b = np.array([1,2,0,0])
print(a == b)
# [ True  True False  True]

print(np.sum(a==b))     # 참의 갯수
# 3