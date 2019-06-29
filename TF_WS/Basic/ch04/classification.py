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
# 신경망은 2차원으로 [입력층(특성), 출력층(레이블)] -> [2, 3] 으로 정합니다.
W = tf.Variable(tf.random.uniform([2,3], -1., 1.))

# 편향을 각각 각 레이어의 출력 갯수로 설정합니다.
# 편향은 출력의 갯수, 즉 최종 결과값의 분류 갯수인 3으로 설정합니다.
b = tf.Variable(tf.zeros([3]))

# 신경망에 가중치 W과 편향 b을 적용합니다
L = tf.add(tf.matmul(X, W), b)

# 텐서플로우에서 기본적으로 제공하는 활성화 함수인 ReLU 함수를 적용합니다.
L = tf.nn.relu(L)

# 마지막으로 softmax 함수를 이용하여 출력값을 사용하기 쉽게 만듭니다
# softmax 함수는 다음처럼 결과값을 전체합이 1인 확률로 만들어주는 함수입니다.
# 예) [8.04, 2.76, -6.52] -> [0.53 0.24 0.23]
model = tf.nn.softmax(L)

# 신경망을 최적화하기 위한 비용 함수를 작성합니다.
# 각 개별 결과에 대한 합을 구한 뒤 평균을 내는 방식을 사용합니다.
# 전체 합이 아닌, 개별 결과를 구한 뒤 평균을 내는 방식을 사용하기 위해 axis 옵션을 사용합니다.
# axis 옵션이 없으면 -1.09 처럼 총합인 스칼라값으로 출력됩니다.
#        Y         model         Y * tf.log(model)   reduce_sum(axis=1)   reduce_mean
# 예) [[1 0 0]  [[0.1 0.7 0.2]  -> [[-1.0  0    0]  -> [-1.0, -0.09]    --> -0.545
#     [0 1 0]]  [0.2 0.8 0.0]]     [ 0   -0.09 0]]
# 즉, 이것은 예측값과 실제값 사이의 확률 분포의 차이를 비용으로 계산한 것이며, 이것을 Cross-Entropy 라고 합니다.
cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.math.log(model), axis = 1))

##########################
# 최적화
##########################
# 기본적인 경사 하강법으로 최적화 수행
optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=0.01)
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
# 예측값 :  [0 1 1 0 0 1]
# 실제값 :  [0 1 2 0 0 2]


#################################
# 정확도 계산
#################################
# 전체 학습 데이터에 대한 예측값과 실측값을 tf.equal 함수로 비교한 뒤, true/false 값으로 나온 결과를 다시
# tf.cast 함수를 이용해서 0 과 1로 바꾸어 평균을 내면 간단히 정확도를 계산할 수 있다.
is_correct = tf.equal(prediction, target)
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
print('정확도 : %.2f' % sess.run(accuracy * 100, feed_dict={X:x_data, Y:y_data}))
# 정확도 : 66.67