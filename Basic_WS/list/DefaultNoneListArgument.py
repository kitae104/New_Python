# 리스트에 항목 추가하기
def add(x, lst=None):
    if lst == None:     # 리스트가 없는 경우 새로운 리스트를 생성
        lst = []
    if x not in lst:
        lst.append(x)

    return lst

def reverse(lst):
    result = []

    for element in lst:
        result.insert(0, element)

    return result

def main():

    list1 = add(1)
    print(list1)

    list2 = add(2)
    print(list2)

    list3 = add(3, [11, 12, 13, 14])
    print(list3)

    list4 = add(3, list3)
    print(list4)

    list5 = reverse(list4)
    print(list5)

main()