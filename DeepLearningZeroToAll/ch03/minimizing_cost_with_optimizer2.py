# 텐서플로의 옵티마이져를 사용하는 경우
import tensorflow as tf
import matplotlib.pyplot as plt

X = [1, 2, 3]
Y = [1, 2, 3]

# 가중치
W = tf.Variable(5.)

# 가설
hypothesis = X * W

# 수식에 의한 gradient
gradient = tf.reduce_mean((W * X - Y) * X) * 2  # 미분 없이 사용 가능

# 비용 함수
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# 최소화(Minimize) - 옵티마이져 사용
learning_rate = 0.1
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)

# cost에 맞는 gradients 계산하기
gvs = optimizer.compute_gradients(cost)

# optimizer에 적용하기
apply_gradients = optimizer.apply_gradients(gvs)

# 세션 시작
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(100):
    print(step, sess.run([gradient, W, gvs]))
    sess.run(apply_gradients)
