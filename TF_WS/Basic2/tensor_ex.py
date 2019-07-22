import tensorflow as tf

# 추후에 데이터 입력으로 사용
X = tf.compat.v1.placeholder(tf.float32, [None, 3])

x_data = [[1,2,3], [4,5,6]]

# 변수 : 텐서가 스스로 학습시킨
W = tf.Variable(tf.random.normal([3,2]))
b = tf.Variable(tf.random.normal([2,1]))

expr = tf.matmul(X, W) + b

print (expr)

sess = tf.compat.v1.Session()

sess.run(tf.compat.v1.global_variables_initializer())

print(sess.run(W))
print(sess.run(b))
print(sess.run(expr, feed_dict={X:x_data}))