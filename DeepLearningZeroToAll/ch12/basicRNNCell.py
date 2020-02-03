# 기본적인 RNN 수행하기
import tensorflow as tf
import numpy as np

char_rdic = ['h', 'e', 'l', 'o']
char_dic = { w : i for i, w in enumerate(char_rdic)}
print(char_dic)