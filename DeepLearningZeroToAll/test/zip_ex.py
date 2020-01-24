# zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
l = list(zip([1,2,3], [4,5,6]))
print(l)

str_l = list(zip("abc", "def"))
print(str_l)