import numpy as np

def my_func(D):
    m = np.mean(D)
    s = np.std(D)
    return m, s

data=np.random.randn(100)
data_mean, data_std = my_func(data)
print('mean:{0:3.2f}, std:{1:3.2f}'.format(data_mean, data_std))

output = my_func(data)
print('mean:{0:3.2f}, std:{1:3.2f}'.format(output[0], output[1]))