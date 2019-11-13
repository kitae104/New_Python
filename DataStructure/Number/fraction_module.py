from fractions import Fraction

def rounding_floats(number1, places):
    return round(number1, places)

# 부동 소수점을 분수로 표현
def float_to_fractions(number):
    return Fraction(*number.as_integer_ratio())

'''분모를 반환한다.'''
def get_denominator(number1, number2):
    a = Fraction(number1, number2)
    return a.denominator


def get_numerator(number1, number2):
    '''분자를 반환한다. '''
    a = Fraction(number1, number2)
    return a.numerator

def test_testing_floats():
    number1 = 1.25
    number2 = 1
    number3 = -1
    number4 = 5/4
    number5 = 6
    assert(rounding_floats(number1, number2) == 1.2)
    assert(rounding_floats(number1 * 10, number3) == 10)
    assert(float_to_fractions(number1) == number4)
    assert(get_denominator(number2, number5) == number5)
    assert(get_numerator(number2, number5) == number2)
    print('테스트 통과')

if __name__ == '__main__':
    test_testing_floats()
    print(rounding_floats(1.25*10, -1))