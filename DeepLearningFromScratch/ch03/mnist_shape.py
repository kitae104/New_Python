# MNIST 정보 출력
import sys, os
sys.path.append(os.pardir)      # 부모디렉토리로 접근
from DeepLearningFromScratch.dataset.mnist import load_mnist

# 데이터 로딩하기
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

# 각 데이터의 형상 출력하기
print(x_train.shape)    # (60000, 784)
print(t_train.shape)    # (60000,)
print(x_test.shape)     # (10000, 784)
print(t_test.shape)     # (10000,)