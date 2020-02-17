# 스파이럴 데이터 셋 그래프
from DeepLearningFromScratch.dataset.spiral import load_data
import matplotlib.pyplot as plt

x, t = load_data()
print('x', x.shape)
print('t', t.shape)

N = 100
CLS_NUM = 3
markers = ['o', 'x', '^']

for i in range(CLS_NUM):
    plt.scatter(x[i*N:(i+1)*N, 0], x[i*N:(i+1)*N, 1], s=40, marker=markers[i])

plt.show()