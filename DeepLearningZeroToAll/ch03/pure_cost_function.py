import numpy as np

X = np.array([1, 2, 3])
Y = np.array([1, 2, 3])

def cost_function(W, X, Y):
    c = 0
    for i in range(len(X)):
        c += (W * X[i] - Y[i])**2
    return c / len(X)

for feedW in np.linspace(-3, 5, num=15):    # -3에서 5까지 15구간으로 나눔
    curr_cost = cost_function(feedW, X, Y)
    print("{:6.3f} | {:10.5f}".format(feedW, curr_cost))