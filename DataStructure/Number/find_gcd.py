# GCD 찾기
def find_gcd(number1, number2):
    while(number2 != 0):
        result = number2
        number1, number2 = number2, number1 % number2

    return result;

if __name__ == "__main__":
    a, b = 21, 12
    result = find_gcd(a, b)
    print(a, '와', b, '의 GCD 는', result)