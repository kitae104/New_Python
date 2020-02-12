# 기본적인 RNN 수행하기
import tensorflow as tf
from tensorflow.models.rnn import rnn, rnn_cell
tf.disable_v2_behavior()
import numpy as np

char_rdic = ['h', 'e', 'l', 'o']
char_dic = { w : i for i, w in enumerate(char_rdic)}  # char -> id
print(char_dic)

x_data = np.array([[1,0,0,0],   # h
                    [0,1,0,0],  # e
                    [0,0,1,0],  # l
                    [0,0,1,0]], # l
                  dtype='f')

sample = [char_dic[c] for c in 'hello']  # to index
print(sample)

# 설정
char_vocab_size = len(char_dic)
rnn_size = char_vocab_size      # one hot coding(one of 4)
state_size = 0
time_step_size = 4  # hell -> predict ello
batch_size = 1      # one sample

# # RNN model
rnn_cell = rnn_cell.BasicRNNCell(rnn_size)   # rnn_size는 output 사이즈와 관련
# rnn_cell = rnn_cell.BasicLSTMCell(rnn_size)   # rnn_size는 output 사이즈와 관련
# rnn_cell = rnn_cell.BasicGRUCell(rnn_size)   # rnn_size는 output 사이즈와 관련

state = tf.zeros([batch_size, rnn_cell, state_size])    # 초기엔 0 , state_size : rnn의 사이즈
X_split = tf.split(0, time_step_size, x_data)

outputs, state = rnn.rnn(rnn_cell, X_split, state)  # X_split : 사용할 벡터들의 갯수

# Cost
logits = tf.reshape(tf.concat(1, outputs), [-1, rnn_size]) # 예측값,  -1은 n개라는 의미
targets = tf.reshape(sample[1:],[-1])
weights = tf.ones([time_step_size * batch_size])

# 학습
loss = tf.nn.seq2seq.sequence_loss_by_example([logits], [targets], [weights])
cost = tf.reduce_sum(loss)/batch_size

# 최적화
train_op = tf.train.RMSPropOptimizer(0.01, 0.9).minimize(cost)

with tf.Session() as sess:
    tf.initialize_all_variables().run()

    for i in range(100):
        sess.run(train_op)
        result = sess.run(tf.arg_max(logits, 1))
        print(result, [char_rdic[t] for t in result])
