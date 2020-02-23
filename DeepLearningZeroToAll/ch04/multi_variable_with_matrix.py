# 다중 변수를 이용한 선형 회귀 with matrix
import tensorflow as tf
import numpy as np

# 데이터와 라벨
data = np.array([
    [73., 93., 89., 96., 73.],
    [80., 88., 91., 98., 66.],
    [75., 93., 90., 100., 70.],
    [152., 185., 180., 196., 142.]
    ], dtype=np.float32)

data = data.T

# 데이터 슬라이스 - 매트릭스 활용
X = data[:, :-1]    # 행, 열
print(X.shape)
Y = data[:, [-1]]
print(Y.shape)

# 가중치와 편향 - 매트릭스 활용
W = tf.Variable(tf.random.normal([3, 1]))
b = tf.Variable(tf.random.normal([1]))

def predict(X):
    return tf.matmul(X, W) + b

# 학습률
learning_rate = 0.000001
n_epochs = 2000

# 실행
for i in range(n_epochs+1):
    with tf.GradientTape() as tape:
        # cost
        cost = tf.reduce_mean((tf.square(predict(X) - Y)))

    # 비용에 대한 기울기 계산 - 매트릭스 활용
    W_grad, b_grad = tape.gradient(cost, [W, b])

    # 가중치와 편향 갱신
    W.assign_sub(learning_rate * W_grad)
    b.assign_sub(learning_rate * b_grad)

    if i % 100 == 0:
        print("{:5} | {:10.4f}".format(i, cost.numpy()))    # 비용값 확인
