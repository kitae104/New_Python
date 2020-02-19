# cupy 사용하기
import numpy as np
a = np.random.randn(3)
print(a.dtype)

a = np.random.randn(3).astype(np.float32)
print(a.dtype)

a = np.random.randn(3).astype('f')
print(a.dtype)

import cupy as cp
x = cp.arange(6).reshape(2,3).astype('f')
print(x)

print(x.sum(axis=0))
print(x.sum(axis=1))