#리스트 언패킹
first, *rest = [1,2,3,4,5]
print(first)
# 1
print(rest)
# [2, 3, 4, 5]

# 함수의 전달 인수로 *인수 사용
def ex_args(a, b, c):
    return a * b * c

L = [2, 3, 4]
res = ex_args(*L)     #리스트 언패킹
print(res)

res = ex_args(2, *L[1:]) #리스트 언패킹
print(res)