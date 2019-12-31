#softmax 함수 구현 과정
import numpy as np
import DeepLearningFromScratch.ch03.neural_lib as lib

a = np.array([0.3, 2.9, 4.0])
exp_a = np.exp(a)   #지수함수
print(exp_a)
# [ 1.34985881 18.17414537 54.59815003]

sum_exp_a = np.sum(exp_a)
print(sum_exp_a)
# 74.1221542101633

y = exp_a / sum_exp_a
print(y)
# [0.01821127 0.24519181 0.73659691]

a = np.array([1010, 1000, 990])
# res = np.exp(a) / np.sum(np.exp(a))
# print(res)
# [inf inf inf]     # 결과 이상

c = np.max(a)
print(c)
# 1010

print(a - c)
# [  0 -10 -20]

res = np.exp(a - c) / np.sum(np.exp(a - c))
print(res)
# [9.99954600e-01 4.53978686e-05 2.06106005e-09]

a = np.array([0.3, 2.9, 4.0])
y = lib.softmax(a)
print(y)
# [0.01821127 0.24519181 0.73659691]

print(np.sum(y))
# 1.0
