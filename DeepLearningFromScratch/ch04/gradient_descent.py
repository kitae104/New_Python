# 경사하강법
import numpy as np
import matplotlib.pyplot as plt
from DeepLearningFromScratch.ch04.numerical_gradient import numerical_gradient, function_2

def gradient_descent(f, init_x, lr = 0.01, step_num = 100):
    x = init_x  # 초기값
    x_history = []

    for i in range(step_num):   # 반복 횟수
        x_history.append(x.copy())

        grad = numerical_gradient(f, x)
        x -= lr * grad
    return x, np.array(x_history)

init_x = np.array([-3.0, 4.0])
x, x_history = gradient_descent(function_2, init_x = init_x, lr = 0.1, step_num = 100 )
print(x) # 0에 가까운 값을 얻으면 거의 정확한 결과임

# init_x = np.array([-3.0, 4.0])
# x, x_history = gradient_descent(function_2, init_x = init_x, lr = 0.5, step_num = 100 )
# print(x)  # 학습률이 큰 경우

# init_x = np.array([-3.0, 4.0])
# x, x_history = gradient_descent(function_2, init_x = init_x, lr = 1e-4, step_num = 100 )
# print(x)  # 학습률이 작은 경우

plt.plot( [-5, 5], [0,0], '--b')
plt.plot( [0,0], [-5, 5], '--b')

plt.plot(x_history[:,0], x_history[:,1], 'o')

plt.xlim(-3.5, 3.5)
plt.ylim(-4.5, 4.5)
plt.xlabel("X0")
plt.ylabel("X1")
plt.show()

