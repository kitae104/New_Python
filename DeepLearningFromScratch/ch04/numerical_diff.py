# 수치 미분
import numpy as np
import matplotlib.pyplot as plt

def numerical_diff(f, x):
    h = 1e-4
    return (f(x + h) - f(x-h)) / (2*h)

def function_1(x):
    return 0.01 * x **2 + 0.1 * x

def tangent_line(f, x):
    d = numerical_diff(f, x)
    print(d)
    y = f(x) - d*x
    res = lambda t : d * t + y
    return res

x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)          # function_1 그래프

tf = tangent_line(function_1, 5)
y2 = tf(x)
plt.plot(x, y2)     # x = 5 일때 접선

tf = tangent_line(function_1, 10)
y3 = tf(x)
plt.plot(x, y3)     # x = 10 일때 접선
plt.show()

res = numerical_diff(function_1, 5)
print(res)

res2 = numerical_diff(function_1, 10)
print(res2)