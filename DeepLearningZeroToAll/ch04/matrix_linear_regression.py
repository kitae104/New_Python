# 다중 변수를 이용한 선형 회귀
import tensorflow as tf

# 다양한 종류의 변수
x_data = [[73., 80., 75.],
          [93., 88., 93.],
          [89., 91., 90.],
          [96., 98., 100.],
          [73., 66., 70.]]
y_data = [[152.],
          [185.],
          [180.],
          [196.],
          [142.]]

X = tf.placeholder(tf.float32, shape=[None, 3])
Y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([3, 1]), name="weight")
b = tf.Variable(tf.random_normal([1]), name="bias")

#hypothesis = X * W + b
hypothesis = tf.matmul(X, W) + b

# cost
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# optimizer
optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train = optimizer.minimize(cost)

# RUN
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train], feed_dict={X:x_data, Y:y_data})

    if step % 10 == 0:
        print(step, "Cost : ", cost_val, "\nPrediction:\n", hy_val)
