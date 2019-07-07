# 대표적인 비지도(Unsupervised) 학습 방법인 Autoencoder를 구현해봅니다.
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)

#==================================
# 옵션 설정
#==================================
learning_rate = 0.01    # 최적화 함수에서 사용할 학습률
training_epoch = 20     # 전체 데이터를 학습할 총횟수
batch_size = 100        # 미니배치로 한 번에 학습할 데이터의 개수
# 신경망 레이어 구성 옵션
n_hidden = 256          # 히든 레이어의 뉴런 갯수
n_input = 28*28         # 입력값 크기 - 이미지 픽셀수(784)

#==================================
# 신경망 모델 구성
#==================================
# 비지도 학습이기 때문에 Y가 없습니다. 입력값을 Y로 사용하기 때문.
X = tf.placeholder(tf.float32, [None, n_input])

# 인코더 레이어와 디코더 레이어의 가중치와 편향 변수를 설정.
# 다음과 같이 이어지는 레이어를 구성하기 위한 값들 입니다.
# input -> encode -> decode -> output

#==================================
# 인코더
#==================================
# n_hidden개의 뉴런을 가진 은닉층 만듬 (W와 b 만듬)
# 입력값인 n_input 값 보다 은닉층인 n_hidden 값이 더 적음
# --> 입력값을 압축하고 노이즈를 제거하면서 입력값의 특징을 찾아냄.
W_encode = tf.Variable(tf.random.normal([n_input, n_hidden]))
b_encode = tf.Variable(tf.random.normal([n_hidden]))

# sigmoid 함수를 이용해 신경망 레이어를 구성합니다.
# sigmoid(X * W + b)
# 인코더 레이어 구성
encoder = tf.nn.sigmoid(tf.add(tf.matmul(X, W_encode), b_encode))

#==================================
# 디코더
#==================================
W_decode = tf.Variable(tf.random.normal([n_hidden, n_input]))
b_decode = tf.Variable(tf.random.normal([n_input]))

# 디코더 레이어 구성
decoder = tf.nn.sigmoid(tf.add(tf.matmul(encoder, W_decode), b_decode))

#==================================
# 손실 함수
#==================================
# 디코더는 인풋과 최대한 같은 결과를 내야 하므로, 디코딩한 결과를 평가하기 위해
# 입력 값인 X 값을 평가를 위한 실측 결과 값으로하여 decoder 와의 차이를 손실값으로 설정.
cost = tf.reduce_mean(tf.pow(X - decoder, 2))

#==================================
# 최적화 함수
#==================================
optimizer = tf.train.RMSPropOptimizer(learning_rate=learning_rate).minimize(cost)

#==================================
# 신경망 모델 학습
#==================================
# 텐서플로의 세션을 초기화
init = tf.compat.v1.global_variables_initializer()
sess = tf.compat.v1.Session()
sess.run(init)

total_batch = int(mnist.train.num_examples / batch_size)

print('\n학습이 시작되었습니다. 학습에 상당한 시간이 걸립니다....')
for epoch in range(training_epoch):
    total_cost = 0

    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        _, cost_val = sess.run([optimizer, cost], feed_dict={X: batch_xs})
        total_cost += cost_val

    print('Epoch:', '%04d' % (epoch + 1), 'Avg. cost =', '{:.4f}'.format(total_cost/total_batch))

print("최적화 완료")

#==================================
# 결과 확인 - 이미지 출력
#==================================
sample_size = 10        # 10개의 테스트 데이터 가져오기

# 디코더를 이용해 출력값 만들기
samples = sess.run(decoder, feed_dict={X: mnist.test.images[:sample_size]})
print(samples)

fig, ax = plt.subplots(2, sample_size, figsize=(sample_size, 2))

for i in range(sample_size):
    ax[0][i].set_axis_off()
    ax[1][i].set_axis_off()
    ax[0][i].imshow(np.reshape(mnist.test.images[i], (28, 28)))     # 입력값 이미지
    ax[1][i].imshow(np.reshape(samples[i], (28, 28)))               # 생성한 이미지

plt.show()
