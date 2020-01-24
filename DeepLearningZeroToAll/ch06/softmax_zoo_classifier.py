# animal classification with softmax_cross_entropy_with_logits
import tensorflow as tf
import numpy as np

# 1 파일로 부터 데이터 읽어 오기
xy = np.loadtxt('../datas/data-04-zoo.csv', delimiter=',', dtype=np.float32)
x_data = xy[:, 0:-1]    # 전체 행과 마지막 전 열까지 데이터
y_data = xy[:, [-1]]    # 전체 행과 마지막 열 데이터
print(x_data.shape, y_data.shape)

# 2. 텐서를 위한 X, Y 플레이스홀더
X = tf.placeholder(tf.float32, shape=[None, 16])    # 16종류의 정보
Y = tf.placeholder(tf.int32, shape=[None, 1])       # 1개의 결과, 하지만 값의 범위는 0~6
nb_classes = 7  # 결과 종류 갯수 0~6

# one-hot encoding은 tf.ont_hot 사용 이후에 tf.reshape를 하지 않으면 오류 발생 !!
# [ [0], [3] ] => [ [[1000000]], [[0001000]] ] =>  [ [1000000], [0001000] ]
Y_one_hot = tf.one_hot(Y, nb_classes)   # one hot shape = (?, 1, 7)    ex)[[[1000000]], [[0001000]]] shape=(2,1,7), rank=3
#  -1은 모든 것을 의미하며, 왼쪽인자를 오른쪽에서 지정한 모양으로 모양을 변경해주는 것
Y_one_hot = tf.reshape(Y_one_hot, [-1, nb_classes]) # shape = (?, 7) ex)[[1000000], [0001000]]     shape=(2,7)  , rank=2

# 3. 가중치와 bias
W = tf.Variable(tf.random_normal([16, nb_classes]), name="weight")
b = tf.Variable(tf.random_normal([nb_classes]), name='bias')

# 4. 가설
# softmax = exp(logits) / reduce_sum(exp(logits), dim)
logits = tf.matmul(X, W) + b
hypothesis = tf.nn.softmax(logits)

# 5. 비용함수(다양한 형태 - cross entropy) - 전달 파라미터 주의 !!
# 주의할 점은 Y_one_hot은 label로 1개의1, 여러개의 0으로 이루어진 one_hot 벡터 이어야 한다.
# 그러면 각각의  logit에 대한 오차값이 결과로 나오고 그것을 tf.reduce_mean해주면 전체에 대한 평균오차값이 나온다.
cost_i = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=Y_one_hot)
cost = tf.reduce_mean(cost_i)   # 전체에 대한 평균오차값

# 최적화
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train = optimizer.minimize(cost)

# 정확도 계산
# argmax() : [0.1, 0.3, 0.5]의 argmax는 1로 가장 큰 값의 index 출력
prediction = tf.argmax(hypothesis, 1)   # 가장 높은 값을 가지는 index반환
correct_prediction = tf.equal(prediction, tf.argmax(Y_one_hot, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, dtype=tf.float32))

# 세션
with tf.Session() as sess:
    # 변수 초기화
    sess.run(tf.global_variables_initializer())

    # 학습
    for step in range(2001):
        cost_val, acc, _ = sess.run([cost, accuracy, train], feed_dict={X:x_data, Y:y_data})

        if step % 100 == 0:
            print("Step: {:5}\tCost: {:.3f}\tAcc: {:.2%}".format(step, cost_val, acc))

    # 예측
    pred = sess.run(prediction, feed_dict={X: x_data})

    # y_data: (N,1) = flatten => (N, ) matches pred.shape
    # [[0], [3]].flatten = [0, 3], zip은 두 리스트를 묶는 것으로 양쪽리스트에서 하나씩 뽑기위해 사용
    for p, y in zip(pred, y_data.flatten()):
        print("[{}] Prediction: {} True Y: {}".format(p == int(y), p, int(y)))