# Set : 반복 가능하고, 가변저깅고, 중복요소가 없고, 정렬되지 않은 컬렉션 데이터 타입
# 멤버십 테스트 및 중복 항목 제거에 사용
# 삽입 시간 복잡도 O(1)
# 합집합 O(m + n)
# 교집합 O(n)
print(dir(set()))
print(dir(frozenset()))
fs = frozenset((0,1,2,3,4,1))
print(2 in fs)
print(len(fs))
