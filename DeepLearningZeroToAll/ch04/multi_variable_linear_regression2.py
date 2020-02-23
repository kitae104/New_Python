# 다중 변수를 이용한 선형 회귀2
import tensorflow as tf

# 데이터와 라벨
x1 = [73., 93., 89., 96., 73.]
x2 = [80., 88., 91., 98., 66.]
x3 = [75., 93., 90., 100., 70.]
Y = [152., 185., 180., 196., 142.]      # 결과

# 가중치와 편향
w1 = tf.Variable(tf.random.normal([1]), name="weight1")
w2 = tf.Variable(tf.random.normal([1]), name="weight2")
w3 = tf.Variable(tf.random.normal([1]), name="weight3")
b = tf.Variable(tf.random.normal([1]), name="bias")

# 학습률
learning_rate = 0.000001

# 실행
for i in range(1000+1):
    with tf.GradientTape() as tape:
        # 가설
        hypothesis = x1 * w1 + x2 * w2 + x3 * w3 + b
        # cost
        cost = tf.reduce_mean(tf.square(hypothesis - Y))

    # 비용에 대한 기울기 계산
    w1_grad, w2_grad, w3_grad, b_grad = tape.gradient(cost, [w1, w2, w3, b])

    # 가중치와 편향 갱신
    w1.assign_sub(learning_rate * w1_grad)
    w2.assign_sub(learning_rate * w2_grad)
    w3.assign_sub(learning_rate * w3_grad)
    b.assign_sub(learning_rate * b_grad)

    if i % 50 == 0:
        print("{:5} | {:12.4f}".format(i, cost.numpy()))    # 비용값 확인
