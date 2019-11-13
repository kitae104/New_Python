# 다른 진법을 10진수로 만들기
def convert_to_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0:
        result += number % 10 * multiplier
        multiplier *= base
        number = number // 10

    return result

# 10진수를 다진 진법으로 바꾸기
def convert_from_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0:
        result += number % base * multiplier
        multiplier *= 10
        number = number // base

    return result

# 10진수를 임의의 진법으로 변경하기
def convert_dec_to_any_base_rec(number, base):
    convertString = "0123456789ABCDEF"
    if number < base:
        return convertString[number]
    else:
        return convert_dec_to_any_base_rec(number // base, base) + convertString[number % base]



if __name__ == "__main__":
    a = convert_to_decimal(1001, 2)
    print(a)
    a = convert_from_decimal(9, 2)
    print(a)
    a = convert_dec_to_any_base_rec(65, 16)
    print(a)
