import numpy as np

# AND 함수 구현
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

# NAND
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])  # AND와 반대 상황
    b = 0.7                     # AND와 반대 상황
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

# OR
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

# 퍼셉트론
def percept(x, w, b):
    return np.sum(w * x) + b

# XOR
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y