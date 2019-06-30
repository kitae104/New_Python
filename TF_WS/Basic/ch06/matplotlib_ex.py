# 과적합 방지 기법 중 하나인 Dropout 을 사용해봅니다.
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.examples.tutorials.mnist import input_data

# 텐서플로우에 기본 내장된 mnist 모듈을 이용하여 데이터를 로드합니다.
# 지정한 폴더에 MNIST 데이터가 없는 경우 자동으로 데이터를 다운로드합니다.
# one_hot 옵션은 레이블을 one_hot 방식의 데이터로 만들어줍니다.
mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)

#================================
# 신경망 모델 구성
#================================
# 입력 값의 차원은 [배치크기, 특성값] 으로 되어 있습니다.
# 손글씨 이미지는 28x28 픽셀로 이루어져 있고, 이를 784개의 특성값으로 정합니다.
# 첫번째 차원이 None으로 되어 있는 곳에 한 번에 학습시킬 이미지의 개수를 지정
# 한 번에 학습할 개수를 계속 바꿔가면서 실험을 위해 None을 사용
X = tf.compat.v1.placeholder(tf.float32, [None, 784])

# 결과는 0~9 의 10 가지 분류를 가집니다.
Y = tf.compat.v1.placeholder(tf.float32, [None, 10])

# 학습시에는 0.8을 넣어 드롭아웃을 사용하고, 예측시에는 1을 넣어 신경망 전체를 사용
keep_prob = tf.compat.v1.placeholder(tf.float32)

# 신경망의 레이어는 다음처럼 구성합니다.
# 784(입력 특성값) -> 256 (히든레이어 뉴런 갯수) -> 256 (히든레이어 뉴런 갯수) -> 10 (결과값 0~9 분류)
# 표준편차가 0.01인 정류분포를 가지는 임의의 값으로 뉴런(변수)를 초기화 시킴
W1 = tf.Variable(tf.random.normal([784, 256], stddev=0.01))

# 입력값에 가중치를 곱하고 ReLU 함수를 이용하여 레이어를 만듭니다.
L1 = tf.nn.relu(tf.matmul(X, W1))

# 텐서플로우에 내장된 함수를 이용하여 dropout 을 적용합니다.
# 함수에 적용할 레이어와 확률만 넣어주면 됩니다.
L1 = tf.nn.dropout(L1, keep_prob)

W2 = tf.Variable(tf.random.normal([256, 256], stddev=0.01))
L2 = tf.nn.relu(tf.matmul(L1, W2))
L2 = tf.nn.dropout(L2, keep_prob)

W3 = tf.Variable(tf.random.normal([256, 10], stddev=0.01))
# 최종 모델의 출력값은 W3 변수를 곱해 10개의 분류를 가지게 됩니다.
# 출력층에는 보통 활성화 함수를 사용하지 않음
model = tf.matmul(L2, W3)

# softmax_cross_entropy_with_logits_v2를 이용해 각 이미지에 대한 손실값을 구하고
# tf.reduce_mean을 이용해 미니 배치의 평균 손실값을 계산
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=model, labels=Y))

# tf.train.AdamOptimizer 함수를 사용하여 이 손실값을 최소화하는 최적화 수행
optimizer = tf.compat.v1.train.AdamOptimizer(0.001).minimize(cost)

#================================
# 신경망 모델 학습
#================================
# 텐서플로의 세션을 초기화
init = tf.compat.v1.global_variables_initializer()
sess = tf.compat.v1.Session()
sess.run(init)

# 실제 학습
batch_size = 100
total_batch = int(mnist.train.num_examples / batch_size)
print(total_batch)

for epoch in range(30):
    total_cost = 0

    for i in range(total_batch):
        # 텐서플로우의 mnist 모델의 next_batch 함수를 이용해
        # 지정한 크기만큼 학습할 데이터를 가져옵니다.
        # batch_xs : 입력 값인 이미지 데이터 저장
        # batch_ys : 출력값인 레이블 데이터 저장
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)

        # 학습 시 0.8넣어 드롭아웃 수행
        _,cost_val = sess.run([optimizer, cost], feed_dict={X:batch_xs, Y:batch_ys, keep_prob:0.8})
        total_cost += cost_val

    print('Epoch : ', '%04d' % (epoch + 1), 'Avg. cost = ', '{:.3f}'.format(total_cost / total_batch))

print("최적화 완료!!")

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
print('정확도 : ', sess.run(accuracy, feed_dict={X:mnist.test.images, Y:mnist.test.labels, keep_prob:1}))

#================================
# 결과 출력 (matplot)
#================================
# 예측 모델을 수행한 후 결과값을 labels에 저장
labels = sess.run(model, feed_dict={X:mnist.test.images, Y:mnist.test.labels, keep_prob:1})

# 손글씨를 출력할 그래프 준비
fig = plt.figure()

# 테스트 데이터의 첫번째부터 열번째까지의 이미지와 예측한 값을 출력
for i in range(10):
    # 2행 5열의 그래프를 만들고 i + 1 번째에 숫자 이미지를 출력한다.
    subplot = fig.add_subplot(2, 5, i+1)

    # x, y 축의 눈금 제거
    subplot.set_xticks([])
    subplot.set_yticks([])

    # 출력할 이미지 위에 예측한 숫자를 출력
    # np.argmax는 tf.argmax와 같은 기능의 함수
    # labels의 i 번째 원소가 원-핫 인코딩 형식으로 되어 있으므로 해당 배열에서
    # 가장 높은 값을 가진 인덱스를 예측한 숫자로 출력한다.
    subplot.set_title('%d' % np.argmax(labels[i]))

    # 1차원 배열에 되어있는 i번째 이미지를 데이터를 28 X 28인 2차원 배열로 변형하여 이미지 형태로 출력
    # cmap 파라미터를 통해 이미지를 그레이스케일로 출력
    subplot.imshow(mnist.test.images[i].reshape((28, 28)), cmap=plt.cm.gray_r)

plt.show()