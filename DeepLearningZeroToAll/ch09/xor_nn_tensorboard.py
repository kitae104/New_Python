# NN으로 XOR 구현하기 + 텐서보드 만들기
import tensorflow as tf
import numpy as np

x_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)
y_data = np.array([[0], [1], [1], [0]], dtype=np.float32)

X = tf.placeholder(tf.float32, [None, 2], name='x')
Y = tf.placeholder(tf.float32, [None, 1], name="y")

# 계층 추가하여 처리
# name_scope로 묶어서 한 단위로 보여줌
with tf.name_scope("Layer1"):
    W1 = tf.Variable(tf.random_normal([2, 2]), name="weight_1")
    b1 = tf.Variable(tf.random_normal([2]), name="bias_1")
    layer1 = tf.sigmoid(tf.matmul(X, W1) + b1)

    tf.summary.histogram("W1", W1)
    tf.summary.histogram("b1", b1)
    tf.summary.histogram("Layer1", layer1)

with tf.name_scope("Layer2"):
    W2 = tf.Variable(tf.random_normal([2, 1]), name="weight_2")
    b2 = tf.Variable(tf.random_normal([1]), name="bias_2")
    hypothesis = tf.sigmoid(tf.matmul(layer1, W2) + b2)

    tf.summary.histogram("W2", W2)
    tf.summary.histogram("b2", b2)
    tf.summary.histogram("Hypothesis", hypothesis)

# 5. 비용함수(다양한 형태 - cross entropy) - 전달 파라미터 주의 !!
# 주의할 점은 Y_one_hot은 label로 1개의1, 여러개의 0으로 이루어진 one_hot 벡터 이어야 한다.
# 그러면 각각의  logit에 대한 오차값이 결과로 나오고 그것을 tf.reduce_mean해주면 전체에 대한 평균오차값이 나온다.
with tf.name_scope("Cost"):
    cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))  # 기본 형태
    tf.summary.scalar("Cost", cost)
#cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), axis=1))
#cost_i = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=Y_one_hot)
#cost = tf.reduce_mean(cost_i)   # 전체에 대한 평균오차값

# 최적화
with tf.name_scope("Train"):
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-1)
    train = optimizer.minimize(cost)

# 정확도 계산
# 가설이 0.5보다 큰지 확인하여 True 설정, 아니면 false -> 타입 때문에 1. 과 0. 으로 설정
predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))
tf.summary.scalar("accuracy", accuracy)
# argmax() : [0.1, 0.3, 0.5]의 argmax는 1로 가장 큰 값의 index 출력
# prediction = tf.argmax(hypothesis, 1)   # 가장 높은 값을 가지는 index반환
# correct_prediction = tf.equal(prediction, tf.argmax(Y, 1))  # 맞는지 확인
# accuracy = tf.reduce_mean(tf.cast(correct_prediction, dtype=tf.float32))

# 세션
with tf.Session() as sess:
    # tensorboard --logdir=./logs/xor_logs
    merged_summary = tf.summary.merge_all()
    writer = tf.summary.FileWriter("./logs/xor_logs_r0_01")
    writer.add_graph(sess.graph)  # Show the graph

    # 변수 초기화
    sess.run(tf.global_variables_initializer())

    # 학습
    for step in range(10001):
        # 학습 데이터만 사용해서 학습
        cost_val, summary, _ = sess.run([cost, merged_summary, train], feed_dict={X:x_data, Y:y_data})
        writer.add_summary(summary, global_step=step)

        if step % 100 == 0:
            #print("Step: {:5}\tCost: {:.3f}\tWeight: {:.8f}".format(step, cost_val, W_val))
            print(step, cost_val)

    # Accuracy report
    h, c, a = sess.run([hypothesis, predicted, accuracy], feed_dict={X: x_data, Y: y_data})
    print("\nHypothesis: ", h, "\nCorrect: ", c, "\nAccuracy: ", a)