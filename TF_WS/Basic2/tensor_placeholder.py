# 플레이스홀더 사용하기 --> 입력 데이터와 정답 데이터를 입력하기 위해 사용 
import tensorflow as tf

#플레이스홀더 노드 정의
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
c = a + b
print(a)
print(b)
print(c)

# 세션을 만들고 플레이스홀더 노드를 통해 값 입력 받음
sess = tf.compat.v1.Session()

print(sess.run(c, feed_dict={a:1.0, b:3.0}))
print(sess.run(c, feed_dict={a:[1.0, 2.0], b:[3.0, 4.0]}))

# 연산 추가
d = 100 * c

print(sess.run(d, feed_dict={a:1.0, b:3.0}))
print(sess.run(d, feed_dict={a:[1.0, 2.0], b:[3.0, 4.0]}))

sess.close()