# 텐서보드를 이용하기 위해 각종 변수들을 설정하고 저장하는 방법을 익혀봅니다.
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
import numpy as np

#
data = np.loadtxt('./data.csv', delimiter=',', unpack=True, dtype='float32')

# 털, 날개, 기타, 포유류, 조류
# x_data = 0, 1 --> 앞 2열 추출하기
x_data = np.transpose(data[0:2])
#print(x_data)

# y_data = 2, 3, 4 --> 뒤 3열 추출하기
y_data = np.transpose(data[2:])
#print(y_data)

#=================================
# 신경망 모델 구성
#=================================
# 학습에 직접적으로 사용하지 않고 학습 횟수에 따라 단순히 증가시킬 변수를 만듭니다.
global_step = tf.Variable(0, trainable=False, name='global_step')

X = tf.compat.v1.placeholder(tf.float32)
Y = tf.compat.v1.placeholder(tf.float32)

# with tf.name_scope 으로 묶은 블럭은 텐서보드에서 한 레이어안에 표현해줍니다
with tf.name_scope('layer1'):
    W1 = tf.Variable(tf.random.uniform([2, 10], -1., 1.), name='W1')
    L1 = tf.nn.relu(tf.matmul(X, W1))

with tf.name_scope('layer2'):
    W2 = tf.Variable(tf.random.uniform([10, 20], -1., 1.), name='W2')
    L2 = tf.nn.relu(tf.matmul(L1, W2))

with tf.name_scope('output'):
    W3 = tf.Variable(tf.random.uniform([20, 3], -1., 1.), name='W3')
    # 최종 모델
    model = tf.nn.relu(tf.matmul(L2, W3))

with tf.name_scope('optimizer'):
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=Y, logits=model))
    optimizer = tf.compat.v1.train.AdamOptimizer(learning_rate=0.01)

    # 최적화 함수가 학습용 변수들을 최적화할 때마다 global_step 변수의 값을 1씩 증가 시킴
    train_op = optimizer.minimize(cost, global_step=global_step)

    # tf.summary.scalar 를 이용해 수집하고 싶은 값들을 지정할 수 있습니다.
    # 손실값을 추적하기 위해 수집할 값을 지정 --> 하나의 텐서 수집
    tf.summary.scalar('cost', cost)
    tf.summary.histogram("Weights", W1)

#=================================
# 신경망 모델 학습
#=================================
# 모델을 저장하고 불러오는 API를 초기화합니다.
# global_variables 함수를 통해 앞서 정의하였던 변수들을 저장하거나 불러올 변수들로 설정합니다.
sess = tf.compat.v1.Session()
saver = tf.compat.v1.train.Saver(tf.compat.v1.global_variables())

# ./model 디렉토리에 기존에 학습해둔 모델이 있는지 확인해서 모델이 있으면 saver.restore 함수를 사용해
# 학습된 값들을 불러오고, 아니면 변수를 새로 초기화 한다.
# 학습된 모델을 저장한 파일을 체크포인트 파일이라 한다.
ckpt = tf.train.get_checkpoint_state('./model')
if ckpt and tf.compat.v1.train.checkpoint_exists(ckpt.model_checkpoint_path):
    saver.restore(sess, ckpt.model_checkpoint_path)
else:
    sess.run(tf.global_variables_initializer())

# 텐서보드에서 표시해주기 위한 텐서들을 수집합니다.
merged = tf.summary.merge_all()

# 저장할 그래프와 텐서값들을 저장할 디렉토리를 설정합니다.
writer = tf.summary.FileWriter('./logs', sess.graph)

# 이렇게 저장한 로그는, 학습 후 다음의 명령어를 이용해 웹서버를 실행시킨 뒤
# tensorboard --logdir=./logs
# 다음 주소와 웹브라우저를 이용해 텐서보드에서 확인할 수 있습니다.
# http://localhost:6006

# 최적화 진행
for step in range(100):
    sess.run(train_op, feed_dict={X:x_data, Y:y_data})

    print('Step : %d, ' % sess.run(global_step),
          'Cost : %.3f' % sess.run(cost, feed_dict={X:x_data, Y:y_data}))

    # 적절한 시점에 저장할 값들을 수집하고 저장합니다.
    summary = sess.run(merged, feed_dict={X: x_data, Y: y_data})
    writer.add_summary(summary, global_step=sess.run(global_step))

# 최적화가 끝난 뒤, 변수를 저장합니다.
saver.save(sess, './model/dnn.ckpt', global_step=global_step)

#=================================
# 결과 확인
# 0: 기타 1: 포유류, 2: 조류
#=================================
prediction = tf.argmax(model, axis = 1)
target = tf.argmax(Y, axis = 1)
print("예측값 : ", sess.run(prediction, feed_dict={X:x_data}))
print("실제값 : ", sess.run(target, feed_dict={Y:y_data}))

#=================================
# 정확도 계산
#=================================
# 전체 학습 데이터에 대한 예측값과 실측값을 tf.equal 함수로 비교한 뒤, true/false 값으로 나온 결과를 다시
# tf.cast 함수를 이용해서 0 과 1로 바꾸어 평균을 내면 간단히 정확도를 계산할 수 있다.
is_correct = tf.equal(prediction, target)
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
print('정확도 : %.2f' % sess.run(accuracy * 100, feed_dict={X:x_data, Y:y_data}))