# 미분 계산을 이용하는 경우
import tensorflow as tf
import matplotlib.pyplot as plt

x_data = [1, 2, 3]
y_data = [1, 2, 3]

# 가중치
W = tf.Variable(tf.random_normal([1]), name='weight')
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

# 가설
hypothesis = X * W

# 비용 함수
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# 최소화(Minimize) - 미분값 계산
learning_rate = 0.1
gradient = tf.reduce_mean((W * X - Y) * X)  # 미분 없이 사용 가능
descent = W - learning_rate * gradient
update = W.assign(descent)      # W 업데이트

# 세션 시작
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(21):
    sess.run(update, feed_dict={X: x_data, Y: y_data})  # 업데이트 실행
    print(step, sess.run(cost, feed_dict={X:x_data, Y:y_data}), sess.run(W))

