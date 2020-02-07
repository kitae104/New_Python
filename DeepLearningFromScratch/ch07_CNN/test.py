import numpy as np

# CNN은 4차원의 데이터를 다룸
x = np.random.rand(10, 1, 28, 28)  # 높이 28, 너비 28, 채널 1, 데이터 10개
print(x.shape)
print(x[0].shape)       # 1번째 데이터
print(x[1].shape)       # 2번째 데이터
print(x[0, 0].shape)    # 1번째 데이터의 첫 채널의 공간에 접근