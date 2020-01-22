import tensorflow as tf
import numpy as np

# 1 데이터
xy = np.loadtxt("../datas/data-03-diabetes.csv", delimiter=",", dtype=np.float32)
x_data = xy[:, 0:-1]    # 전체행에서 맨마지막을 제외한 모든 열
y_data = xy[:, [-1]]    # 전체행에서 맨마지막 열만

# 2. 텐서를 위한 X, Y 플레이스홀더
X = tf.placeholder(tf.float32, shape=[None, 8])
Y = tf.placeholder(tf.float32, shape=[None, 1])

# 3. 가중치와 bias
W = tf.Variable(tf.random_normal([8, 1]), name="weight")
b = tf.Variable(tf.random_normal([1]), name='bias')

# 4.가설(시그모이드 함수 사용)
hypothesis = tf.sigmoid(tf.matmul(X, W) + b)

# 5. 비용함수
cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1-Y) * tf.log(1 - hypothesis))

# 최적화
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

# 정확도 계산
predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)   # T : 1.0 , F : 0.0
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))

# 세션
with tf.Session() as sess:
    # 변수 초기화
    sess.run(tf.global_variables_initializer())

    # 학습
    for step in range(10001):
        cost_val, _ = sess.run([cost, train], feed_dict={X:x_data, Y:y_data})
        if step % 200 == 0:
            print(step, cost_val)

    # 결과 확인
    h, c, a = sess.run([hypothesis, predicted, accuracy], feed_dict={X:x_data, Y:y_data})
    print("\nHypothesis: ", h, "\nCorrect (Y): ", c, "\nAccuracy: ", a)