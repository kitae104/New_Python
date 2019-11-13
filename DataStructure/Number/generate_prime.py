# 소수 생성하기
import math
import random
import sys
from DataStructure.Number.find_prime import find_prime_sqrt

def generate_prime(number=3):
    while True:
        p = random.randint(pow(2, number-2), pow(2, number-1)-1)
        p = 2 * p + 1
        if find_prime_sqrt(p):
            return p

if __name__ == "__main__":
    print(generate_prime(6))