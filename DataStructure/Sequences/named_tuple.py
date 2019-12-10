import collections

Person = collections.namedtuple("person", "name age gender")
p = Person("홍길동", 30, "남자")
print(p)
# person(name='홍길동', age=30, gender='남자')

print(p[0])
# 홍길동

print(p.name)
# 홍길동

