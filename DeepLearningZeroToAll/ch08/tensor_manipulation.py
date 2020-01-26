import tensorflow as tf
import numpy as np

sess = tf.Session()

# 1차원
t = np.array([0., 1., 2., 3., 4., 5., 6.])
print(t)
print(t.ndim)   # rank
print(t.shape)
print(t[0], t[1], t[-1])
print(t[2:5], t[4:-1])
print(t[:2], t[3:])

# 2차원
t = np.array([[1., 2., 3.],
              [4., 5., 6.],
              [7., 8., 9.],
              [10., 11., 12.]])
print(t)
print(t.ndim)   # rank
print(t.shape)

t = tf.constant([1,2,3,4])
print(tf.shape(t))

t = tf.constant([[1,2],
                 [3,4]])
print(t.shape)
print(t.dtype)

t = tf.constant([
                    [
                        [
                            [1, 2, 3, 4],
                            [5, 6, 7, 8],
                            [9, 10, 11, 12]
                        ],
                        [
                            [13, 14, 15, 16],
                            [17, 18, 19, 20],
                            [21, 22, 23, 24]
                        ]
                    ]
                ])
print(t.shape, t.dtype)

matrix1 = tf.constant([[1., 2.], [3., 4.]])
matrix2 = tf.constant([[1.],[2.]])
print(matrix1.shape)
print(matrix2.shape)
print(sess.run(tf.matmul(matrix1, matrix2)))

m1 = tf.constant([[1., 2.]])
m2 = tf.constant(3.)
print(sess.run(m1 + m2))

m1 = tf.constant([[1., 2.]])
m2 = tf.constant([[3.], [4.]])
print(sess.run(m1 + m2))

# 평균 구하기
x = [[1., 2.],
     [3., 4.]]

print(sess.run(tf.reduce_mean(x)))  # 전체 평균
print(sess.run(tf.reduce_mean(x, axis=0)))  # 세로 평균
print(sess.run(tf.reduce_mean(x, axis=1)))  # 가로 평균
print(sess.run(tf.reduce_mean(x, axis=-1)))  # 가로 평균

# 합 구하기
x = [[1., 2.],
     [3., 4.]]

print(sess.run(tf.reduce_sum(x)))   # 전체 합
print(sess.run(tf.reduce_sum(x, axis=0)))   # 세로 합
print(sess.run(tf.reduce_sum(x, axis=1)))   # 가로 합
print(sess.run(tf.reduce_sum(x, axis=-1)))   # 가로 합
print(sess.run(tf.reduce_mean(tf.reduce_sum(x, axis=-1))))  # 가로 합의 평균

# argmax : 가장 큰 값의 위치
x = [[0., 1., 2.],
     [2., 1., 0.]]

print(sess.run(tf.argmax(x)))
print(sess.run(tf.argmax(x, axis=0)))   # 세로 중 제일 큰 값 위치
print(sess.run(tf.argmax(x, axis=1)))   # 가로 요소중 가장 큰 값의 위치
print(sess.run(tf.argmax(x, axis=-1)))   # 가로 요소중 가장 큰 값의 위치

# reshape
t = np.array([[[0, 1, 2],
               [3, 4, 5]],

              [[6, 7, 8],
               [9, 10, 11]]])

print(t.shape)

arr = tf.reshape(t, shape=[-1, 3])
print(sess.run(arr))

arr2 = tf.reshape(t, shape=[-1, 1, 3])
print(sess.run(arr2))

# squeeze - 여러개를 하나로 묶을 때 , expand - 하나를 여러개로 만들 때
t = [[0], [1], [2]]
arr = tf.squeeze(t)
print(sess.run(arr))

arr2 = tf.expand_dims(arr, 1)
print(sess.run(arr2))

# one hot
t = [[0], [1], [2], [0]]
arr = tf.one_hot(t, depth=10)
print(sess.run(arr))

arr2 = tf.one_hot(t, depth=3)
arr3 = tf.reshape(arr2, shape=[-1, 3])
print(sess.run(arr3))

# casting
print(sess.run(tf.cast([1.8, 5.2], tf.int32)))
print(sess.run(tf.cast([True, False, 1==1, 1 == 0], tf.int32)))

# Stack
x = [1, 4]
y = [2, 5]
z = [3, 6]
stack = tf.stack([x, y, z])
print(sess.run(stack))

stack2 = tf.stack([x, y, z], axis=1)
print(sess.run(stack2))

# ones와 zeros
x = [[0,1,2],
     [2,1,0]]

arr = tf.ones_like(x)
print(sess.run(arr))

zero = tf.zeros_like(x)
print(sess.run(zero))

# zip
for x, y in zip([1,2,3], [4,5,6]):
    print(x, y)

for x, y, z in zip([1,2,3], [4,5,6], [7,8,9]):
    print(x, y, z)

