t1 = 1234, '안녕!'
print(t1[0])
# 1234

print(t1)
# (1234, '안녕!')

t2 = t1, (1,2,3,4,5)
print(t2)
# ((1234, '안녕!'), (1, 2, 3, 4, 5))

empty = ()
t = '안녕',
print(t)
('안녕',)

t2 = ('안녕')
print(t2)
# 안녕

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

