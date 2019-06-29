import os
import logging

# 경고 제거를 위해 사용
logging.disable(logging.WARNING)

# CPU 경고 제거
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf

hello = tf.constant('Hello, Tensorflow!')
print(hello)
# Tensor("Const:0", shape=(), dtype=string)

a = tf.constant(10)
b = tf.constant(32)
c = tf.add(a, b)
print(c)
# Tensor("Add:0", shape=(), dtype=int32)

sess = tf.compat.v1.Session()
#sess = tf.Session()

print(sess.run(hello))
print(sess.run([a, b, c]))

sess.close()