import numpy as np
import time

def trad_version():
    t1 = time.time()
    X = range(10000000)
    Y = range(10000000)
    Z = []

    for i in range(len(X)):
        Z.append(X[i] + Y[i])

    return time.time() - t1     # 측정 시간 반환

def numpy_version():
    t1 = time.time()
    X = np.arange(10000000)
    Y = np.arange(10000000)
    Z = X + Y
    return time.time() - t1

if __name__ == "__main__":
    print(trad_version())
    print(numpy_version())

