import numpy as np
# 1차원 배열
a = [1, 2, 3, 4, 5, 6, 7, 8]

# 2차원 배열
b = np.reshape(a, (2, 4))
print(b)
'''
[[1 2 3 4]
 [5 6 7 8]]
'''
c = np.reshape(a, (4, 2))
print(c)
'''
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
'''

# 3차원 배열
a = np.arange(1, 9)
print(a)
'''
[1 2 3 4 5 6 7 8]
'''

b = a.reshape(2, 2, 2)
print(b)
'''
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
'''

# reshape(-1,정수) : 행의 위치에 -1인 경우
x = np.arange(12)
x = x.reshape(3, 4)
print(x)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''

a = x.reshape(-1, 1)
print(a)
'''
[[ 0]
 [ 1]
 [ 2]
 [ 3]
 [ 4]
 [ 5]
 [ 6]
 [ 7]
 [ 8]
 [ 9]
 [10]
 [11]]
'''

b = x.reshape(-1, 2)
print(b)
'''
[[ 0  1]
 [ 2  3]
 [ 4  5]
 [ 6  7]
 [ 8  9]
 [10 11]]
'''

c = x.reshape(-1, 3)
print(c)
'''
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
'''

# reshape(정수,-1) : 열의 위치에 -1인 경우
a = x.reshape(1, -1)
print(a)
'''
[[ 0  1  2  3  4  5  6  7  8  9 10 11]]
'''

b = x.reshape(2, -1)
print(b)
'''
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]]
'''

c = x.reshape(3, -1)
print(c)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''
# reshape(-1)인 경우
a = x.reshape(-1)
print(a)
'''
[ 0  1  2  3  4  5  6  7  8  9 10 11]
'''

b = x.reshape(1, -1)
print(b)
'''
[[ 0  1  2  3  4  5  6  7  8  9 10 11]]
'''

