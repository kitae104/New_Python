import tensorflow as tf
import matplotlib.pyplot as plt
import random
from tensorflow.examples.tutorials.mnist import input_data

# 1. 학습에 사용할 데이터 셋
# 데이터 셋 읽어오기
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# 2. 텐서를 위한 X, Y 플레이스홀더
# MNIST data image의 형태는 28 * 28 = 784
nb_classes = 10     # 10개의 결과물로 구분
X = tf.placeholder(tf.float32, shape=[None, 784])           # 784개의 픽셀 정보 입력
Y = tf.placeholder(tf.float32, shape=[None, nb_classes])    # 구분되는 결과

# 3. NN 사용으로 변경 --> xavier
W1 = tf.Variable(tf.random_normal([784, 256]), name="weight_1")
b1 = tf.Variable(tf.random_normal([256]), name='bias_1')
L1 = tf.nn.relu(tf.matmul(X, W1) + b1)

W2 = tf.Variable(tf.random_normal([256, 256]), name="weight_2")
b2 = tf.Variable(tf.random_normal([256]), name='bias_2')
L2 = tf.nn.relu(tf.matmul(L1, W2) + b2)

W3 = tf.Variable(tf.random_normal([256, nb_classes]), name="weight_3")
b3 = tf.Variable(tf.random_normal([nb_classes]), name='bias_3')
hypothesis = tf.matmul(L2, W3) + b3

# 5. 비용함수(다양한 형태 - cross entropy) - 전달 파라미터 주의 !!
# 주의할 점은 Y_one_hot은 label로 1개의1, 여러개의 0으로 이루어진 one_hot 벡터 이어야 한다.
# 그러면 각각의  logit에 대한 오차값이 결과로 나오고 그것을 tf.reduce_mean해주면 전체에 대한 평균오차값이 나온다.
# cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), axis=1))
cost_i = tf.nn.softmax_cross_entropy_with_logits(logits=hypothesis, labels=Y)
cost = tf.reduce_mean(cost_i)   # 전체에 대한 평균오차값

# 최적화
optimizer = tf.train.AdamOptimizer(learning_rate=1e-3)
train = optimizer.minimize(cost)

# 정확도 계산 (Test model)
# argmax() : [0.1, 0.3, 0.5]의 argmax는 1로 가장 큰 값의 index 출력
prediction = tf.argmax(hypothesis, 1)   # 가장 높은 값을 가지는 index반환
is_correct = tf.equal(prediction, tf.argmax(Y, 1))  # 맞는지 확인
accuracy = tf.reduce_mean(tf.cast(is_correct, dtype=tf.float32))

# 파라미터
training_epochs = 15    # 전체 데이터 셋을 한 번 학습을 1 epochs --> 15번 학습
batch_size = 100        # 한 번에 읽어올 크기
total_batch = int(mnist.train.num_examples / batch_size)    # 전체 배치 갯수

# 세션
with tf.Session() as sess:
    # 변수 초기화
    sess.run(tf.global_variables_initializer())

    # 학습 사이클
    for epoch in range(training_epochs):
        avg_cost = 0

        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)  # 배치 크기만큼 처리
            cost_val, _ = sess.run([cost, train], feed_dict={X:batch_xs, Y:batch_ys})
            avg_cost += cost_val / total_batch

        print("Epoch: {:04d}, Cost: {:.9f}".format(epoch + 1, avg_cost))
    print("학습 finished")

    # 테스트 셋을 이용해서 정확도 측정
    print(
        "Accuracy: ",
        accuracy.eval(
            session=sess, feed_dict={X: mnist.test.images, Y: mnist.test.labels}
        ),
    )

    # Get one and predict
    r = random.randint(0, mnist.test.num_examples - 1)
    print("Label: ", sess.run(tf.argmax(mnist.test.labels[r: r + 1], 1)))
    print(
        "Prediction: ",
        sess.run(tf.argmax(hypothesis, 1), feed_dict={X: mnist.test.images[r: r + 1]}),
    )

    plt.imshow(
        mnist.test.images[r: r + 1].reshape(28, 28),
        cmap="Greys",
        interpolation="nearest",
    )
    plt.show()