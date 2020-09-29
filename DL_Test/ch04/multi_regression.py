# 다중 선형 회귀
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d        # 3d 그래프 라이브러리

data = [[2, 0, 81], [4,4,93], [6,2,91], [8,3, 97]]
x1 = [i[0] for i in data]
x2 = [i[1] for i in data]
y = [i[2] for i in data]

ax = plt.axes(projection='3d')      # 그래프 유형
ax.set_xlabel('study_hours')
ax.set_ylabel('private_class')
ax.set_zlabel('Score')
ax.scatter(x1, x2, y)
plt.show()