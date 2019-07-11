def m(x, y):
    x = 3;
    y[0] = 3

def reverse(lst):
    newLst = len(lst) * [0]

    for i in range(len(lst)):
        newLst[i] = lst[len(lst) - 1 - i]

    lst = newLst

def func(x, lst=[1,1,2,3]):
    if x in lst:
        lst.remove(x)
    return lst

def func2(x, lst=None):
    if lst == None:     # 리스트가 없는 경우 새로운 리스트를 생성
        lst = [1, 1, 2, 3]

    if x in lst:
        lst.remove(x)
    return lst


def main():
    number = 0
    numbers = [10]

    m(number, numbers)

    print('number :', number, 'numbers[0] : ', numbers[0])

    lst = [1,2,3,4,5]
    reverse(lst)

    for value in lst :
        print(value, end=' ')
    print()

    list1 = func(1)
    print(list1)

    list1 = func(1)
    print(list1)

    list2 = func2(1)
    print(list2)

    list2 = func2(1)
    print(list2)


main()