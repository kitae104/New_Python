# 단순 선형 회귀 구현
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
tf.enable_eager_execution()

# 데이터
x_data = [1, 2, 3, 4, 5]
y_data = [1, 2, 3, 4, 5]

# 변수
W = tf.Variable(2.9)
b = tf.Variable(0.5)

learning_rate = 0.01    # 학습률 - 기울기 반영을 위해 사용

for i in range(100):
    # Gradient descent
    with tf.GradientTape() as tape:
        # 가설
        hypothesis = W * x_data + b
        # 비용함수
        cost = tf.reduce_mean(tf.square(hypothesis - y_data))
    # 기울기
    W_grad, b_grad = tape.gradient(cost, [W, b])
    W.assign_sub(learning_rate * W_grad)
    b.assign_sub(learning_rate * b_grad)

    if i % 10 == 0:
        print("{:5}|{:10.4f}|{:10.4f}|{:10.6f}".format(i, W.numpy(), b.numpy(), cost))

plt.plot(x_data, y_data, 'o')
plt.plot(x_data, hypothesis.numpy(), 'g-')
plt.xlim(0, 8)
plt.ylim(0, 8)
plt.show()


