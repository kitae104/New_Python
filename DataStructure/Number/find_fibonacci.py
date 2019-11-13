# 피보나치 수열 찾기
import math

# 반복을 이용한 방법
def find_fibonacci_iter(n):
    if n < 2:
        return n
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def find_fibonacci_rec(n):
    if n < 2:
        return n
    return find_fibonacci_rec(n-1) + find_fibonacci_rec(n-2)

def find_fibonacci_generator():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

if __name__ == "__main__":
    n = 10

    result = find_fibonacci_iter(n)
    print(result)

    result = find_fibonacci_rec(n)
    print(result)

    fg = find_fibonacci_generator()
    for _ in range(10):
        print(next(fg), end=" ")

# 55
# 55
# 1 1 2 3 5 8 13 21 34 55