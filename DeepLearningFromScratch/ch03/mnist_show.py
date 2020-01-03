import sys, os
sys.path.append(os.pardir)
from DeepLearningFromScratch.dataset.mnist import load_mnist
import numpy as np
from PIL import Image

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

if __name__ == "__main__":
    (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)
    img = x_train[1]
    label = t_train[1]
    print(label)

    print(img.shape)
    img = img.reshape(28, 28)   # 원래 이미지 모양으로 변형
    print(img.shape)

    img_show(img)


