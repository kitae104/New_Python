# 집합과 딕셔너리

# 딕셔너리 내용 출력
pairs = [('a', 1), ("b", 2), ("c", 3)]
print(pairs)
d1 = dict(pairs)
print(d1)
print("딕셔너리1\t: {0}".format(d1))

d2 = {"a": 1, "c": 2, "d": 3, "e": 4}
print("딕셔너리2\t: {0}".format(d2))

# 교집합
intersection = d1.keys() & d2.keys()
print(intersection)

intersection2 = d1.items() & d2.items()
print(intersection2)

# 차집합
subtraction1 = d1.keys() - d2.keys()
print(subtraction1)

subtraction2 = d2.keys() - d1.keys()
print(subtraction2)

subtraction3 = d1.items() - d2.items()
print(subtraction3)

# 딕셔너리의 특정 키 제외하기
d3 = {key : d2[key] for key in d2.keys() - {"c", "d"}}
print(d3)
print("d2 - {{c, d}}\t: {0}".format(d3))