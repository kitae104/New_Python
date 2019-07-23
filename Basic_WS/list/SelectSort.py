# 선택 정렬
def selectionSort(lst):

    for i in range(len(lst) - 1):

        # lst[i:len(lst)]에서 가장 작은 원소를 찾는다.
        currentMin = lst[i]
        currentMinIndex = i

        for j in range(i + 1, len(lst)):
            if currentMin > lst[j]:
                currentMin = lst[j]
                currentMinIndex = j

        # 필요한 경우 lst[i]와 lst[currentMinIndex]를 교환한다.
        if currentMinIndex != i:
            lst[currentMinIndex] = lst[i]
            lst[i] = currentMin

    return lst

lst = [1, 9, 4.5, 10.6, 5.7, -4.5]
print(lst)
lst2 = selectionSort(lst)
print(lst2)
