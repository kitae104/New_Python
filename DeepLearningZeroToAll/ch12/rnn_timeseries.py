# RNN을 이용하여 Time Series 데이터 처리하기
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.contrib import rnn

tf.compat.v1.set_random_seed(777)  # 재현성

def MinMaxScaler(data):
    numerator = data - np.min(data, 0)
    denominator = np.max(data, 0) - np.min(data, 0)
    return numerator / (denominator + 1e-7)

# 학습에 사용되는 파라미터
seq_length = 7          # 7일
data_dim = 5            # 5개의 항목
hidden_dim = 10         #
output_dim = 1          # 출력 크기
learning_rate = 0.01
iterations = 500        # 반복 횟수

# 5개의 항목 Open, High, Low, Volume, Close 순서
xy = np.loadtxt('data-stock_daily.csv', delimiter=',')
print('xy1 :', xy)
xy = xy[::-1]
print('xy2 :', xy)
xy = MinMaxScaler(xy)
print('xy :', xy)

x = xy
print('x :', x)
y = xy[:, [-1]]
print('y :', y)

# 데이터셋(dataset) 만들기
x_data = []
y_data = []

for i in range(0, len(y) - seq_length):
    _x = x[i:i+seq_length]
    _y = y[i+seq_length]
    print(i, _x, '->', _y)

    x_data.append(_x)
    #print('x_data :', x_data)
    y_data.append(_y)
    #print('y_data :', y_data)

# 학습과 테스트로 분리하기
train_size = int(len(y_data) * 0.7)
print('train_size :',train_size)
test_size = len(y_data) - train_size
print('test_size :',test_size)

trainX, testX = np.array(x_data[0:train_size]), np.array(x_data[train_size:len(x_data)])
trainY, testY = np.array(y_data[0:train_size]), np.array(y_data[train_size:len(y_data)])

# 입력 플레이스 홀더
X = tf.compat.v1.placeholder(tf.float32, [None, seq_length, data_dim])      # X data
Y = tf.compat.v1.placeholder(tf.float32, [None, 1])                         # Y label

# LSTM network 구성하기
cell = rnn.BasicLSTMCell(num_units=hidden_dim, state_is_tuple=True, activation=tf.tanh)
outputs, _states = tf.nn.dynamic_rnn(cell, X, dtype=tf.float32)

# 마지막 셀의 아웃풋을 사용
Y_pred = tf.contrib.layers.fully_connected(inputs=outputs[:,-1], num_outputs=output_dim, activation_fn=None)
print(Y_pred)      # Tensor("fully_connected/BiasAdd:0", shape=(?, 1), dtype=float32)

# cost/loss와 optimizer 구하기
loss = tf.reduce_sum(tf.square(Y_pred - Y))
optimizer = tf.train.AdamOptimizer(learning_rate)
train = optimizer.minimize(loss)

# # RMSE
targets = tf.placeholder(tf.float32, [None, 1])
predictions = tf.placeholder(tf.float32, [None, 1])
rmse = tf.sqrt(tf.reduce_mean(tf.square(targets - predictions)))

with tf.compat.v1.Session() as sess:                            # 세션 생성
    sess.run(tf.compat.v1.global_variables_initializer())       # 변수 초기화

    # 학습 단계
    for i in range(iterations):                                 # 500번 수행
        _, step_lose = sess.run([train, loss], feed_dict={X: trainX, Y: trainY})
        print('[step: {}] loss : {}'.format(i, step_lose))

    # 테스트 단계
    test_predict = sess.run(Y_pred, feed_dict={X: testX})
    rmse_val = sess.run(rmse, feed_dict={targets: testY, predictions: test_predict})

    print("RMSE : {}".format(rmse_val))

    plt.plot(testY)
    plt.plot(test_predict)
    plt.xlabel("Time Period")
    plt.ylabel("Stock Price")
    plt.show()