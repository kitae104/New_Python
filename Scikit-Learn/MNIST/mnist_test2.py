from sklearn.datasets import fetch_openml
mnist = fetch_openml('mnist_784')
print(mnist.data.shape, mnist.target.shape)
# (70000, 784)

split_ratio = 0.9
n_train = int(mnist.data.shape[0] * split_ratio)
print(n_train)
# 63000

n_test = mnist.data.shape[0] - n_train
print(n_test)
#7000

X_train = mnist.data[:n_train]
y_train = mnist.target[:n_train]
print(X_train.shape, y_train.shape)
# ((63000, 784), (63000,))

X_test = mnist.data[n_train:]
y_test = mnist.target[n_train:]
print(X_test.shape, y_test.shape)
# ((7000, 784), (7000,))

# Checking uniqueness of the target
import numpy as np
print(np.unique(y_train))
# array(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], dtype=object)

from sklearn.ensemble import RandomForestClassifier

# module loading
clf = RandomForestClassifier()

# train data!
clf.fit(X_train, y_train)

# make predicition
prediction = clf.predict(X_test)
print(prediction.shape)
# 7000

# accuracy
result = (prediction == y_test).mean()
print(result)
# 0.9617142857142857

import matplotlib.pyplot as plt

# 랜덤하게 몇 가지 data 가져오기
random_pick = np.random.randint(low=0, high=n_test, size=10)
# array([3898, 6815, 6640, 2924,  451, 2688,  633, 6563, 5993, 4024])


figure = plt.figure()
figure.set_size_inches(12, 5)

axes = []
for i in range(1, 11):
    axes.append(figure.add_subplot(2, 5, i))

tmp_list = []
for i in range(10):
    tmp = mnist.data[n_train + random_pick[i]]
    tmp = tmp.reshape(-1, 28)
    tmp_list.append(tmp)

print(y_test[random_pick])

for i in range(10):
    axes[i].matshow(tmp_list[i])

plt.show()