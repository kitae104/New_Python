# 평균 제곱 오차
import numpy as np

def mean_squared_error(y, t):
    return 0.5 * np.sum(np.square(y - t))

y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
t = [0,0,1,0,0,0,0,0,0,0]
print(mean_squared_error(np.array(y), np.array(t))) # 오차가 적을 수록 정답

y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
print(mean_squared_error(np.array(y), np.array(t)))