# 람다 표현식은 식 형태로 되어 있어 함수를 간단히 만들어냄
# 람다 표현식은 다른 함수의 인수로 넣을 때 주로 사용함
def plus_10(x):
    return x + 10

print(plus_10(1))

# 람다식(이름이 없는 함수)
plus_ten = lambda x : x + 10    # x는 매개변수
print(plus_ten(10))

print((lambda y : y * 2)(2))

y = 10
print((lambda x: x + y)(2))

# 람다 표현식을 인수로 사용하기
list1 = list(map(plus_10, [1,2,3]))
print(list1)

list2 = list(map(lambda x: x+20, [1,2,3]))
print(list2)