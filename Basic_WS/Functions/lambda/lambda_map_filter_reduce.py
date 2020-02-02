# 람다 표현식과 map, filter, reduce 함수 활용하기
# 람다 표현식에 조건부 표현식 사용하기
a = [1,2,3,4,5,6,7,8,9,10]

# 리스트의 원소가 3의 배수이면 문자열로 만들고 아니면 그냥 반환하기 -> 반드시 else 구문 필요
list1 = list(map(lambda x : str(x) if x % 3 == 0 else x, a))
print(list1)

# 람다 표현식에 elif는 사용 불가
list2 = list(map(lambda x : str(x) if x == 1 else float(x) if x == 2 else x + 10, a))
print(list2)

def f(x):
    if x == 1:
        return str(x)
    elif x == 2:
        return float(x)
    else:
        return x + 10

list3 = list(map(f, a))
print(list3)

# map에 여러 객체 넣기
a = [1,2,3,4,5]
b = [2,4,6,8,10]
list4 = list(map(lambda x, y : x * y, a, b))
print(list4)

# filter 사용하기 - 특정 조건에 맞는 요소만 가져오기
def func(x):
    return x>5 and x < 10

a = [1,2,3,4,5,6,7,8,9,10]

flist1 = list(filter(func, a))  # 만족하는 요소만 가져옴
print(flist1)

flist2 = list(filter(lambda x : x > 3 and x < 8, a))
print(flist2)

# reduce : 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤 이전 결과와 누적해서 반환하는 함수
from functools import reduce
def f2(x, y):
    return x + y
a = [1,2,3,4,5]
rlist1 = reduce(f2, a)  # 결과를 계속 누저함
print(rlist1)

res = reduce(lambda x, y : x + y, a)
print(res)