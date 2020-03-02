import math
import tensorflow as tf

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

x = 1
y = 0
w = tf.random.normal([1], 0, 1)
output = sigmoid(x * w)
print(output)