import DeepLearningFromScratch.libs.neural_lib as lib
import numpy as np

# 평균 제곱 오차 함수 사용하기
t = [0,0,1,0,0,0,0,0,0,0]
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
res = lib.mean_squared_error(np.array(y), np.array(t))
print(res)

y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
res = lib.mean_squared_error(np.array(y), np.array(t))
print(res)

# 교차 엔트로피 오차 함수 사용하기
t = [0,0,1,0,0,0,0,0,0,0]
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
res = lib.cross_entropy_error(np.array(y), np.array(t))
print(res)
# 0.510825457099338

y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
res = lib.cross_entropy_error(np.array(y), np.array(t))
print(res)
# 2.302584092994546