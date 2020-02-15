# 편미분 : 특정 장소에서 기울기
import numpy as np

def numerical_diff(f, x):
    h = 1e-4
    return (f(x + h) - f(x-h)) / (2*h)

def function_tmp1(x0):
    return x0*x0 + 4.0**2.0

def function_tmp2(x1):
    return 3.0**2.0 + x1*x1

res = numerical_diff(function_tmp1, 3.0)
print(res)

res = numerical_diff(function_tmp2, 4.0)
print(res)