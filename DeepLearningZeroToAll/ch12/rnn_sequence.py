# RNN 데이터 입력 자동화 하기
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
import numpy as np
tf.compat.v1.set_random_seed(777)  # 재현성

sample = " if you want you"

# 중복 문자 제거후 리스트 만들기
idx2char = list(set(sample))
print(idx2char) # ['a', 'i', 'n', 'w', 'f', ' ', 't', 'u', 'o', 'y'] --> 수행할 때마다 바뀜

# 문자와 인덱스 확인하기
char2idx = {c: i for i, c in enumerate(idx2char)}
print(char2idx) # {'a': 0, 'i': 1, 'n': 2, 'w': 3, 'f': 4, ' ': 5, 't': 6, 'u': 7, 'o': 8, 'y': 9}

# 하이퍼 파라미터
dic_size = len(char2idx)            # RNN 입력 크기 (one hot size)
print('dic_size :', dic_size)
hidden_size = len(char2idx)         # RNN 출력 크기
print('hidden_size :', hidden_size)
num_classes = len(char2idx)         # 최종 출력 크기(RNN or softmax, etc.) --> 유일한 문자의 갯수
print('num_classes :',num_classes)
batch_size = 1                      # 샘플 데이터 갯수
sequence_length = len(sample) - 1   # 전체 문자열의 길이 (number of lstm rollings (unit #))
print('sequence_length :', sequence_length)
learning_rate = 0.1

sample_idx = [char2idx[c] for c in sample]  # 문자를 인덱스로
print(sample_idx)   # [5, 1, 4, 5, 9, 8, 7, 5, 3, 0, 2, 6, 5, 9, 8, 7]
x_data = [sample_idx[:-1]]  # X data sample (0 ~ n-1) hello: hell
y_data = [sample_idx[1:]]   # Y label sample (1 ~ n) hello: ello

X = tf.compat.v1.placeholder(tf.int32, [None, sequence_length])     # X data
Y = tf.compat.v1.placeholder(tf.int32, [None, sequence_length])     # Y label

x_one_hot = tf.one_hot(X, num_classes)  # one hot: 1 -> 0 1 0 0 0 0 0 0 0 0
print(x_one_hot)            # Tensor("one_hot:0", shape=(?, 15, 10), dtype=float32)

# Cell 생성
cell = tf.contrib.rnn.BasicLSTMCell(num_units=hidden_size, state_is_tuple=True)
print(cell)     # <tensorflow.python.ops.rnn_cell_impl.BasicLSTMCell object at 0x0000026266BBD048>
initial_state = cell.zero_state(batch_size, tf.float32)
print(initial_state)    # LSTMStateTuple(c=<tf.Tensor 'BasicLSTMCellZeroState/zeros:0' shape=(1, 10) dtype=float32>, h=<tf.Tensor 'BasicLSTMCellZeroState/zeros_1:0' shape=(1, 10) dtype=float32>)
outputs, _states = tf.nn.dynamic_rnn(cell, x_one_hot, initial_state=initial_state, dtype=tf.float32)
print(outputs)  # Tensor("rnn/transpose_1:0", shape=(1, 15, 10), dtype=float32)

# FC layer
X_for_fc = tf.reshape(outputs, [-1, hidden_size])
print(X_for_fc) # Tensor("Reshape:0", shape=(15, 10), dtype=float32)
outputs = tf.contrib.layers.fully_connected(inputs=X_for_fc, num_outputs=num_classes, activation_fn=None)
print(outputs)  # Tensor("fully_connected/BiasAdd:0", shape=(15, 10), dtype=float32)

# reshape out for sequence_loss
outputs = tf.reshape(outputs, [batch_size, sequence_length, num_classes])
weights = tf.ones([batch_size, sequence_length])    # 모두 1로 설정
sequence_loss = tf.contrib.seq2seq.sequence_loss(logits=outputs, targets=Y, weights=weights)

loss = tf.reduce_mean(sequence_loss)
train = tf.compat.v1.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)
prediction = tf.argmax(outputs, axis=2)

with tf.compat.v1.Session() as sess:                            # 세션 생성
    sess.run(tf.compat.v1.global_variables_initializer())       # 변수 초기화

    for i in range(50):                                       # 3000번 수행
        l, _ = sess.run([loss, train], feed_dict={X: x_data, Y: y_data})
        result = sess.run(prediction, feed_dict={X: x_data})
        print(i, "loss : ", l, "prediction : ", result, "true Y : ", y_data)

        result_str = [idx2char[c] for c in np.squeeze(result)]
        print("\tPrediction str : ", ''.join(result_str))