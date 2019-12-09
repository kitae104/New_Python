# 튜플 메소드
t = 1, 5, 7, 4, 4, 1
print(t)
# (1, 5, 7, 4, 4, 1)

print(t.count(4))
# 2

# 튜플 언패킹
x, *y = (1,2,3,4)
print(x)
# 1
print(y)
# [2, 3, 4]

*x, y = (1,2,3,4)
print(x)
# [1, 2, 3]
print(y)
# 4


