# 플레이스홀더 : 그래프에 사용할 입력값을 나중에 받기 위해 사용하는 매개변수
# 변수 : 그래프를 최적화하는 용도로 텐서플로가 학습한 결과를 갱신하기 위해 사용하는 변수
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf

# None은 크기가 정해지지 않았음을 의미
X = tf.compat.v1.placeholder(tf.float32, [None, 3])
print(X)
# Tensor("Placeholder:0", shape=(?, 3), dtype=float32)

# X 플레이스홀더에 넣을 값 입니다.
# 플레이스홀더에서 설정한 것 처럼, 두번째 차원의 요소의 갯수는 3개 입니다.
x_data = [[1,2,3], [4,5,6]]

# random_normal : 정규분포의 무작위 값으로 초기화
W = tf.Variable(tf.random.normal([3, 2]))
# W = tf.Variable([[0.1, 0.1],[0.2, 0.2],[0.3 0.3]]) 과 같은 데이터 입력 가능
b = tf.Variable(tf.random.normal([2, 1]))

# tf.matmul 처럼 mat* 로 되어 있는 함수로 행렬 계산을 수행합니다.
expr = tf.matmul(X, W) + b

# 그래프 실행
# tf.Session() 을 사용
# 최근엔 tf.compat.v1.Session() 로 변경
sess = tf.compat.v1.Session()

# 위에서 설정한 Variable 들의 값들을 초기화 하기 위해
# 처음에 tf.global_variables_initializer 를 한 번 실행해야 합니다.
# 최근엔 tf.compat.v1.global_variables_initializer() 로 변경
sess.run(tf.compat.v1.global_variables_initializer())

print("=== x_data ===")
print(x_data)
print("=== W ===")
print(sess.run(W))
print("=== b ===")
print(sess.run(b))
print("=== expr ===")
print(sess.run(expr, feed_dict={X:x_data}))

sess.close()