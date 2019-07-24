# Logistic Regression(로지스틱 회귀) 구현하기
import tensorflow as tf
import numpy as np

# 당뇨병 정보 데이터
loaded_data = np.loadtxt('./data-02.csv', delimiter=',')

# 입력 데이터 [ 모든 행 , 0~마지막 전 열]
x_data = loaded_data[ :, 0:-1]
print("x_data.shpe =", x_data.shape)

#정답 데이터 [모든 행, 마지막 1열]
y_data = loaded_data[ :, [-1]]
print("y_data.shpe =", y_data.shape)

#=============================
# 2. 데이터 입력
#=============================
# 입력 데이터 - 외부에서 입력되기 때문에 플레이스홀더 사용 --> 데이터 8개
# 759대신 None을 사용한 이유는 759 X 8, 1500 X 8 등 확장을 위해
X = tf.compat.v1.placeholder(tf.float32, [None, 8])

# 정답 데이터 - 외부에서 입력되기 때문에 플레이스홀더 사용  --> 결과는 1개
T = tf.compat.v1.placeholder(tf.float32, [None, 1])

# 가중치 - 계속 업데이트 되어야하기 때문에 변수로 선언
W = tf.Variable(tf.random.normal([8,1]))

# 바이어스 설정 - 계속 업데이트 되어야하기 때문에 변수로 선언
b = tf.Variable(tf.random.normal([1]))

#=============================
# 3. 선형 회귀 값 계산
#=============================
z = tf.matmul(X, W) + b
y = tf.sigmoid(z)           # 0~1 사이 값

#=============================
# 4. 손실 함수 - cross-entropy
#=============================
# 교차 엔트로피 값은 예측값과 실제값 사이의 활률 분포 차이를 계산한 값
loss = -tf.reduce_mean(T * tf.log(y) + (1-T) * tf.log(1-y))

#=============================
# 5. 경사하강법 (최적화)
#=============================
learning_rate = 0.01        # 학습률
optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=learning_rate)
train = optimizer.minimize(loss)    # 손실 함수 최소화

#=============================
# 6. 정확도 측정
#=============================
predicated = tf.cast(y > 0.5, dtype=tf.float32)     # 0 또는 1을 반환
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicated, T), dtype=tf.float32))

#=============================
# 7. 학습 시작
#=============================
with tf.compat.v1.Session() as sess:
    # 가장먼저 변수(tf.Variable) 초기화
    sess.run(tf.compat.v1.global_variables_initializer())

    for step in range(20001):
        loss_val, y_val, _ = sess.run([loss, y, train], feed_dict={X:x_data, T:y_data})

        if step % 500 == 0:
            print('step :', step, ", loss_val =", loss_val)

    y_val, predicated_val, accuracy_val = sess.run([y, predicated, accuracy], feed_dict={X: x_data, T: y_data})

    print('y_val.shape =', y_val.shape, ", predicated_val.shape =", predicated_val.shape)
    print('accuracy_val =', accuracy_val)