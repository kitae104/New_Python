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
keep_prob = tf.compat.v1.placeholder(tf.float32)                # 드롭아웃 계수

#========================================
# 첫번째 계층
#========================================
# 입력층 X와 첫번째 계층의 가중치 W1을 가지고 오른쪽과 아래쪽으로 한칸씩 움직이는 32개의 커널을 가진 컨볼루션 계층 만들기
# 각각의 변수와 레이어는 다음과 같은 형태로 구성됩니다.
# W1 [3 3 1 32] -> [3 3]: 커널 크기, 1: 입력값 X 의 특성수(색상), 32: 필터 갯수
# L1 Conv shape=(?, 28, 28, 32)
#    Pool     ->(?, 14, 14, 32)
W1 = tf.Variable(tf.random.normal([3, 3, 1, 32], stddev=0.01))
# tf.nn.conv2d 를 이용해 한칸씩 움직이는 컨볼루션 레이어를 쉽게 만들 수 있습니다.
# padding='SAME' 은 필터(커널) 슬라이딩시 최외곽에서 한칸 밖으로 더 움직이는 옵션(동일한 크기로 만들어냄)
L1 = tf.nn.conv2d(X, W1, strides=[1, 1, 1, 1], padding='SAME')
L1 = tf.nn.relu(L1)     # 활성화 함수 --> 컨볼류션 계층을 완성

# 폴링 계층 만들기 --> 사이즈가 줄어듬
# Pooling 역시 tf.nn.max_pool 을 이용하여 쉽게 구성할 수 있습니다.
# 앞에서 만든 컨볼루션 계층을 입력층으로 사용하고, 필터 크기를 2 X 2로 하는 풀링 계층 만들기
# strides=[1, 2, 2, 1]은 스라이딩 시 2칸씩 움직임
L1 = tf.nn.max_pool(L1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

#========================================
# 두번째 계층
#========================================
# 3 X 3 크기의 커널 64개로 컨볼루션 계층과 2 X 2 크기의 폴링 계층으로 구성
# W2 의 [3, 3, 32, 64] 에서 32 는 L1 에서 출력된 W1 의 마지막 차원, 필터의 크기 입니다.
W2 = tf.Variable(tf.random.normal([3, 3, 32, 64], stddev=0.01))
L2 = tf.nn.conv2d(L1, W2, strides=[1, 1, 1, 1], padding='SAME')
L2 = tf.nn.relu(L2)
L2 = tf.nn.max_pool(L2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

#========================================
# Full connect
#========================================
# FC 레이어: 입력값 7x7x64 -> 출력값 256
# Full connect를 위해 직전의 Pool 사이즈인 (?, 7, 7, 64) 를 참고하여 차원을 줄여줍니다.
#    Reshape  ->(?, 256)
W3 = tf.Variable(tf.random.normal([7 * 7 * 64, 256], stddev=0.01))
L3 = tf.reshape(L2, [-1, 7 * 7 * 64])   # 차원을 줄이는 단계 --> 1차원 계층으로 만듬
# 이 배열 전체를 최종 출력값의 중간 단계인 256개의 뉴런으로 연결하는 신경망을 만들어 냄
# 인접한 계층의 모든 뉴런과 상호 연결된 계층을 완전연결계층(fully connect layer)라 한다.
L3 = tf.matmul(L3, W3)
L3 = tf.nn.relu(L3)
L3 = tf.nn.dropout(L3, keep_prob)       # 과적합을 막아주는 드롭아웃 기법 사용

# 최종 출력
# 최종 출력값 L3 에서의 출력 256개를 입력값으로 받아서 0~9 레이블인 10개의 출력값을 만듭니다.
W4 = tf.Variable(tf.random.normal([256, 10], stddev=0.01))
model = tf.matmul(L3, W4)

# softmax_cross_entropy_with_logits_v2를 이용해 각 이미지에 대한 손실값을 구하고
# tf.reduce_mean을 이용해 미니 배치의 평균 손실값을 계산
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=model, labels=Y))

learning_rate = 0.001

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
        #feed_dict = {X: batch_xs, Y: batch_ys, keep_prob: 0.7}

        # 이미지 데이터를 CNN 모델을 위한 자료형태인 [28 28 1] 의 형태로 재구성합니다.
        batch_xs = batch_xs.reshape(-1, 28, 28, 1)

        _, cost_val = sess.run([optimizer, cost], feed_dict={X: batch_xs, Y: batch_ys, keep_prob: 0.7})
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
print('정확도 : ', sess.run(accuracy, feed_dict={X:mnist.test.images.reshape(-1, 28, 28, 1), Y:mnist.test.labels, keep_prob:1}))

#===================================
# 임의의 값에 대한 테스트
#===================================
# r = random.randint(0, mnist.test.num_examples - 1)
# print("라벨 : ", sess.run(tf.argmax(mnist.test.labels[r:r + 1], 1)))
# print("예측 : ", sess.run(tf.argmax(model, 1), feed_dict={X: mnist.test.images[r:r + 1]}))
#
# plt.imshow(mnist.test.images[r:r + 1].reshape(28, 28), cmap='Greys', interpolation='nearest')
# plt.show()