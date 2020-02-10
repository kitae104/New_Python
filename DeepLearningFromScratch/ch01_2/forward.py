import numpy as np

from DeepLearningFromScratch.libs.simple_layer import TwoLayerNet

x = np.random.randn(10, 2)      # 2차원 데이터 10개
model = TwoLayerNet(2, 4, 3)    # 입력(2) - 은닉(4) - 출력(3)
s = model.predict(x)            # 입력 x에 대한 점수s(예측 결과)
print(s)