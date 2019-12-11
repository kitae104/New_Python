# 리스트 사용하기
q = [2,3]
p = [1, q, 4]
print(p)
# [1, [2, 3], 4]

p[1].append("test")
print(p)
# [1, [2, 3, 'test'], 4]

print(q)
# [2, 3, 'test']

print(q.pop(1))
# 3

############################
# 리스트 메소드
############################
# 1 append()
people = ["버피", "페이스"]
people.append("자일스")
print(people)
# ['버피', '페이스', '자일스']

people[len(people):] = ["AA"]   # append와 동일
print(people)
# ['버피', '페이스', '자일스', 'AA']

# 2 extend()
# 반복 가능한 모든 항목 C를 리스트에 추가
people = ["AA", "BB"]
people.extend("CC")
print(people)
# ['AA', 'BB', 'C', 'C']

people += "DD"      # extend와 동일
print(people)
# ['AA', 'BB', 'C', 'C', 'D', 'D']

people += ["EE"]
print(people)
# ['AA', 'BB', 'C', 'C', 'D', 'D', 'EE']

people[len(people):] = "FF"   # ["FF"] 와 다름
print(people)
# ['AA', 'BB', 'C', 'C', 'D', 'D', 'EE', 'F', 'F']

# 3. insert()
people = ["AA", "BB"]
people.insert(1, "XX")
print(people)
# ['AA', 'XX', 'BB']

# 4. remove()
people = ["AA", "BB", "CC"]
people.remove("BB")
print(people)
# ['AA', 'CC']

# 5. pop()
people = ["AA", "BB", "CC"]
print(people.pop(1))
# BB

# 6. del 문
a = [1, 2, 3, 4, 5]
del a[0]
print(a)
# [2, 3, 4, 5]

del a[1:3]  # 슬라이스를 이용한 제거
print(a)
# [2, 5]

del a       # 변수 a 자체를 제거함

# 7. index() : 항목의 인덱스
a = [1, 2, 3, 4, 5]
print(a.index(3))
# 2

