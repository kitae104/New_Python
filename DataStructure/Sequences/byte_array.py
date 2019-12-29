# 바이트와 바이트 배열
blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
print(the_bytes)
# b'\x01\x02\x03\xff'

the_types_array = bytearray(blist)
print(the_types_array)
# bytearray(b'\x01\x02\x03\xff')

blist[1] = 127
print(blist)

# the_bytes[1] = 127    # 불변(immutable)
# print(the_bytes)

the_types_array[1] = 127 # 가변(mutable)
print(the_types_array)

# 비트 이동
x = 2
print(4 << x)   # 4를 왼쪽으로x번 이동
# 16
print(16 >> x)  # 16을 오른쪽으로 x번 이동
# 4

# 비트 연산
x = 8
print(x & 7)
# 0
print(x | 7)
# 15

