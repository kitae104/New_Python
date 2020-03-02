# softmax classifier
import tensorflow as tf

# 1 데이터
x_data = [[1, 2, 1, 1],
          [2, 1, 3, 2],
          [3, 1, 3, 4],
          [4, 1, 5, 5],
          [1, 7, 5, 5],
          [1, 2, 5, 6],
          [1, 6, 6, 6],
          [1, 7, 7, 7]]

# one-hot encoding
y_data = [[0, 0, 1],
          [0, 0, 1],
          [0, 0, 1],
          [0, 1, 0],
          [0, 1, 0],
          [0, 1, 0],
          [1, 0, 0],
          [1, 0, 0]]

# 2. 텐서를 위한 X, Y 플레이스홀더
X = tf.placeholder(tf.float32, shape=[None, 4])
Y = tf.placeholder(tf.float32, shape=[None, 3])     # 결과, 클래스의 숫
nb_classes = 3  # 결과 종류 갯수

# 3. 가중치와 bias
W = tf.Variable(tf.random_normal([4, nb_classes]), name="weight")
b = tf.Variable(tf.random_normal([nb_classes]), name='bias')

# 4. 가설
hypothesis = tf.nn.softmax(tf.matmul(X, W) + b)

# 5. 비용함수(다양한 형태 - cross entropy)
cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), axis=1))

# 최적화
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train = optimizer.minimize(cost)

# 정확도 계산
# predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)   # T : 1.0 , F : 0.0
# accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))

# 세션
with tf.Session() as sess:
    # 변수 초기화
    sess.run(tf.global_variables_initializer())

    # 학습
    for step in range(2001):
        cost_val, _ = sess.run([cost, train], feed_dict={X:x_data, Y:y_data})

        if step % 200 == 0:
            print(step, cost_val)

    # 결과 확인
    print('--------------')
    # Testing & One-hot encoding
    a = sess.run(hypothesis, feed_dict={X: [[1, 11, 7, 9]]})
    print(a, sess.run(tf.argmax(a, 1)))

    print('--------------')
    b = sess.run(hypothesis, feed_dict={X: [[1, 3, 4, 3]]})
    print(b, sess.run(tf.argmax(b, 1)))

    print('--------------')
    c = sess.run(hypothesis, feed_dict={X: [[1, 1, 0, 1]]})
    print(c, sess.run(tf.argmax(c, 1)))

    print('--------------')
    all = sess.run(hypothesis, feed_dict={X: [[1, 11, 7, 9], [1, 3, 4, 3], [1, 1, 0, 1]]})
    print(all, sess.run(tf.argmax(all, 1)))