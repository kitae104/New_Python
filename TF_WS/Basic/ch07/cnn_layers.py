# 신경망 구성을 손쉽게 해 주는 유틸리티 모음인 tensorflow.layers 를 사용해봅니다.
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
import random
import matplotlib.pyplot as plt

from tensorflow.examples.tutorials.mnist import input_data

tf.compat.v1.set_random_seed(777)

# 텐서플로우에 기본 내장된 mnist 모듈을 이용하여 데이터를 로드합니다.
# 지정한 폴더에 MNIST 데이터가 없는 경우 자동으로 데이터를 다운로드합니다.
# one_hot 옵션은 레이블을 one_hot 방식의 데이터로 만들어줍니다.
mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)

#======================================
# 신경망 모델 구성
#======================================
# 기존 모델에서는 입력 값을 28x28 하나의 차원으로 구성하였으나,
# CNN 모델을 사용하기 위해 2차원 평면과 특성치의 형태를 갖는 구조로 만듭니다.
X = tf.compat.v1.placeholder(tf.float32, [None, 28, 28, 1])     # 입력 (None은 입력 데이터 갯수)
Y = tf.compat.v1.placeholder(tf.float32, [None, 10])            # 출력
is_training = tf.compat.v1.placeholder(tf.bool)

#========================================
# 첫번째 계층
#========================================
# 기본적으로 inputs, outputs size, kernel_size 만 넣어주면
# 활성화 함수 적용은 물론, 컨볼루션 신경망을 만들기 위한 나머지 수치들은 알아서 계산해줍니다.
L1 = tf.layers.conv2d(X, 32, [3, 3], activation=tf.nn.relu)
L1 = tf.layers.max_pooling2d(L1, [2, 2], [2, 2])
L1 = tf.layers.dropout(L1, 0.7, is_training)

#========================================
# 두번째 계층
#========================================
L2 = tf.layers.conv2d(L1, 64, [3, 3], activation=tf.nn.relu)
L2 = tf.layers.max_pooling2d(L2, [2, 2], [2, 2])
L2 = tf.layers.dropout(L2, 0.7, is_training)

#========================================
# Full connect
#========================================
L3 = tf.contrib.layers.flatten(L2)
L3 = tf.layers.dense(L3, 256, activation=tf.nn.relu)
L3 = tf.layers.dropout(L3, 0.5, is_training)

# 최종 출력
model = tf.layers.dense(L3, 10, activation=None)

# softmax_cross_entropy_with_logits_v2를 이용해 각 이미지에 대한 손실값을 구하고
# tf.reduce_mean을 이용해 미니 배치의 평균 손실값을 계산
learning_rate = 0.001
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=model, labels=Y))
# tf.train.AdamOptimizer 함수를 사용하여 이 손실값을 최소화하는 최적화 수행
optimizer = tf.compat.v1.train.AdamOptimizer(learning_rate = learning_rate).minimize(cost)
# 최적화 함수를 RMSPropOptimizer 로 바꿔서 결과를 확인.
# optimizer = tf.train.RMSPropOptimizer(0.001, 0.9).minimize(cost)

#========================================
# 신경망 모델 학습
#========================================
# 텐서플로의 세션을 초기화
init = tf.compat.v1.global_variables_initializer()
sess = tf.compat.v1.Session()
sess.run(init)

batch_size = 100
total_batch = int(mnist.train.num_examples / batch_size)

print('\n학습이 시작되었습니다. 학습에 상당한 시간이 걸립니다....')
for epoch in range(15):
    total_cost = 0

    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        # 이미지 데이터를 CNN 모델을 위한 자료형태인 [28 28 1] 의 형태로 재구성합니다.
        batch_xs = batch_xs.reshape(-1, 28, 28, 1)

        _, cost_val = sess.run([optimizer, cost], feed_dict={X: batch_xs, Y: batch_ys, is_training:True})
        total_cost += cost_val

    print('Epoch:', '%04d' % (epoch + 1), 'cost =', '{:.3f}'.format(total_cost/total_batch))

print("최적화 완료")

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
print('정확도 : ', sess.run(accuracy, feed_dict={X:mnist.test.images.reshape(-1, 28, 28, 1), Y:mnist.test.labels, is_training:False}))

#===================================
# 임의의 값에 대한 테스트
#===================================
# r = random.randint(0, mnist.test.num_examples - 1)
# print("라벨 : ", sess.run(tf.argmax(mnist.test.labels[r:r + 1], 1)))
# print("예측 : ", sess.run(tf.argmax(model, 1), feed_dict={X: mnist.test.images[r:r + 1], is_training:False}))
#
# plt.imshow(mnist.test.images[r:r + 1].reshape(28, 28), cmap='Greys', interpolation='nearest')
# plt.show()