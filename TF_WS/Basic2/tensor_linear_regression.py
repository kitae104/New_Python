# Linear Regression 구현하기
import tensorflow as tf
import numpy as np

#============================
# 1. 데이터 분리
#============================
# 파일로부터 데이터 읽어오기
loaded_data = np.loadtxt('./data-01.csv', delimiter=',')

# 입력 데이터
x_data = loaded_data[ :, 0:-1]
print("x_data.shpe =", x_data.shape)

#정답 데이터
y_data = loaded_data[ :, [-1]]
print("y_data.shpe =", y_data.shape)

#=============================
# 2. 데이터 입력
#=============================
# 가중치 - 계속 업데이트 되어야하기 때문에 변수로 선언
W = tf.Variable(tf.random.normal([3,1]))

# 바이어스 설정 - 계속 업데이트 되어야하기 때문에 변수로 선언
b = tf.Variable(tf.random.normal([1]))

# 입력 데이터 - 외부에서 입력되기 때문에 플레이스홀더 사용
# 25대신 None을 사용한 이유는 25 X 3, 50 X 3 등 확장을 위해
X = tf.compat.v1.placeholder(tf.float32, [None, 3])

# 정답 데이터 - 외부에서 입력되기 때문에 플레이스홀더 사용
T = tf.compat.v1.placeholder(tf.float32, [None, 1])

#=============================
# 3. 선형 회귀
#=============================
y = tf.matmul(X, W) + b

#=============================
# 4. 손실함수
#=============================
loss = tf.reduce_mean(tf.square(y - T))

#=============================
# 5. 경사하강법 (최적화)
#=============================
learning_rate = 1e-5
optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=learning_rate)
train = optimizer.minimize(loss)    # 손실 함수 최소화

#=============================
# 6. 학습 시작
#=============================
with tf.compat.v1.Session() as sess:
    # 가장먼저 변수(tf.Variable) 초기화
    sess.run(tf.compat.v1.global_variables_initializer())

    for step in range(8001):
        loss_val, y_val, _ = sess.run([loss, y, train], feed_dict={X: x_data, T:y_data})

        if step % 400 == 0:
            print('step :', step, ", loss_val =", loss_val)


    # 예측
    print(" 성적 예측 :", sess.run(y, feed_dict={X:[[100, 98, 81]]}))

