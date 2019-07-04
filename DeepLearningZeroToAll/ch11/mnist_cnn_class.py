import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
import random
import matplotlib.pyplot as plt

from tensorflow.examples.tutorials.mnist import input_data

tf.set_random_seed(777)

# 텐서플로우에 기본 내장된 mnist 모듈을 이용하여 데이터를 로드합니다.
# 지정한 폴더에 MNIST 데이터가 없는 경우 자동으로 데이터를 다운로드합니다.
# one_hot 옵션은 레이블을 one_hot 방식의 데이터로 만들어줍니다.
mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)

# 하이퍼 매개변수
learning_rate = 0.001
training_epochs = 15
batch_size = 100

#======================================
# 모델을 클래스로 만들기
#======================================
class Model:

    def __init__(self, sess, name):
        self.sess = sess
        self.name = name
        self._build_net()

    def _build_net(self):
        with tf.compat.v1.variable_scope(self.name):
            # 트레이닝에 사용할 dropout (keep_prob) rate  0.7~0.5, 하지만 테스트에서는 1을 사용해야 함
            self.keep_prob = tf.compat.v1.placeholder(tf.float32)

            # Input
            self.X = tf.compat.v1.placeholder(tf.float32, [None, 784])     # n개의 이미지 28 X 28 크기
            X_img = tf.reshape(self.X, [-1, 28, 28, 1])          # img 28x28x1 (black/white)
            self.Y = tf.compat.v1.placeholder(tf.float32, [None, 10])

            W1 = tf.Variable(tf.random_normal([3, 3, 1, 32], stddev=0.01))  # 필터의 크기 3 X 3 색상은 1 필터의 갯수는 32
            # 첫번째 Convolutional Layer L1으로 들어오는 이미지 형태 shape=(?, 28, 28, 1)
            L1 = tf.nn.conv2d(X_img, W1, strides=[1, 1, 1, 1], padding='SAME')
            L1 = tf.nn.relu(L1)
            # stride에 의해 크기가 줄어듬 14 X 14 --> 풀링 수행
            L1 = tf.nn.max_pool(L1, ksize=[1,2,2,1], strides=[1,2,2,1], padding="SAME")
            L1 = tf.nn.dropout(L1, keep_prob=self.keep_prob)
#======================================================================================
            # L2으로 들어오는 이미지 형태 shape=(?, 14, 14, 32)
            W2 = tf.Variable(tf.random.normal([3, 3, 32, 64], stddev=0.01))  # 필터의 크기 3 X 3 색상은 1 필터의 갯수는 64
            # 두번째 Convolutional Layer L2으로 들어오는 이미지 형태 shape=(?, 14, 14, 32)
            L2 = tf.nn.conv2d(L1, W2, strides=[1, 1, 1, 1], padding='SAME')
            L2 = tf.nn.relu(L2)
            # stride에 의해 크기가 줄어듬 14 X 14
            L2 = tf.nn.max_pool(L2, ksize=[1,2,2,1], strides=[1,2,2,1], padding="SAME")
            L2 = tf.nn.dropout(L2, keep_prob=self.keep_prob)
#======================================================================================
            # L3으로 들어오는 이미지 형태 shape=(?, 14, 14, 32)
            W3 = tf.Variable(tf.random.normal([3, 3, 64, 128], stddev=0.01))  # 필터의 크기 3 X 3 색상은 1 필터의 갯수는 64
            # 두번째 Convolutional Layer L2으로 들어오는 이미지 형태 shape=(?, 14, 14, 32)
            L3 = tf.nn.conv2d(L2, W3, strides=[1, 1, 1, 1], padding='SAME')
            L3 = tf.nn.relu(L3)
            # stride에 의해 크기가 줄어듬 14 X 14
            L3 = tf.nn.max_pool(L3, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")
            L3 = tf.nn.dropout(L3, keep_prob=self.keep_prob)
            L3_flat = tf.reshape(L3, [-1, 128 * 4 * 4])
# ======================================================================================
            # L4 FC 4x4x128 inputs -> 625 outputs
            W4 = tf.get_variable("W4", shape=[128 * 4 * 4, 625],
                                 initializer=tf.contrib.layers.xavier_initializer())
            b4 = tf.Variable(tf.random.normal([625]))
            L4 = tf.nn.relu(tf.matmul(L3_flat, W4) + b4)  # Tensor("Relu_3:0", shape=(?, 625), dtype=float32)
            L4 = tf.nn.dropout(L4, keep_prob=self.keep_prob)  # Tensor("dropout_3/mul:0", shape=(?, 625), dtype=float32)
# ======================================================================================
            # 최종 L5 Final FC 625 inputs -> 10 개의 출력
            W5 = tf.compat.v1.get_variable("W5", shape=[625, 10], initializer=tf.contrib.layers.xavier_initializer())
            b5 = tf.Variable(tf.random.normal([10]))
            # hypothesis
            self.model = tf.matmul(L4, W5) + b5

# =======================================================================================
        # softmax_cross_entropy_with_logits_v2를 이용해 각 이미지에 대한 손실값을 구하고
        # tf.reduce_mean을 이용해 미니 배치의 평균 손실값을 계산
        self.cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=self.model, labels=self.Y))
        # tf.train.AdamOptimizer 함수를 사용하여 이 손실값을 최소화하는 최적화 수행
        self.optimizer = tf.compat.v1.train.AdamOptimizer(learning_rate = learning_rate).minimize(self.cost)

        correct_prediction = tf.equal(tf.argmax(self.model, 1), tf.argmax(self.Y, 1))
        self.accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    def predict(self, x_text, keep_prop=1.0):
        return self.sess.run(self.model, feed_dict={self.X: x_text, self.keep_prob:keep_prop})

    def get_accuracy(self, x_test, y_test, keep_prop=1.0):
        return self.sess.run(self.accuracy, feed_dict={self.X:x_test, self.Y:y_test, self.keep_prob:keep_prop})

    def train(self, x_data, y_data, keep_prop=0.7):
        return self.sess.run([self.cost, self.optimizer], feed_dict={
            self.X: x_data, self.Y: y_data, self.keep_prob: keep_prop})

#================================
# 신경망 모델 학습
#================================
# 텐서플로의 세션을 초기화
# init = tf.compat.v1.global_variables_initializer()
# sess = tf.compat.v1.Session()
# m1 = Model(sess, "m1")
# sess.run(init)
sess = tf.Session()
m1 = Model(sess, "m1")

sess.run(tf.global_variables_initializer())


# 실제 모델 학습

print('\n학습이 시작되었습니다. 학습에 상당한 시간이 걸립니다....')
for epoch in range(training_epochs):
    avg_cost = 0
    total_batch = int(mnist.train.num_examples / batch_size)

    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        c, _ = m1.train(batch_xs, batch_ys)
        avg_cost += c / total_batch

    print('Epoch:', '%04d' % (epoch + 1), 'cost =', '{:.9f}'.format(avg_cost))

print('Learning Finished!')
print("최적화 완료!!")

#================================
# 결과 확인
#================================
print("정확도 : ", m1.get_accuracy(mnist.test.images, mnist.test.labels))
