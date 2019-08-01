# 선형회귀
import tensorflow as tf

# 학습 데이터
x_train = [1,2,3,4]
y_train = [6,5,7,10]

# 변수 선언
W = tf.Variable(tf.random.normal([1]), name='weight')
b = tf.Variable(tf.random.normal([1]), name='bias')

# 가설
hypothesis = x_train * W + b

# Cost 함수
cost = tf.reduce_mean(tf.square(hypothesis - y_train))