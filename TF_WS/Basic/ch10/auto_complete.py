# 자연어 처리나 음성 처리 분야에 많이 사용되는 RNN 의 기본적인 사용법을 익힙니다.
# 4개의 글자를 가진 단어를 학습시켜, 3글자만 주어지면 나머지 한 글자를 추천하여 단어를 완성하는 프로그램입니다.

import tensorflow as tf
import numpy as np


char_arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# one-hot 인코딩 사용 및 디코딩을 하기 위해 연관 배열을 만듭니다.
# {'a': 0, 'b': 1, 'c': 2, ..., 'j': 9, 'k', 10, ...}
num_dic = {n: i for i, n in enumerate(char_arr)}
print('num_dic :', num_dic)
dic_len = len(num_dic)
print('dic_len :', dic_len)

# 학습할 단어 배열은 입력값과 출력값으로 다음처럼 사용할 것 입니다.
# wor -> X, d -> Y
# woo -> X, d -> Y
seq_data = ['word', 'wood', 'deep', 'dive', 'cold', 'cool', 'load', 'love', 'kiss', 'kind']

# 입력값과 실측값을 분리
def make_batch(seq_data):
    input_batch = []
    target_batch = []

    for seq in seq_data:
        # 여기서 생성하는 input_batch 와 target_batch는 알파벳 배열의 인덱스 번호 입니다.
        # [(w-22, o-14, r-17] [w-22, o-14, o-14] [3, 4, 4] [3, 8, 21] ...
        input = [num_dic[n] for n in seq[:-1]]
        print('input :',input)
        # d-3, d-3, p-15, 4, 3 ...
        target = num_dic[seq[-1]]
        print(target)
        # one-hot 인코딩을 합니다.
        # if input is [0, 1, 2]:
        # [[ 1.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
        #  [ 0.  1.  0.  0.  0.  0.  0.  0.  0.  0.]
        #  [ 0.  0.  1.  0.  0.  0.  0.  0.  0.  0.]]
        input_batch.append(np.eye(dic_len)[input])
        print('input_batch :', input_batch)

        # 지금까지 손실함수로 사용하던 softmax_cross_entropy_with_logits 함수는 label 값을 one-hot 인코딩으로 넘겨줘야 하지만,
        # 이 예제에서 사용할 손실 함수인 sparse_softmax_cross_entropy_with_logits는 one-hot 인코딩을 사용하지 않으므로 index를 그냥 넘겨주면 됩니다.
        target_batch.append(target)

    return input_batch, target_batch

#=========================
# 옵션 설정
#=========================
learning_rate = 0.01
n_hidden = 128
total_epoch = 30

# 타입 스텝: [1 2 3] => 3
# RNN 을 구성하는 시퀀스의 갯수입니다. 전체중에 3글자를 단계적으로 학습
n_step = 3

# 입력값 크기. 알파벳에 대한 one-hot 인코딩이므로 26개가 됩니다.
# 예) c => [0 0 1 0 0 0 0 0 0 0 0 ... 0]
# 출력값도 입력값과 마찬가지로 26개의 알파벳으로 분류합니다.
n_input = n_class = dic_len

#=========================
# 신경망 모델 구성
#=========================
X = tf.compat.v1.placeholder(tf.float32, [None, n_step, n_input])
# 비용함수에 sparse_softmax_cross_entropy_with_logits 을 사용하므로
# 출력값과의 계산을 위한 원본값의 형태는 one-hot vector가 아니라 인덱스 숫자를 그대로 사용하기 때문에
# 다음처럼 하나의 값만 있는 1차원 배열을 입력값으로 받습니다.
# [3] [3] [15] [4] ...
# 기존처럼 one-hot 인코딩을 사용한다면 입력값의 형태는 [None, n_class] 여야합니다.
Y = tf.compat.v1.placeholder(tf.int32, [None])      # batch_size에 해당하는 1차원만 존재

W = tf.Variable(tf.random.normal([n_hidden, n_class]))
b = tf.Variable(tf.random.normal([n_class]))

