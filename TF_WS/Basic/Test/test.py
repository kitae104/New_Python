import tensorflow as tf

# 그래프 생성
node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)
node3 = tf.add(node1, node2)

print('node1 : ', node1, "node2 : ", node2)
print('node3 : ', node3)

# 세션 생성
sess = tf.Session()

# 그래프 수행
print("sess.run(node1, node2) : ", sess.run([node1, node2]))
print("sess.run(node3) : ", sess.run(node3))

# 값을 설정해서 처리하기
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
add_node = a + b

print(sess.run(add_node, feed_dict={a:3, b:4.5}))
print(sess.run(add_node, feed_dict={a:[1,3], b:[2,4]}))