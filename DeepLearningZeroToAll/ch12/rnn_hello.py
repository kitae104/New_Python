# RNN 사용하기
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
import numpy as np
tf.compat.v1.set_random_seed(777)  # 재현성

# 문자에 대한 인덱스 설정
idx2char = ['h', 'i', 'e', 'l', 'o']

x_data = [[0, 1, 0, 2, 3, 3]]       # hihell

# x_data를 원핫 형태로 변환
x_one_hot = [[[1, 0, 0, 0, 0],      # h 0
              [0, 1, 0, 0, 0],      # i 1
              [1, 0, 0, 0, 0],      # h 0
              [0, 0, 1, 0, 0],      # e 2
              [0, 0, 0, 1, 0],      # l 3
              [0, 0, 0, 1, 0]]]     # l 3

y_data = [[1, 0, 2, 3, 3, 4]]       # ihello

num_classes = 5
input_dim = 5           # 입력 차수(one-hot size) --> [1, 0, 0, 0, 0]
hidden_size = 5         # 출력 output from the LSTM. 5 to directly predict one-hot
batch_size = 1          # 하나의 문장이면 1
sequence_length = 6     # 시퀀스 길이 --> |ihello| == 6
learning_rate = 0.1

X = tf.compat.v1.placeholder(tf.float32, [None, sequence_length, input_dim])  # one-hot 형태
Y = tf.compat.v1.placeholder(tf.int32, [None, sequence_length])               # label

cell = tf.contrib.rnn.BasicLSTMCell(num_units=hidden_size, state_is_tuple=True)
initial_state = cell.zero_state(batch_size, tf.float32)
outputs, _states = tf.nn.dynamic_rnn(cell, X, initial_state=initial_state, dtype=tf.float32)

#=======================
# FC layer
#=======================
X_for_fc = tf.reshape(outputs, [-1, hidden_size])
outputs = tf.contrib.layers.fully_connected(inputs=X_for_fc, num_outputs=num_classes, activation_fn=None)

# reshape out for sequence_loss
outputs = tf.reshape(outputs, [batch_size, sequence_length, num_classes])
weights = tf.ones([batch_size, sequence_length])    # 1로 설정
sequence_loss = tf.contrib.seq2seq.sequence_loss(logits=outputs, targets=Y, weights=weights)

loss = tf.reduce_mean(sequence_loss)
train = tf.compat.v1.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)
prediction = tf.argmax(outputs, axis=2)

with tf.compat.v1.Session() as sess:
    sess.run(tf.compat.v1.global_variables_initializer())

    for i in range(50):
        l, _ = sess.run([loss, train], feed_dict={X: x_one_hot, Y: y_data})
        result = sess.run(prediction, feed_dict={X: x_one_hot})
        print(i, "loss : ", l, "prediction : ", result, "true Y : ", y_data)

        result_str = [idx2char[c] for c in np.squeeze(result)]
        print("\tPrediction str : ", ''.join(result_str))