#===================================
# RNN 에 학습에 사용할 셀을 생성합니다
#===================================
# 다음 함수들을 사용하면 다른 구조의 셀로 간단하게 변경할 수 있습니다(BasicRNNCell,BasicLSTMCell,GRUCell)
# n_hidden 개의 출력값을 갖는 RNN 셀 생성
cell = tf.nn.rnn_cell.BasicRNNCell(n_hidden)

# 과적합 방지를 위한 Dropout 기법을 사용한다.
cell = tf.nn.rnn_cell.DropoutWrapper(cell, output_keep_prob=0.5)

# 여러개의 셀을 조합해서 사용하기 위해 셀을 추가로 생성합니다.
cell2 = tf.nn.rnn_cell.BasicLSTMCell(n_hidden)

# 여러개의 셀을 조합한 RNN 셀을 생성합니다.
multi_cell = tf.nn.rnn_cell.MultiRNNCell([cell, cell2])

#=================================================
# RNN 신경망 - 복잡한 과정을 dynamic_rnn으로 해결
# states = tf.zeros(batch_size)
# for i in range(n_step):
#   outputs, states = cell(X[[:, i]], states)
#=================================================
# RNN 셀, 입력값 --> 신경망 생성
outputs, states = tf.nn.dynamic_rnn(multi_cell, X, dtype=tf.float32)
print(outputs)      # Tensor("rnn/transpose_1:0", shape=(?, 3, 128), dtype=float32)

#===============================================
# 최종 출력값
# outputs의 형태는 (?, 28, 128) -->
# [batch_size, n_step, n_hidden] 형태
# outputs : [batch_size, n_step, n_hidden]
#        -> [n_step, batch_size, n_hidden]
#        -> [batch_size, n_hidden]
#===============================================
# 은닉층의 출력값을 가중치 W와 같은 형태로 만들어야 행렬곱 수행가능
# transpose로 위치 변경
outputs = tf.transpose(outputs, [1, 0, 2])  # [n_step, batch_size, n_hidden]
print(outputs)          # Tensor("transpose:0", shape=(3, ?, 128), dtype=float32)
# n_step 차원 제거
outputs = outputs[-1]   # [batch_size, n_hidden]
print(outputs)          # Tensor("strided_slice:0", shape=(?, 128), dtype=float32)

#===============================================
# 모델 생성
#===============================================
model = tf.matmul(outputs, W) + b
print(model)        # Tensor("add:0", shape=(?, 26), dtype=float32)

#
cost = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=model, labels=Y))
optimizer = tf.compat.v1.train.AdamOptimizer(learning_rate).minimize(cost)

#===============================================
# 신경망 학습과 결과 확인
#===============================================
init = tf.compat.v1.global_variables_initializer()
sess = tf.compat.v1.Session()
sess.run(init)

input_batch, target_batch = make_batch(seq_data)

print('\n학습이 시작되었습니다. 학습에 상당한 시간이 걸립니다....')
for epoch in range(total_epoch):
    c, _ = sess.run([cost, optimizer], feed_dict={X:input_batch, Y:target_batch})
    print('Epoch:', '%04d' % (epoch + 1), 'cost =', '{:.6f}'.format(c))

print('최적화 완료!')

#===============================================
# 결과 확인
#===============================================
# 레이블값이 정수이므로 예측값도 정수로 변경해줍니다.
prediction = tf.cast(tf.argmax(model, 1), tf.int32)

# one-hot 인코딩이 아니므로 입력값을 그대로 비교합니다.
prediction_check = tf.equal(prediction, Y)

accuracy = tf.reduce_mean(tf.cast(prediction_check, tf.float32))

input_batch, target_batch = make_batch(seq_data)

predict, accuracy_val = sess.run([prediction, accuracy], feed_dict={X: input_batch, Y: target_batch})

predict_words = []
for idx, val in enumerate(seq_data):
    last_char = char_arr[predict[idx]]
    predict_words.append(val[:3] + last_char)

print('\n=== 예측 결과 ===')
print('입력값:', [w[:3] + ' ' for w in seq_data])
print('예측값:', predict_words)
print('정확도:', accuracy_val)
