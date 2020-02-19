# 셋과 리스트

# 리스트의 중복 제거
def remove_dup(l1):
    return list(set(l1))

# 교집합 결과 반환
def intersection(l1, l2):
    return list(set(l1) & set(l2))

# 합집합 결과 반환
def union(l1, l2):
    return list(set(l1) | set(l2))

if __name__ == "__main__" :
    l1 = [1, 2, 3, 4, 5, 5, 9, 11, 11, 15]
    l2 = [4, 5, 6, 7, 8]
    l3 = []

    assert(remove_dup(l1) == [1, 2, 3, 4, 5, 9, 11, 15])
    assert (intersection(l1, l2) == [4, 5])
    assert (union(l1, l2) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 15])
    assert (remove_dup(l3) == [])
    assert(intersection(l3, l2) == l3)
    assert(sorted(union(l3, l2)) == sorted(l2))
    print("테스트 통과")