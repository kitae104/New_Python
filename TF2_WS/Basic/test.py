import math
import tensorflow as tf

print(tf.__version__)

def sigmoid(x):
    return 1 / (1 + math.exp(-x))