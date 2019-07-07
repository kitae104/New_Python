# RNN을 softmax를 이용하여 긴문장 처리하기
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
import numpy as np
from tensorflow.contrib import rnn

tf.compat.v1.set_random_seed(777)  # 재현성

sentence = (" if you want to build a ship, don't drum up people together to "
            "collect wood and don't assign them tasks and work, but rather "
            "teach them to long for the endless immensity of the sea.")
print('전체 문장 길이 :',len(sentence))

# 중복 문자 제거후 리스트 만들기
char_set= list(set(sentence))
print(char_set) # 수행할 때마다 바뀜

# 문자와 인덱스 확인하기
char_dic = {c: i for i, c in enumerate(char_set)}
print(char_dic) # 문자와 인덱스 형태로 출력

# 하이퍼 파라미터
data_dim = len(char_set)            # RNN 입력 크기 (one hot size)
print('data_dim :', data_dim)
hidden_size = len(char_set)         # RNN 출력 크기
print('hidden_size :', hidden_size)
num_classes = len(char_set)         # 최종 출력 크기(RNN or softmax, etc.) --> 유일한 문자의 갯수
print('num_classes :',num_classes)
sequence_length = 10                # 임의의 문자 길이
print('sequence_length :', sequence_length)
learning_rate = 0.1

x_data = []  # X data sample (0 ~ n-1) hello: hell
y_data = []  # Y label sample (1 ~ n) hello: ello

for i in range(0, len(sentence) - sequence_length):
    x_str = sentence[i:i+sequence_length]
    y_str = sentence[i+1:i+sequence_length+1]
    print(i, x_str, '->', y_str)

    x = [char_dic[c] for c in x_str]    # x는 x_str을 인덱스로 처리
    print('x :', x)
    y = [char_dic[c] for c in y_str]    # y는 y_str을 인덱스로 처리
    print('y :', y)

    x_data.append(x)
    print('x_data :', x_data)
    y_data.append(y)
    print('y_data :', y_data)

batch_size = len(x_data)
print('batch_size :', batch_size)

X = tf.compat.v1.placeholder(tf.int32, [None, sequence_length])     # X data
print(X)    # Tensor("Placeholder:0", shape=(?, 10), dtype=int32)
Y = tf.compat.v1.placeholder(tf.int32, [None, sequence_length])     # Y label
print(Y)    # Tensor("Placeholder_1:0", shape=(?, 10), dtype=int32)

x_one_hot = tf.one_hot(X, num_classes)  # one hot 형태 : 1 -> 0 1 0 0 0 0 0 0 0 0
print(x_one_hot)            # Tensor("one_hot:0", shape=(?, 10, 25), dtype=float32)

# Cell 생성
# def lstm_cell():
#     cell = tf.contrib.rnn.BasicLSTMCell(num_units=hidden_size, state_is_tuple=True)
#     print(cell)     # <tensorflow.python.ops.rnn_cell_impl.BasicLSTMCell object at 0x0000026266BBD048>
#     return cell
#
# multi_cells = rnn.MultiRNNCell([lstm_cell() for _ in range(2)], state_is_tuple=True)

cell = rnn.BasicLSTMCell(num_units=hidden_size, state_is_tuple=True)
multi_cells = rnn.MultiRNNCell([cell] * 2, state_is_tuple=True)

outputs, _states = tf.nn.dynamic_rnn(multi_cells, x_one_hot, dtype=tf.float32)
print('outputs :', outputs)  # Tensor("rnn/transpose_1:0", shape=(?, 10, 25), dtype=float32)

# softmax layer
ouputs = tf.reshape(outputs, [batch_size, sequence_length, num_classes])
x_for_softmax = tf.reshape(outputs, [-1, hidden_size])
print('X_for_softmax :', x_for_softmax) # Tensor("Reshape:0", shape=(?, 25), dtype=float32)

softmax_w = tf.get_variable("softmax_w", [hidden_size, num_classes])
softmax_b = tf.get_variable("softmax_b", [num_classes])

outputs = tf.matmul(x_for_softmax, softmax_w) + softmax_b

# reshape out for sequence_loss
outputs = tf.reshape(outputs, [batch_size, sequence_length, num_classes])
print('outputs :', outputs)  # Tensor("Reshape_1:0", shape=(170, 10, 25), dtype=float32)

weights = tf.ones([batch_size, sequence_length])    # 모두 1로 설정
print('weights :', weights)  # Tensor("ones:0", shape=(170, 10), dtype=float32)

# sequence cost/loss 계산 하기
sequence_loss = tf.contrib.seq2seq.sequence_loss(logits=outputs, targets=Y, weights=weights)
print('sequence_loss :', sequence_loss)  # Tensor("sequence_loss/div_no_nan:0", shape=(), dtype=float32)

loss = tf.reduce_mean(sequence_loss)
print('loss :', loss)   # Tensor("Mean:0", shape=(), dtype=float32)

train = tf.compat.v1.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)

prediction = tf.argmax(outputs, axis=2)

with tf.compat.v1.Session() as sess:                            # 세션 생성
    sess.run(tf.compat.v1.global_variables_initializer())       # 변수 초기화

    for i in range(1000):                                       # 3000번 수행
        _, l, results = sess.run([train, loss, outputs], feed_dict={X: x_data, Y: y_data})

        for j, result in enumerate(results):
            index = np.argmax(result, axis=1)
            print(i, j, ''.join([char_set[t] for t in index]), l)

    results = sess.run(outputs, feed_dict={X: x_data})

    for j, result in enumerate(results):
        index = np.argmax(result, axis=1)
        if j is 0:  # print all for the first result to make a sentence
            print(''.join([char_set[t] for t in index]), end='')
        else:
            print(char_set[index[-1]], end='')