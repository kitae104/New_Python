import numpy as np
import tensorflow as tf
import pandas as pd

# 1 데이터
xy = np.loadtxt("../datas/data-01-test-score.csv", delimiter=",", dtype=np.float32)
x_data = xy[:, 0:-1]    # 전체행에서 맨마지막을 제외한 모든 열
y_data = xy[:, [-1]]    # 전체행에서 맨마지막 열만

print(x_data.shape, x_data, len(x_data))
print(y_data.shape, y_data)

# 2. 텐서를 위한 플레이스 홀더
X = tf.placeholder(tf.float32, shape=[None, 3])
Y = tf.placeholder(tf.float32, shape=[None, 1])

# 3. 가중치와 bias
W = tf.Variable(tf.random_normal([3, 1]), name="weight")
# 임의의 가중치 생성
#[[-0.07078645]
# [-2.6336906 ]
# [-0.23482952]]
b = tf.Variable(tf.random_normal([1]), name='bias')
# 임의의 값 생성
# [0.14635393]

# 4.가설
hypothesis = tf.matmul(X, W) + b

# 5. 비용함수
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# 최적화
optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train = optimizer.minimize(cost)

# 세션
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# 학습
for step in range(2001):
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train], feed_dict={X:x_data, Y:y_data})

    if step % 10 == 0:
        print(step, "Cost:", cost_val, "\nPrediction:\n", hy_val)

# 테스트(예측)
print("Your score will be ", sess.run(hypothesis, feed_dict={X: [[100, 70, 101]]}))
print("Other scores will be ", sess.run(hypothesis, feed_dict={X: [[60, 70, 110], [90, 100, 80]]}))
