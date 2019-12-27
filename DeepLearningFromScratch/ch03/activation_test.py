import numpy as np
import DeepLearningFromScratch.ch03.neural_lib as lib
x = np.array([-1.0, 1.0, 2.0])
print(x)
# [-1.  1.  2.]

y = x > 0
print(y)
# [False  True  True]

y = y.astype(np.int)    # bool --> int
print(y)
# [0 1 1]

x = np.array([-1.0, 1.0, 2.0])
res = lib.sigmoid(x)
print(res)
# [0.26894142 0.73105858 0.88079708]

t = np.array([1.0, 2.0, 3.0])
print(1.0 + t)
# [2. 3. 4.]

print(1.0/t)
# [1.         0.5        0.33333333]