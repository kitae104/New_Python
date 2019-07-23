# 텐서 변수 사용하기
# 가중치나 바이어스처럼 계속 업데이트되는 변수는 텐서플로우에서 변수로 정의
import tensorflow as tf

# 값이 계속 업데이트되는 변수노드 정의
W1 = tf.Variable(tf.random.normal([1]))         # 임의의 값 추출
b1 = tf.Variable(tf.random.normal([1]))         # np.random.rand(1) 과 유사

W2 = tf.Variable(tf.random.normal([1, 2]))
b2 = tf.Variable(tf.random.normal([1, 2]))

# 세션 생성
sess = tf.compat.v1.Session()

# 변수 노드 값 초기화 --> 변수 노드를 정의했다면 반드시 초기화 해야 함
sess.run(tf.compat.v1.global_variables_initializer())

for step in range(3):
    W1 = W1 - step
    b1 = b1 - step

    W2 = W2 - step
    b2 = b2 - step

    print("step :", step, ", W1 =", sess.run(W1), ", b1 =", sess.run(b1))
    print("step :", step, ", W2 =", sess.run(W2), ", b2 =", sess.run(b2))

sess.close()