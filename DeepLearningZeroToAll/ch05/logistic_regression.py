# 논리적인 회귀 분석
import tensorflow as tf

# 데이터 설정
x_data = [[1, 2],
          [2, 3],
          [3, 1],
          [4, 3],
          [5, 3],
          [6, 2]]

# logistic의 경우 결과가 항상 0 또는 1로 설정
y_data = [[0],
          [0],
          [0],
          [1],
          [1],
          [1]]

# 2. 텐서를 위한 X, Y 플레이스홀더
X = tf.placeholder(tf.float32, shape=[None, 2])
Y = tf.placeholder(tf.float32, shape=[None, 1])

# 3. 가중치와 bias
W = tf.Variable(tf.random_normal([2, 1]), name="weight")
b = tf.Variable(tf.random_normal([1]), name='bias')         # 나가는 결과의 갯수와 동일

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