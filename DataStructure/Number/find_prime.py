# 소수 찾기
import math
import random

# 2부터 number까지 나머지 연산을 통해 찾기
def find_prime(number):
    num = abs(number)
    if num < 4:
        return True
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

# 제곱근을 이용한 방법
def find_prime_sqrt(number):
    num = abs(number)
    if num < 4:
        return True

    for x in range (2, int(math.sqrt(num)) + 1):
        if number % x == 0:
            return False
    return True

def find_prime_fermat(number):
    if number <= 102:
        for a in range(2, number):
            if pow(a, number-1, number) != 1:
                return False
        return True
    else:
        for i in range(100):
            a = random.randint(2, number - 1)
            if pow(a, number -1, number) != 1:
                return False
        return True

if __name__ == "__main__":
    result1 = find_prime(17)
    result2 = find_prime(20)
    print(result1, result2)

    result1 = find_prime_sqrt(17)
    result2 = find_prime_sqrt(20)
    print(result1, result2)

    result1 = find_prime_fermat(17)
    result2 = find_prime_fermat(20)
    print(result1, result2)

