import tensorflow as tf

# 1. 학습에 사용할 데이터 셋
x_data = [[1, 2, 1],
          [1, 3, 2],
          [1, 3, 4],
          [1, 5, 5],
          [1, 7, 5],
          [1, 2, 5],
          [1, 6, 6],
          [1, 7, 7]]
y_data = [[0, 0, 1],
          [0, 0, 1],
          [0, 0, 1],
          [0, 1, 0],
          [0, 1, 0],
          [0, 1, 0],
          [1, 0, 0],
          [1, 0, 0]]

# 테스트 데이터 셋
x_test = [[2, 1, 1],
          [3, 1, 2],
          [3, 3, 4]]
y_test = [[0, 0, 1],
          [0, 0, 1],
          [0, 0, 1]]

# 2. 텐서를 위한 X, Y 플레이스홀더
X = tf.placeholder(tf.float32, shape=[None, 3])    # 3종류의 정보 입력
Y = tf.placeholder(tf.float32, shape=[None, 3])    # 3개의 결과
nb_classes = 3

# 3. 가중치와 bias
W = tf.Variable(tf.random_normal([3, nb_classes]), name="weight")
b = tf.Variable(tf.random_normal([nb_classes]), name='bias')

# 4. 가설
# softmax = exp(logits) / reduce_sum(exp(logits), dim)
logits = tf.matmul(X, W) + b
hypothesis = tf.nn.softmax(logits)

# 5. 비용함수(다양한 형태 - cross entropy) - 전달 파라미터 주의 !!
# 주의할 점은 Y_one_hot은 label로 1개의1, 여러개의 0으로 이루어진 one_hot 벡터 이어야 한다.
# 그러면 각각의  logit에 대한 오차값이 결과로 나오고 그것을 tf.reduce_mean해주면 전체에 대한 평균오차값이 나온다.
cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), axis=1))
#cost_i = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=Y_one_hot)
#cost = tf.reduce_mean(cost_i)   # 전체에 대한 평균오차값

# 최적화
optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-1)
train = optimizer.minimize(cost)

# 정확도 계산
# argmax() : [0.1, 0.3, 0.5]의 argmax는 1로 가장 큰 값의 index 출력
prediction = tf.argmax(hypothesis, 1)   # 가장 높은 값을 가지는 index반환
correct_prediction = tf.equal(prediction, tf.argmax(Y, 1))  # 맞는지 확인
accuracy = tf.reduce_mean(tf.cast(correct_prediction, dtype=tf.float32))

# 세션
with tf.Session() as sess:
    # 변수 초기화
    sess.run(tf.global_variables_initializer())

    # 학습
    for step in range(201):
        # 학습 데이터만 사용해서 학습
        cost_val, W_val, acc, _ = sess.run([cost, W, accuracy, train], feed_dict={X:x_data, Y:y_data})

        #print("Step: {:5}\tCost: {:.3f}\tWeight: {:.3f}\tAcc: {:.2%}".format(step, cost_val, W_val, acc))
        print(step, cost_val, W_val, acc)

    # 예측 - 테스트 데이터만 사용해서 처리
    print("Prediction:", sess.run(prediction, feed_dict={X: x_test}))
    # 정확도 계산
    print("Accuracy: ", sess.run(accuracy, feed_dict={X: x_test, Y: y_test}))