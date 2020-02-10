# Gradient descent 구현하기
# import tensorflow.compat.v1 as tf
# tf.disable_v2_behavior()
import tensorflow as tf
import numpy as np
print(tf.__version__)

tf.executing_eagerly()     # 즉시 실행
tf.random.set_seed(0)

X = [1., 2., 3., 4.]
Y = [1., 3., 5., 7.]
# W = tf.Variable(tf.random.normal((1,), -100., 100.))    # 정규분포 이용 -100~100 사이의 값
W = tf.Variable([5.])

print(W)

for step in range(300):
    hypothesis = W * X
    cost = tf.reduce_mean(tf.square(hypothesis - Y))

    learn_rate = 0.01      # learning_rate(학습률)
    # 경사 구하기
    gradient = tf.reduce_mean(tf.multiply(tf.multiply(W, X) - Y, X))

    # 하강 - 내려가기
    descent = W - tf.multiply(learn_rate, gradient)

    W.assign(descent)

    if step % 10 == 0:
        print('{:5} | {:10.4f} | {:10.6f}'.format(step, cost.numpy(), W.numpy()[0]))
