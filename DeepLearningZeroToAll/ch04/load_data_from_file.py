import numpy as np
import tensorflow as tf
import pandas as pd

xy = np.loadtxt("../datas/data-01-test-score.csv", delimiter=",", dtype=np.float32)
x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]

print(y_data)