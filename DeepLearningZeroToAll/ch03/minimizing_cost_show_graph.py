# 최소 비용함수 구하기 
import tensorflow as tf
import matplotlib.pyplot as plt

X = [1, 2, 3]
Y = [1, 2, 3]

# 가중치
W = tf.placeholder(tf.float32)

# 가설
hypothesis = X * W

# 비용 함수
cost = tf.reduce_mean(tf.square(hypothesis - Y))

sess = tf.Session()
sess.run(tf.global_variables_initializer())

W_val = []
cost_val = []

for i in range(-30, 50):
    feed_W = i * 0.1
    curr_cost, curr_W = sess.run([cost, W], feed_dict={W: feed_W})
    W_val.append(curr_W)
    cost_val.append(curr_cost)

# 비용함수 보이기
plt.plot(W_val, cost_val)
plt.show()