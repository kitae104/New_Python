# 딕셔너리 생성 - 내부적으로 해시 테이블로 구성
res = hash(42)
print(res)

res = hash("hello")
print(res)

tarantino = {}
tarantino['name'] = 'ABC'
tarantino['job'] = "MMM"
print(tarantino)

# 딕셔너리 작성 방법
dic1 = dict({'name':'버피', "age":16, 'hobby':'게임'})
print(dic1)

dic2 = dict(name='AAA', age=45, hobby="BBB")
print(dic2)

dic3 = dict([("name", "CCC"), ("age", 15), ("hobby", "DDD")])
print(dic3)
