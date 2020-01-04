from DeepLearningFromScratch.ch05.layer_naive import *

apple = 100
apple_num = 2
orange = 150
orange_num = 3
tax = 1.1

# 계층들
mul_apple_layer = MulLayer()
mul_orange_layer = MulLayer()
add_apple_orange_layer = AddLayer()
mul_tax_layer = MulLayer()

# 순전파(forward)
apple_price = mul_apple_layer.forward(apple, apple_num) #1
orange_price = mul_orange_layer.forward(orange, orange_num) # 2
all_price = add_apple_orange_layer.forward(apple_price, orange_price)   # 3
price = mul_tax_layer.forward(all_price, tax)   # 4
print(price)    # 220

# 역전파(backward)
dprice = 1
dall_price, dtax = mul_tax_layer.backward(dprice)
dapple_price, dorange_price = add_apple_orange_layer.backward(dall_price)
dorange, dorange_num = mul_orange_layer.backward(dorange_price)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)

print("price:", int(price))
print("dApple:", dapple)
print("dApple_num:", int(dapple_num))
print("dOrange:", dorange)
print("dOrange_num:", int(dorange_num))
print("dTax:", dtax)

