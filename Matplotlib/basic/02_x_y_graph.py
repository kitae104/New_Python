# x축과 y축에 값이 각각 있는 그래프
import matplotlib.pyplot as plt

# red circle 그래프 (b-, g-, ro, mx, c--, k*)
plt.plot([1,2,3,4], [1,4,9, 16], 'k*') # x값, y값
plt.axis([0, 6, 0, 20])     # x축은 0~6, y축은 0~20
plt.show()