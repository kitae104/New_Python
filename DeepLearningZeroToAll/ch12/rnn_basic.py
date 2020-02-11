import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
import numpy as np
from tensorflow.contrib import rnn
import pprint

pp = pprint.PrettyPrinter(indent=4)
sess = tf.compat.v1.InteractiveSession()

# One hot encoding으로 'hello'를 설정
h = [1, 0, 0, 0]
e = [0, 1, 0, 0]
l = [0, 0, 1, 0]
o = [0, 0, 0, 1]

print('\n================one_cell============================\n')
with tf.variable_scope('one_cell') as scope:
    # One cell RNN input_dim (4) -> output_dim (2)
    hidden_size = 2
    #cell = tf.keras.layers.SimpleRNNCell(units=hidden_size)
    cell = tf.contrib.rnn.BasicLSTMCell(num_units=hidden_size)
    # cell = rnn.GRUCell(num_units=hidden_size)
    print(cell.output_size, cell.state_size)

    x_data = np.array([[h]], dtype=np.float32) # x_data = [[[1,0,0,0]]]
    pp.pprint(x_data)
    outputs, _states = tf.nn.dynamic_rnn(cell, x_data, dtype=tf.float32)

    sess.run(tf.compat.v1.global_variables_initializer())
    pp.pprint(outputs.eval())

print('\n================two_sequances============================\n')
with tf.variable_scope('two_sequances') as scope:
    # One cell RNN input_dim (4) -> output_dim (2). sequence: 5
    hidden_size = 2
    # cell = tf.keras.layers.SimpleRNNCell(units=hidden_size)
    cell = tf.contrib.rnn.BasicLSTMCell(num_units=hidden_size)

    x_data = np.array([[h, e, l, l, o]], dtype=np.float32)
    print(x_data.shape)
    pp.pprint(x_data)

    outputs, _states = tf.nn.dynamic_rnn(cell, x_data, dtype=tf.float32)
    sess.run(tf.compat.v1.global_variables_initializer())
    pp.pprint(outputs.eval())

print('\n================3_batches============================\n')
with tf.variable_scope('3_batches') as scope:
    # One cell RNN input_dim (4) -> output_dim (2). sequence: 5, batch 3
    # 3 batches 'hello', 'eolll', 'lleel'
    x_data = np.array([[h, e, l, l, o],
                       [e, o, l, l, l],
                       [l, l, e, e, l]], dtype=np.float32)
    pp.pprint(x_data)

    hidden_size = 2
    # cell = tf.nn.rnn_cell.LSTMCell(num_units=hidden_size, state_is_tuple=True)
    cell = tf.contrib.rnn.BasicLSTMCell(num_units=hidden_size, state_is_tuple=True)
    outputs, _states = tf.nn.dynamic_rnn(cell, x_data, dtype=tf.float32)
    sess.run(tf.compat.v1.global_variables_initializer())
    pp.pprint(outputs.eval())

print('\n============3_batches_dynamic_length==================\n')
with tf.variable_scope('3_batches_dynamic_length') as scope:
    # One cell RNN input_dim (4) -> output_dim (5). sequence: 5, batch 3
    # 3 batches 'hello', 'eolll', 'lleel'
    x_data = np.array([[h, e, l, l, o],
                       [e, o, l, l, l],
                       [l, l, e, e, l]], dtype=np.float32)
    pp.pprint(x_data)

    hidden_size = 2
    # tf.keras.layers.LSTMCell
    cell = tf.nn.rnn_cell.LSTMCell(num_units=hidden_size, state_is_tuple=True)
    outputs, _states = tf.nn.dynamic_rnn(cell, x_data, sequence_length=[5, 3, 4], dtype=tf.float32)
    sess.run(tf.compat.v1.global_variables_initializer())
    pp.pprint(outputs.eval())

print('\n==================initial_state========================\n')
with tf.variable_scope('initial_state') as scope:
    batch_size = 3
    x_data = np.array([[h, e, l, l, o],
                       [e, o, l, l, l],
                       [l, l, e, e, l]], dtype=np.float32)
    pp.pprint(x_data)

    # One cell RNN input_dim (4) -> output_dim (5). sequence: 5, batch: 3
    hidden_size = 2
    cell = tf.nn.rnn_cell.LSTMCell(num_units=hidden_size, state_is_tuple=True)
    initial_state = cell.zero_state(batch_size, tf.float32)
    outputs, _states = tf.nn.dynamic_rnn(cell, x_data, initial_state=initial_state, dtype=tf.float32)
    sess.run(tf.compat.v1.global_variables_initializer())
    pp.pprint(outputs.eval())