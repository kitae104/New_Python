# 단순 선형 회귀 구현
import tensorflow as tf
import matplotlib.pyplot as plt
# tf.enable_eager_execution()     # 즉시 실행

# 데이터
x_data = [1, 2, 3, 4, 5]
y_data = [1, 2, 3, 4, 5]

# 변수(임의의 값 설정) --> W : 1 , b : 0 가 나와야 좋음.
W = tf.Variable(2.9)    # 초기값 지정
b = tf.Variable(0.5)    # 임의의 값으로 지정 가능

learning_rate = 0.01    # 학습률 - 기울기 반영을 위해 사용

for i in range(100+1):  # W, b 업데이트
    # Gradient descent
    with tf.GradientTape() as tape:
        # 가설
        hypothesis = W * x_data + b
        # 비용함수
        cost = tf.reduce_mean(tf.square(hypothesis - y_data))   # reduce는 차원이 줄어든다는 의미

    # 각각 W와 b 기울기 계산
    W_grad, b_grad = tape.gradient(cost, [W, b])

    # W와 b 값 업데이트
    W.assign_sub(learning_rate * W_grad)    # A -= B
    b.assign_sub(learning_rate * b_grad)

    if i % 10 == 0:
        print("{:5}|{:10.4f}|{:10.4f}|{:10.6f}".format(i, W.numpy(), b.numpy(), cost))

plt.plot(x_data, y_data, 'o')
plt.plot(x_data, hypothesis.numpy(), 'g-')
plt.xlim(0, 8)
plt.ylim(0, 8)
plt.show()

# 테스트
print(W * 5 + b)
print(W * 2.5 + b)


