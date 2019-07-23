# 삽입 정렬
def insertionSort(lst):
    for i in range(1, len(lst)):
        # lst[0 : i+1]이 정렬되도록
        # lst[i]를 정렬된 부분 리스트 lst[0 : i]에 삽입한다.
        currentElement = lst[i]
        k = i - 1

        while k>=0 and lst[k] > currentElement :
            lst[k+1] = lst[k]       # 뒤쪽으로 옮기기
            k -= 1                  # 앞으로 이동하기

        lst[k+1] =currentElement    # 데이터 삽입하기

    return lst

lst = [1, 9, 4.5, 10.6, 5.7, -4.5]
print(lst)
lst2 = insertionSort(lst)
print(lst2)