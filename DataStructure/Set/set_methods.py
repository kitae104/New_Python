# 집합과 관련된 메소드
# add()
s = {'a', 'b', 'c'}
s.add('d')
print(s)
# {'b', 'a', 'd', 'c'}

# update()와 |= 연산자 (합집합)
s = {'a', 'b', 'c'}
s.update({'a', 'c', 'd', 'e'})
print(s)
s |= {'k', 's'}
print(s)

# union과 | 연산자
s = {'a', 'b', 'c'}
s.union({'a', 'f'})
print(s.union({'a', 'f'}))
print(s | {'d'})

# intersection() 과 & 연산자
s = {'a', 'b', 'c'}
res = s.intersection({'a', 'f'})
print(res)
res = s & {'b', 'f'}
print(res)

# difference()와 - 연산자
s = {'a', 'b', 'c'}
res = s.difference({'a', 'f'})
print(res)
res = s - {'b', 'f'}
print(res)

# clear()
s = {'a', 'b', 'c'}
s.clear()
print(s)

# discard(), remove(), pop()
countries = {'프랑스', '스페인', '영국'}
res = countries.discard('한국')   # 해당 항목 제거 반환값 없음
print(res)
#res = countries.remove('한국')   # 항목이 없을 경우 오류 발생
#print(res)
res = countries.pop()   # 무작위
print(res)




