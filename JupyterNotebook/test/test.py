import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf
print(tf.__version__)

# 학습에 사용할 데이터
x_train = [[1., 2.],
          [2., 3.],
          [3., 1.],
          [4., 3.],
          [5., 3.],
          [6., 2.]]

# 정답 데이터
y_train = [[0.],
          [0.],
          [0.],
          [1.],
          [1.],
          [1.]]

# 테스트 데이터와 테스트 정답
x_test = [[5.,2.]]
y_test = [[1.]]

# x축 데이터 추출
x1 = [x[0] for x in x_train]
x2 = [x[1] for x in x_train]

colors = [int(y[0]) for y in y_train]

## 그래프 그리기
plt.scatter(x1, x2, c=colors, marker='^')           # 0과 1을 구분하여 출력
plt.scatter(x_test[0][0], x_test[0][1], c='red')    # 테스트 데이터 출력
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()

dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train)).batch(len(x_train))  # 데이터 셋 준비

W = tf.Variable(tf.zeros([2,1]), name = 'weight')
b = tf.Variable(tf.zeros([1]), name = 'bias')

# 1. Sigmoid 함수를 가설로 선언
def logistic_regression(x):
    hypothesis = tf.divide(1., 1. + tf.exp(tf.matmul(x, W) + b))
    return hypothesis

# 2. 가설을 검증할 Cost 함수를 정의¶
def loss_fn(hypothesis, x, y):
    cost = -tf.reduce_mean(y * tf.math.log(logistic_regression(x)) + (1 - y) * tf.math.log(1-hypothesis))
    return cost

# 3. 정확도를 계산할 Accuracy 함수 정의
def accuracy_fn(hypothesis, y):
    predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
    accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, y), dtype=tf.int32))
    return accuracy

# 4. GradientTape를 통한 Grad(경사값 계산) 함수
def grad(x, y):
    with tf.GradientTape() as tape:
        loss_value = loss_fn(logistic_regression(x), x, y)
    return tape.gradient(loss_value, [W, b])

## 학습 실행
optimizer = tf.keras.optimizers.SGD(learning_rate=0.01)

EPOCHS = 1001

for step in range(EPOCHS):
    for x, y in iter(dataset):
        grads = grad(x, y)   # 기울기 계산
        optimizer.apply_gradients(grads_and_vars=zip(grads, [W,b])) # 기울기 적용
        if step % 100 == 0:
            print("iter : {}, Loss : {:.4f}".format(step, loss_fn(logistic_regression(x), x, y)))

test_acc = accuracy_fn(logistic_regression(x_test), y_test)
print("Test Accuracy : {:.4f}".format(test_acc))