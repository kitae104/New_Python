# mnist 랜덤 이미지 보기
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data  # 해당 정보 추가 해서 처리


mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)

# 55000 중에 6개의 숫자를 임의로 뽑아냄
for i in np.random.randint(55000, size=6):
    #print(i)
    imgvec = mnist.train.images[i, :]
    # print(imgvec)
    labelvec = mnist.train.labels[i, :]
    # print(labelvec)
    imgmatrix = np.reshape(imgvec, (28, 28)) # 784 --> 28 * 28
    # print(imgmatrix)
    label = np.argmax(labelvec)
    # print(label)

    plt.matshow(imgmatrix, cmap=plt.get_cmap('gray'))
    plt.title("index: %d, label: %d" % (i, label))
    plt.show()