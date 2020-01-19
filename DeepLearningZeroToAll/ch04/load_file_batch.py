import tensorflow as tf

filename_queue = tf.train.string_input_producer(['../datas/data-01-test-score.csv'], shuffle=False, name='filename_queue')
reader = tf.TextLineReader()
key, value = reader.read(filename_queue)

# 값이 비었을 때 사용할 디폴트 값
record_defaults = [[0.], [0.], [0.], [0.]]
xy = tf.decode_csv(value, record_defaults=record_defaults)

# 배치 작성
train_x_batch, train_y_batch = tf.train.batch([xy[0:-1], xy[-1:]], batch_size=10)

# 2. 텐서를 위한 X, Y 플레이스홀더
X = tf.placeholder(tf.float32, shape=[None, 3])
Y = tf.placeholder(tf.float32, shape=[None, 1])

# 3. 가중치와 bias
W = tf.Variable(tf.random_normal([3, 1]), name="weight")
b = tf.Variable(tf.random_normal([1]), name='bias')

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

# filename queue 채우기 시작
coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(sess=sess, coord=coord)  # 스레드 수행

# 학습
for step in range(2001):
    x_batch, y_batch = sess.run([train_x_batch, train_y_batch])
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train], feed_dict={X:x_batch, Y:y_batch})

    if step % 10 == 0:
        print(step, "Cost :", cost_val, "\nPrediction :\n", hy_val)

coord.request_stop()
coord.join(threads)

# Ask my score
print("Your score will be ",
      sess.run(hypothesis, feed_dict={X: [[100, 70, 101]]}))

print("Other scores will be ",
      sess.run(hypothesis, feed_dict={X: [[60, 70, 110], [90, 100, 80]]}))
