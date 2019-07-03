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

# 트레이닝에 사용할 dropout (keep_prob) rate  0.7~0.5, 하지만 테스트에서는 1을 사용해야 함
keep_prob = tf.compat.v1.placeholder(tf.float32)

# Input
X = tf.compat.v1.placeholder(tf.float32, [None, 784])     # n개의 이미지 28 X 28 크기
X_img = tf.reshape(X, [-1, 28, 28, 1])          # img 28x28x1 (black/white)
Y = tf.compat.v1.placeholder(tf.float32, [None, 10])

W1 = tf.Variable(tf.random.normal([3, 3, 1, 32], stddev=0.01))  # 필터의 크기 3 X 3 색상은 1 필터의 갯수는 32

# 첫번째 Convolutional Layer L1으로 들어오는 이미지 형태 shape=(?, 28, 28, 1)
L1 = tf.nn.conv2d(X_img, W1, strides=[1, 1, 1, 1], padding='SAME')
print(L1)           # Tensor("Conv2D:0", shape=(?, 28, 28, 32), dtype=float32)

L1 = tf.nn.relu(L1)
print(L1)           # Tensor("Relu:0", shape=(?, 28, 28, 32), dtype=float32)

# stride에 의해 크기가 줄어듬 14 X 14 --> 풀링 수행
L1 = tf.nn.max_pool(L1, ksize=[1,2,2,1], strides=[1,2,2,1], padding="SAME")
print(L1)           # Tensor("MaxPool:0", shape=(?, 14, 14, 32), dtype=float32)


L1 = tf.nn.dropout(L1, keep_prob=keep_prob)
print(L1)           # Tensor("dropout/mul:0", shape=(?, 14, 14, 32), dtype=float32)

#======================================================================================
# L2으로 들어오는 이미지 형태 shape=(?, 14, 14, 32)
W2 = tf.Variable(tf.random.normal([3, 3, 32, 64], stddev=0.01))  # 필터의 크기 3 X 3 색상은 1 필터의 갯수는 64

# 두번째 Convolutional Layer L2으로 들어오는 이미지 형태 shape=(?, 14, 14, 32)
L2 = tf.nn.conv2d(L1, W2, strides=[1, 1, 1, 1], padding='SAME')
print(L2)           # Tensor("Conv2D_1:0", shape=(?, 14, 14, 64), dtype=float32)

L2 = tf.nn.relu(L2)
print(L2)           # Tensor("Relu_1:0", shape=(?, 14, 14, 64), dtype=float32)

# stride에 의해 크기가 줄어듬 14 X 14
L2 = tf.nn.max_pool(L2, ksize=[1,2,2,1], strides=[1,2,2,1], padding="SAME")
print(L2)           # Tensor("MaxPool_1:0", shape=(?, 7, 7, 64), dtype=float32)

L2 = tf.nn.dropout(L2, keep_prob=keep_prob)

#======================================================================================
# L3으로 들어오는 이미지 형태 shape=(?, 14, 14, 32)
W3 = tf.Variable(tf.random.normal([3, 3, 64, 128], stddev=0.01))  # 필터의 크기 3 X 3 색상은 1 필터의 갯수는 64

# 두번째 Convolutional Layer L2으로 들어오는 이미지 형태 shape=(?, 14, 14, 32)
L3 = tf.nn.conv2d(L2, W3, strides=[1, 1, 1, 1], padding='SAME')
print(L2)           # Tensor("Conv2D_1:0", shape=(?, 14, 14, 64), dtype=float32)

L3 = tf.nn.relu(L3)
print(L3)           # Tensor("Relu_1:0", shape=(?, 14, 14, 64), dtype=float32)

# stride에 의해 크기가 줄어듬 14 X 14
L3 = tf.nn.max_pool(L3, ksize=[1,2,2,1], strides=[1,2,2,1], padding="SAME")
print(L2)           # Tensor("MaxPool_1:0", shape=(?, 7, 7, 64), dtype=float32)

