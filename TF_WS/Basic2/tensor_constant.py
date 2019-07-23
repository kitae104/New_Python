# 텐서플로우 상수
import tensorflow as tf

# 상수 노드 정의
a = tf.constant(1.0, name='a')
b = tf.constant(2.0, name='b')
c = tf.constant([[1.0, 2.0], [3.0, 4.0]])

# 노드의 상태 출력
print(a)
print(a + b)
print(c)

# 세션 (노드간의 연산을 위해 세션 생성)
sess = tf.compat.v1.Session()

print(sess.run(a))
print(sess.run(b))
print(sess.run(c))
print(sess.run([a, b]))
print(sess.run([a + b]))
print(sess.run(c + 1.0))

sess.close()