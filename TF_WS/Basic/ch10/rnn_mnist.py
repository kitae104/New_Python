import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)

#===============================
# 옵션 설정
#===============================
learning_rate = 0.001   # 최적화 함수에서 사용할 학습률
total_epoch = 30              # 전체 데이터를 학습할 총횟수
batch_size = 128        # 미니배치로 한 번에 학습할 데이터의 개수

# RNN 은 순서가 있는 자료를 다루므로, 한 번에 입력받는 갯수와, 총 몇 단계로 이루어져있는 데이터를 받을지를 설정해야합니다.
n_input = 28            # 가로의 픽셀수
n_step = 28             # 세로의 픽셀수
n_hidden = 128
n_class = 10            # 출력은 10개(원-핫-인코딩)

#===============================
# 신경망 모델 구성
#===============================
X = tf.compat.v1.placeholder(tf.float32, [None, n_step, n_input])
Y = tf.compat.v1.placeholder(tf.float32, [None, n_class])

W = tf.Variable(tf.random.normal([n_hidden, n_class]))
b = tf.Variable(tf.random.normal([n_class]))

#===================================
# RNN 에 학습에 사용할 셀을 생성합니다
#===================================
# 다음 함수들을 사용하면 다른 구조의 셀로 간단하게 변경할 수 있습니다(BasicRNNCell,BasicLSTMCell,GRUCell)
# n_hidden 개의 출력값을 갖는 RNN 셀 생성
cell = tf.nn.rnn_cell.BasicRNNCell(n_hidden)

#=================================================
# RNN 신경망 - 복잡한 과정을 dynamic_rnn으로 해결
# states = tf.zeros(batch_size)
# for i in range(n_step):
#   outputs, states = cell(X[[:, i]], states)
#=================================================
# RNN 셀, 입력값 --> 신경망 생성
outputs, states = tf.nn.dynamic_rnn(cell, X, dtype=tf.float32)
print(outputs)      # Tensor("rnn/transpose_1:0", shape=(?, 28, 128), dtype=float32)

#===============================================
# 최종 출력값
# outputs의 형태는 (?, 28, 128) -->
# [batch_size, n_step, n_hidden] 형태
# outputs : [batch_size, n_step, n_hidden]
#        -> [n_step, batch_size, n_hidden]
#        -> [batch_size, n_hidden]
#===============================================
# 은닉층의 출력값을 가중치 W와 같은 형태로 만들어야 행렬곱 수행가능
# transpose로 위치 변경
outputs = tf.transpose(outputs, [1, 0, 2])  # [n_step, batch_size, n_hidden]
print(outputs)          # Tensor("transpose:0", shape=(28, ?, 128), dtype=float32)
# n_step 차원 제거
outputs = outputs[-1]   # [batch_size, n_hidden]
print(outputs)          # Tensor("strided_slice:0", shape=(?, 128), dtype=float32)

#===============================================
# 모델 생성
#===============================================
model = tf.matmul(outputs, W) + b
print(model)        # Tensor("add:0", shape=(?, 10), dtype=float32)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=model, labels=Y))
optimizer = tf.compat.v1.train.AdamOptimizer(learning_rate).minimize(cost)

#===============================================
# 신경망 학습과 결과 확인
#===============================================
init = tf.compat.v1.global_variables_initializer()
sess = tf.compat.v1.Session()
sess.run(init)

total_batch = int(mnist.train.num_examples / batch_size)

print('\n학습이 시작되었습니다. 학습에 상당한 시간이 걸립니다....')
for epoch in range(total_epoch):
    avg_cost = 0

    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        # 입력값의 형태 바꿔주기(주의!)
        batch_xs = batch_xs.reshape((batch_size, n_step, n_input))
        feed_dict = {X: batch_xs, Y: batch_ys}
        c, _ = sess.run([cost, optimizer], feed_dict=feed_dict)
        avg_cost += c / total_batch

    print('Epoch:', '%04d' % (epoch + 1), 'cost =', '{:.3f}'.format(avg_cost))

print('최적화 완료!')

#==============================
# 결과 확인
#==============================
is_correct = tf.equal(tf.argmax(model, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))

test_batch_size = len(mnist.test.images)
# 입력값의 형태 바꿔주기(주의!)
test_xs = mnist.test.images.reshape(test_batch_size, n_step, n_input)
test_ys = mnist.test.labels

print('정확도:', sess.run(accuracy, feed_dict={X: test_xs, Y: test_ys}))