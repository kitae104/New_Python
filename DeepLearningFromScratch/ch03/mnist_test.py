import sys, os
sys.path.append(os.pardir)     #부모 디렉토리의 파일을 가져올 수 있도록 설정
from DeepLearningFromScratch.dataset.mnist import load_mnist

# flatten=True : 이미지를 1차원 배열로 평탄하게 만들지 결정 True : 784, False : 1 X 28 X 28 (3차원)
# normalize=False : 0.0~1.0 사이의 값으로 정규화할지를 결정(False 일 경우 원래값 그대로 0~255사이값 유지)
# one_hot_label(원-핫 인코딩) : 정답원소만 1이고 나머지는 0으로 처리 [0,0,1,0,0,0,0,0,0,0]
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

# 각 데이터의 형상 출력
print(x_train.shape)    # (60000, 784)
print(t_train.shape)    # (60000,)
print(x_test.shape)     # (10000, 784)
print(t_test.shape)     # (10000,)

