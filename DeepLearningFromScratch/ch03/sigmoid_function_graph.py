import numpy as np
import matplotlib.pylab as plt
import DeepLearningFromScratch.ch03.neural_lib as lib

x = np.arange(-5.0, 5.0, 0.1)
y = lib.sigmoid(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()