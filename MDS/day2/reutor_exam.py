import keras
from keras.datasets import reuters
keras.__version__

(train_data, train_labels), (test_data, test_labels) = reuters.load_data(num_words=10000) # 1만개 사용

train_data.shape

test_labels.max()

a = train_data[10:13]
print(a.shape)

from tabulate import tabulate
print(tabulate(a, tablefmt='psql'))