# 텐서플로의 옵티마이져를 사용하는 경우
import tensorflow as tf
import matplotlib.pyplot as plt

X = [1, 2, 3]
Y = [1, 2, 3]

# 가중치
W = tf.Variable(5.0, name='weight')

# 가설
hypothesis = X * W

# 비용 함수
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# 최소화(Minimize) - 옵티마이져 사용
learning_rate = 0.1
#gradient = tf.reduce_mean((W * X - Y) * X)  # 미분 없이 사용 가능
#descent = W - learning_rate * gradient
#update = W.assign(descent)      # W 업데이트
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
train = optimizer.minimize(cost)

# 세션 시작
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(100):
    print(step, sess.run(W))
    sess.run(train)
