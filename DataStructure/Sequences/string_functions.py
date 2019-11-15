#문자열 메소드
##########################
# join()
##########################
slayer = ['버피', '앤', '아스틴']
res = " ".join(slayer)
print(res)
# 버피 앤 아스틴

res = "-<>-".join(slayer)
print(res)
# 버피-<>-앤-<>-아스틴

res = "".join(slayer)
print(res)
# 버피앤아스틴

res = "".join(reversed(slayer))
print(res)
# 아스틴앤버피

##########################
# ljust(), rjust()
##########################
name = "스칼렛"
res = name.ljust(50,'-')
print(res)
# 스칼렛-----------------------------------------------

res = name.rjust(50,'-')
print(res)
# -----------------------------------------------스칼렛

##########################
# format()
##########################
res = "{0} {1}".format("안녕", "파이썬!")
print(res)
# 안녕 파이썬!

res = "이름 : {who}, 나이 : {age}".format(who="제임스", age=19)
print(res)
# 이름 : 제임스, 나이 : 19

res = "이름 : {who}, 나이 : {0}".format(10, who="제임스")
print(res)
# 이름 : 제임스, 나이 : 10/