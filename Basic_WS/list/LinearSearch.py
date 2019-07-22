# 리스트에서 key를 찾는 함수
def linearSearch(lst, key):
    for i in range(len(lst)):
        if key == lst[i]:
            return i            # 찾으면 인덱스를 반환

    return -1                   # 못 찾으면 -1을 반환

def binarySearch(lst, key):
    low = 0
    high = len(lst) - 1

    while high >= low:
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return mid
        else:
            low = mid + 1

    return -low - 1


lst = [2, 4, 7, 10, 11, 45, 50, 60, 66, 69, 70, 79]
i = linearSearch(lst, 11)
print(i)

j = binarySearch(lst, 11)
print(j)