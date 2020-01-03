import numpy as np
import matplotlib.pylab as plt
import DeepLearningFromScratch.libs.neural_lib as lib

def function_1(x):
    return 0.01*x**2 + 0.1*x

def function_2(x):
    return np.sum(x**2)

def tangent_line(f, x):
    d = lib.numerical_diff(f, x)
    print(d)
    y = f(x) - d*x
    return lambda t: d*t + y

def function_tmp1(x0):
    return x0*x0 + 4.0**2.0

def function_tmp2(x1):
    return 3.0**2.0 + x1*x1

if __name__ == "__main__":
    x = np.arange(0.0, 20.0, 0.1)
    y = function_1(x)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.plot(x, y)

    # x = 5에서의 접선
    tf = tangent_line(function_1, 5)
    y2 = tf(x)
    plt.plot(x, y2)

    # x = 10에서의 접선
    tf2 = tangent_line(function_1, 10)
    y3 = tf2(x)
    plt.plot(x, y3)

    # plt.show()

    res = lib.numerical_diff(function_1, 5)
    print(res)

    res = lib.numerical_diff(function_1, 10)
    print(res)

    res = lib.numerical_diff(function_1, x)
    print(res)

    res = lib.numerical_diff(function_tmp1, 3.0)
    print(res)

    res = lib.numerical_diff(function_tmp2, 4.0)
    print(res)

    res = lib.numerical_gradient(function_2, np.array([3.0, 4.0]))
    print(res)

    res = lib.numerical_gradient(function_2, np.array([0.0, 2.0]))
    print(res)

    res = lib.numerical_gradient(function_2, np.array([3.0, 0.0]))
    print(res)

    # 경사법으로 최소값을 구하기
    init_x = np.array([-3.0, 4.0])
    res = lib.gradient_descent(f=function_2, init_x=init_x, lr=0.1, step_num=100)
    print(res)

    # 학습률이 너무 큰 경우
    init_x = np.array([-3.0, 4.0])
    res = lib.gradient_descent(f=function_2, init_x=init_x, lr=10.0, step_num=100)
    print(res)

    # 학습률이 너무 작은 경우
    init_x = np.array([-3.0, 4.0])
    res = lib.gradient_descent(f=function_2, init_x=init_x, lr=1e-10, step_num=100)
    print(res)