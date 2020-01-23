# tf.cast 연습하기
import tensorflow as tf

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    # 실수형 --> 정수형
    x = tf.constant([1.9, 2.1], dtype=tf.float32)
    print(sess.run(x))
    x = tf.cast(x, tf.int32)
    print(sess.run(x))

    # 불린형 --> 정수형
    x = tf.constant([True, False])
    print(sess.run(x))
    x = tf.cast(x, tf.int32)
    print(sess.run(x))

    # 불린형 --> 정수형
    x = tf.constant([True, False], dtype=tf.float32)
    print(sess.run(x))
    x = tf.cast(x, tf.int32)
    print(sess.run(x))

    # 실수형 --> 불린형
    # 불린형 --> 정수형
    x = tf.constant([1.9, 2.1], dtype=tf.float32)
    print(sess.run(x))
    x = tf.cast(x>=2.0, tf.int32)
    print(sess.run(x))