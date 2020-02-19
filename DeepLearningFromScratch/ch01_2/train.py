# Trainer 사용하기
from DeepLearningFromScratch.common.optimizer import SGD
from DeepLearningFromScratch.common.trainer import Trainer
from DeepLearningFromScratch.dataset import spiral
from DeepLearningFromScratch.ch01_2.two_layer_net import TowLayerNet

# 하이퍼파라미터 설정
max_epoch = 300
batch_size = 30
hidden_size = 10
learning_rate = 1.0

x, t = spiral.load_data()
model = TowLayerNet(input_size=2, hidden_size=hidden_size, output_size=3)
optimizer = SGD(lr=learning_rate)

trainer = Trainer(model, optimizer)
trainer.fit(x, t, max_epoch, batch_size, eval_interval=20)
trainer.plot()