L3 = tf.nn.dropout(L3, keep_prob=keep_prob)

#======================================================================================

# Fully-Connected Layer --> 한 줄로 길게 뽑아
L3_flat = tf.reshape(L3, [-1, 128 * 4 * 4])
print(L3_flat)      # Tensor("Reshape_1:0", shape=(?, 3136), dtype=float32)

#======================================================================================
# L4 FC 4x4x128 inputs -> 625 outputs
W4 = tf.compat.v1.get_variable("W4", shape=[4 * 4 * 128, 625], initializer=tf.contrib.layers.xavier_initializer())
b4 = tf.Variable(tf.random.normal([625]))
L4 = tf.nn.relu(tf.matmul(L3_flat, W4) + b4)    # Tensor("Relu_3:0", shape=(?, 625), dtype=float32)
L4 = tf.nn.dropout(L4, keep_prob=keep_prob)     # Tensor("dropout_3/mul:0", shape=(?, 625), dtype=float32)

#======================================================================================

# 최종 L5 Final FC 625 inputs -> 10 개의 출력
W5 = tf.compat.v1.get_variable("W5", shape=[625, 10], initializer=tf.contrib.layers.xavier_initializer())
b5 = tf.Variable(tf.random.normal([10]))

# hypothesis
model = tf.matmul(L4, W5) + b5

# softmax_cross_entropy_with_logits_v2를 이용해 각 이미지에 대한 손실값을 구하고
# tf.reduce_mean을 이용해 미니 배치의 평균 손실값을 계산
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=model, labels=Y))

# tf.train.AdamOptimizer 함수를 사용하여 이 손실값을 최소화하는 최적화 수행
optimizer = tf.compat.v1.train.AdamOptimizer(learning_rate = learning_rate).minimize(cost)

#================================
# 신경망 모델 학습
#================================
# 텐서플로의 세션을 초기화
init = tf.compat.v1.global_variables_initializer()
sess = tf.compat.v1.Session()
sess.run(init)

# 실제 모델 학습

print('\n학습이 시작되었습니다. 학습에 상당한 시간이 걸립니다....')
for epoch in range(training_epochs):
    avg_cost = 0
    total_batch = int(mnist.train.num_examples / batch_size)

    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        feed_dict = {X: batch_xs, Y: batch_ys, keep_prob: 0.7}
        c, _ = sess.run([cost, optimizer], feed_dict=feed_dict)
        avg_cost += c / total_batch

    print('Epoch:', '%04d' % (epoch + 1), 'cost =', '{:.9f}'.format(avg_cost))

print("학습 완료!!")

#================================
# 결과 확인
#================================
# model 로 예측한 값과 실제 레이블인 Y의 값을 비교합니다.
# tf.argmax 함수를 이용해 예측한 값에서 가장 큰 값을 예측한 레이블이라고 평가합니다.
# 예) [0.1 0 0 0.7 0 0.2 0 0 0 0] -> 3
prediction = tf.argmax(model, axis = 1)
target = tf.argmax(Y, axis = 1)

is_correct = tf.equal(prediction, target)
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
print('정확도 : ', sess.run(accuracy, feed_dict={X:mnist.test.images, Y:mnist.test.labels, keep_prob: 1}))

#===================================
# 임의의 값에 대한 테스트
#===================================
r = random.randint(0, mnist.test.num_examples - 1)
print("라벨 : ", sess.run(tf.argmax(mnist.test.labels[r:r + 1], 1)))
print("예측 : ", sess.run(tf.argmax(model, 1), feed_dict={X: mnist.test.images[r:r + 1], keep_prob: 1}))

#===================================
# 임의의 그림
#===================================
plt.imshow(mnist.test.images[r:r + 1].reshape(28, 28), cmap='Greys', interpolation='nearest')
plt.show()