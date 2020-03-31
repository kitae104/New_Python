import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import jamotools

path_to_file = tf.keras.utils.get_file('input.txt', 'http://bit.ly/2Mc3SOV')

train_text = open(path_to_file, 'rb').read().decode(encoding='UTF-8')
s = train_text[:100]
print(s)

s_split = jamotools.split_syllables(s)
print(s_split)

s2 = jamotools.join_jamos(s_split)
print(s2)
print(s == s2)

train_text_X = jamotools.split_syllables(train_text)  # 텍스트를 자모 단위로 나눔
vocab = sorted(set(train_text_X))
vocab.append('UNK')
print(len(vocab))