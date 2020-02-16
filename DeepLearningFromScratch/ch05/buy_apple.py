# 사과 구입 구현하기
from DeepLearningFromScratch.ch05.layer_naive import MulLayer

apple = 100
apple_num = 2
tax = 1.1

# 계층들
multi_apple_layer = MulLayer()
multi_tax_layer = MulLayer()

# 순전파
apple_price = multi_apple_layer.forward(apple, apple_num)
price = multi_tax_layer.forward(apple_price, tax)

print(price)

# 역전파
dprice = 1
dapple_price, dtax = multi_tax_layer.backward(dprice)
dapple, dapple_num = multi_apple_layer.backward(dapple_price)
print(dapple, dapple_num, dtax)
