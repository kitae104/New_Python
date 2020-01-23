# animal classification with softmax_cross_entropy_with_logits
import tensorflow as tf
import numpy as np

xy = np.loadtxt('../datas/data-04-zoo.csv', delimiter=',', dtype=np.float32)
x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]
print(x_data.shape, y_data.shape)

# 2. 텐서를 위한 X, Y 플레이스홀더
X = tf.placeholder(tf.float32, shape=[None, 16])
Y = tf.placeholder(tf.int32, shape=[None, 1])     # 결과, 0~6
nb_classes = 7  # 결과 종류 갯수 0~6

Y_one_hot = tf.one_hot(Y, nb_classes)       # one_hot shape = (?, 1, 7)
Y_one_hot = tf.reshape(Y_one_hot, [-1, nb_classes]) # shape = (?, 7)


# 3. 가중치와 bias
W = tf.Variable(tf.random_normal([16, nb_classes]), name="weight")
b = tf.Variable(tf.random_normal([nb_classes]), name='bias')

# 4. 가설
logits = tf.matmul(X, W) + b
hypothesis = tf.nn.softmax(logits)

# 5. 비용함수(다양한 형태 - cross entropy)
cost_i = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=Y_one_hot)
cost = tf.reduce_mean(cost_i)

# 최적화
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train = optimizer.minimize(cost)

# 정확도 계산
prediction = tf.argmax(hypothesis, 1)
correct_prediction = tf.equal(prediction, tf.argmax(Y_one_hot, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, dtype=tf.float32))

# 세션
with tf.Session() as sess:
    # 변수 초기화
    sess.run(tf.global_variables_initializer())

    # 학습
    for step in range(2001):
        cost_val, acc, _ = sess.run([cost, accuracy, train], feed_dict={X:x_data, Y:y_data})

        if step % 100 == 0:
            print("Step: {:5}\tCost: {:.3f}\tAcc: {:.2%}".format(step, cost_val, acc))

    # Let's see if we can predict
    pred = sess.run(prediction, feed_dict={X: x_data})

    # y_data: (N,1) = flatten => (N, ) matches pred.shape
    for p, y in zip(pred, y_data.flatten()):
        print("[{}] Prediction: {} True Y: {}".format(p == int(y), p, int(y)))