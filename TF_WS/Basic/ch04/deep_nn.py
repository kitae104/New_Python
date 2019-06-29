###############################
# 심층 신경망 구현하기
###############################
# 털과 날개가 있는지 없는지에 따라, 포유류인지 조류인지 분류하는 신경망 모델을 만들어봅니다.
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
import numpy as np

# [털, 날개]
x_data = np.array([[0, 0], [1, 0], [1, 1], [0, 0], [0, 0], [0, 1]])

# [기타, 포유류, 조류]
# 다음과 같은 형식을 one-hot 형식의 데이터라고 합니다.
y_data = np.array([
    [1, 0, 0],  # 기타
    [0, 1, 0],  # 포유류
    [0, 0, 1],  # 조류
    [1, 0, 0],  # 기타
    [1, 0, 0],  # 기타
    [0, 0, 1]   # 조류
])

############################################
# 신경망 모델 구성 : X와 Y의 관계를 알아내는 모델
############################################
X = tf.compat.v1.placeholder(tf.float32)
Y = tf.compat.v1.placeholder(tf.float32)

# 가중치와 편향
# 첫번째 가중치의 차원은 [특성, 히든 레이어의 뉴런갯수] -> [2, 10] 으로 정합니다.
W1 = tf.Variable(tf.random.uniform([2,10], -1., 1.))

# 두번째 가중치의 차원을 [첫번째 히든 레이어의 뉴런 갯수, 분류 갯수] -> [10, 3] 으로 정합니다.
W2 = tf.Variable(tf.random.uniform([10,3], -1., 1.))

# 편향을 각각 각 레이어의 아웃풋 갯수로 설정합니다.
# b1 은 히든 레이어의 뉴런 갯수 10으로, b2 는 최종 결과값 즉, 분류 갯수인 3으로 설정합니다.
b1 = tf.Variable(tf.zeros([10]))
b2 = tf.Variable(tf.zeros([3]))

# 신경망의 히든 레이어에 가중치 W1과 편향 b1을 적용합니다
L1 = tf.add(tf.matmul(X, W1), b1)

# 텐서플로우에서 기본적으로 제공하는 활성화 함수인 ReLU 함수를 적용합니다.
L1 = tf.nn.relu(L1)

# 최종적인 아웃풋을 계산합니다.
# 히든레이어에 두번째 가중치 W2와 편향 b2를 적용하여 3개의 출력값을 만들어냅니다.
model = tf.add(tf.matmul(L1, W2), b2)

# 텐서플로우에서 기본적으로 제공되는 크로스 엔트로피 함수를 이용해
# 복잡한 수식을 사용하지 않고도 최적화를 위한 비용 함수를 다음처럼 간단하게 적용할 수 있습니다.
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=Y, logits=model))

##########################
# 최적화
##########################
# AdamOptimizer가 GradientDescentOptimizer 보다 일반적으로 더 좋은 성능
optimizer = tf.compat.v1.train.AdamOptimizer(learning_rate=0.01)
train_op = optimizer.minimize(cost)

##########################
# 신경망 모델 학습
##########################
# 텐서플로의 세션을 초기화
init = tf.compat.v1.global_variables_initializer()
sess = tf.compat.v1.Session()
sess.run(init)

# 학습하는 과정 - 100번 진행
for step in range(100):
    sess.run(train_op, feed_dict={X:x_data, Y:y_data})

    # 학습 도중 10번에 한 번씩 손실값을 출력
    if(step + 1) % 10 == 0:
        print(step + 1, sess.run(cost, feed_dict={X:x_data, Y:y_data}))

#################################
# 결과 확인
# 0: 기타 1: 포유류, 2: 조류
#################################
# tf.argmax: 예측값과 실제값의 행렬에서 tf.argmax 를 이용해 가장 큰 값의 위치 인덱스를 가져옵니다.
# 예) [[0 1 0] [1 0 0]] -> [1 0]
#    [[0.2 0.7 0.1] [0.9 0.1 0.]] -> [1 0]
prediction = tf.argmax(model, axis = 1)
target = tf.argmax(Y, axis = 1)
print("예측값 : ", sess.run(prediction, feed_dict={X:x_data}))
print("실제값 : ", sess.run(target, feed_dict={Y:y_data}))
# 예측값 :  [0 1 2 0 0 2]
# 실제값 :  [0 1 2 0 0 2]

#################################
# 정확도 계산
#################################
# 전체 학습 데이터에 대한 예측값과 실측값을 tf.equal 함수로 비교한 뒤, true/false 값으로 나온 결과를 다시
# tf.cast 함수를 이용해서 0 과 1로 바꾸어 평균을 내면 간단히 정확도를 계산할 수 있다.
is_correct = tf.equal(prediction, target)
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
print('정확도 : %.2f' % sess.run(accuracy * 100, feed_dict={X:x_data, Y:y_data}))
# 정확도 : 100.00