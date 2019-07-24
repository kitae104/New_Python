# MNIST 데이터 처리하기
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

print(mnist.train.num_examples, mnist.test.num_examples, mnist.validation.num_examples)
# 55000 10000 5000

print("train image shape :", np.shape(mnist.train.images))
# train image shape : (55000, 784)
print("train label shape :", np.shape(mnist.train.labels))
# train label shape : (55000, 10)
print("test image shape :", np.shape(mnist.test.images))
# test image shape : (10000, 784)
print("test label shape :", np.shape(mnist.test.labels))
# test label shape : (10000, 10)

#================================
# 하이퍼 파라미터 정의
#================================
learning_rate = 0.1         # 학습률
epochs = 100                # 반복 횟수
batch_size = 100            # 한번에 입력으로 주어지는 MNIST 갯수

input_nodes = 784           # 입력 노드 갯수
hidden_nodes = 100          # 은닉 노드 갯수
output_nodes = 10           # 출력 노드 갯수

X = tf.compat.v1.placeholder(tf.float32, [None, input_nodes])
Y = tf.compat.v1.placeholder(tf.float32, [None, output_nodes])

W2 = tf.Variable(tf.random.normal([input_nodes, hidden_nodes]))     # 은닉층 가중치 노드
b2 = tf.Variable(tf.random.normal([hidden_nodes]))                  # 은닉층 바이어스 노드

W3 = tf.Variable(tf.random.normal([hidden_nodes, output_nodes]))    # 출력층 가중치 노드
b3 = tf.Variable(tf.random.normal([output_nodes]))                  # 출력층 바이어스 노드

#================================
# feed forward 정의
#================================
# 선형회귀
Z2 = tf.matmul(X, W2) + b2
# 은닉층 출력 값 sigmoid 대신 relu 사용
A2 = tf.nn.relu(Z2)

Z3 = tf.matmul(A2, W3) + b3
logist = Z3

y = A3 = tf.nn.softmax(Z3)

#================================
# 손실함수 최소값 구하기
#================================
# 출력층 선형회귀 값(logits) Z3와 정답 Y를 이용하여 손실함수 크로스 엔트로피 계산
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=Z3, labels=Y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate)
train = optimizer.minimize(loss)        # 손실함수 줄이기

# batch_size * 10 데이터에 대해 argmax를 통해 행단위로 비교함
# 출력값과 정답을 이용해서 예측값 계산
predicated_val = tf.equal(tf.argmax(A3, 1), tf.argmax(Y, 1))

# batch_size * 10의 True, False를 1 또는 0으로 변환
accuracy = tf.reduce_mean(tf.cast(predicated_val, dtype=tf.float32))

#=============================
# 학습 시작
#=============================
with tf.compat.v1.Session() as sess:
    # 가장먼저 변수(tf.Variable) 초기화
    sess.run(tf.compat.v1.global_variables_initializer())

    for i in range(epochs):     # 100번 반복 수행
        total_batch = int(mnist.train.num_examples / batch_size)

        for step in range(total_batch):
            # 100개의 데이터를 임의로 뽑아서 사용
            batch_x_data, batch_y_data = mnist.train.next_batch(batch_size)

            loss_val, _ = sess.run([loss, train], feed_dict={X:batch_x_data, Y:batch_y_data})

            if step % 100 == 0:
                print("step : ", step, ", loss_val : ", loss_val)

    # 정확성 확인
    test_x_data = mnist.test.images
    test_y_data = mnist.test.labels

    accuracy_val = sess.run(accuracy, feed_dict={X:test_x_data, Y:test_y_data})

    print("정확도 :", accuracy_val)