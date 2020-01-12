import tensorflow as tf

print(tf.__version__)
hello = tf.constant("Hello, TensorFlow!")

sess = tf.Session()
print(sess.run(hello))

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)
node3 = tf.add(node1, node2)

print("node1:", node1, "node2:", node2)
print("node3:", node3)

print(sess.run([node1, node2]))
print(sess.run(node3))

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b
print(sess.run(adder_node, feed_dict={a:3, b:4.5}))
print(sess.run(adder_node, feed_dict={a:[1,2,3], b:[1,2,3]}))

add_and_triple = adder_node * 3
print(sess.run(add_and_triple, feed_dict={a:3, b:4.5}))

v =[1., 2., 3., 4.]
mean = tf.reduce_mean(v) # 2.5
print(sess.run(mean))

square = tf.square(3)   # 9
print(sess.run(square))