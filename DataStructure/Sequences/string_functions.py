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

import decimal
res = "{0} {0!s} {0!r} {0!a}".format(decimal.Decimal("99.9"))
print(res)
# 99.9 99.9 Decimal('99.9') Decimal('99.9')

##########################
# 문자열 언패킹
##########################
hero = "버피"
number = 999
res = "{number}:{hero}".format(**locals()) # 현재 스코프에 있는 지역변수를 딕셔너리로 변환
print(res)
# 999:버피

##########################
# splitlines()
##########################
test = "로미오\n줄리엣"
res = test.splitlines()
print(res)
# ['로미오', '줄리엣']

##########################
# split()
##########################
test = "123 456 789"
res = test.split(' ')
print(res)
# ['123', '456', '789']

# 공백 제거후 합치기
test = "".join(res)
print(test)
# 123456789

test = "테스트*크리스-메리*16"
fields = test.split("*")
print(fields)
# ['테스트', '크리스-메리', '16']

res = fields[1].split('-')
print(res)
# ['크리스', '메리']

msg = "안녕*세상*!"
res = msg.split('*', 1)
print(res)
# ['안녕', '세상*!']

res = msg.rsplit("*", 1)
print(res)
# ['안녕*세상', '!']

##########################
# strip() - 문자열 제거
##########################
msg = "로미오 & 줄리엣999"
res = msg.strip("999")
print(res)
# 로미오 & 줄리엣

##########################
# swapcase - 대소문자 반전
##########################
msg = "Naver-Daum"
res = msg.swapcase()
print(res)
# nAVER-dAUM

##########################
# index(), find()
##########################
msg = "Buffy and Faith"
res = msg.find('y')
print(res)
# 4

res = msg.find('k')
print(res)
# -1

res = msg.index('y')
print(res)
# 4

#res = msg.index('k')
#print(res)
# ValueError: substring not found

##########################
# count
##########################
msg = "Buffy and Buffy and Buffy and Buffy"
res = msg.count("Buffy", 0, -1)
print(res)
# 3

res = msg.count("Buffy")
print(res)
# 4

##########################
# replace
##########################
msg = "Buffy and Buffy and Buffy and Buffy"
res = msg.replace("Buffy", "test")
print(res)
# test and test and test and test

res = msg.replace("Buffy", "test", 2)
print(res)
# test and test and Buffy and Buffy

##########################
# f-strings
##########################
name = "홍길동"

# !r은 표현 형식
msg = f"그의 이름은 {name!r} 입니다."
print(msg)
# 그의 이름은 '홍길동' 입니다.

# repr(name)은 name!r와 동일
msg = f"그의 이름은 {repr(name)} 입니다."
print(msg)
# 그의 이름은 '홍길동' 입니다.

width = 10
precision = 4
value = decimal.Decimal("12.34567")
res = f"결과: {value:{width}.{precision}}"    # 중첩 필드 사용
print(res)
# 결과:      12.35

from datetime import datetime
today = datetime(year=2019, month=11, day=20)
print(today)
# 2019-11-20 00:00:00

today = f"{today:%Y %B %d}"
print(today)
# 2019 November 20

number = 1024
res = f"{number:#0x}"
print(res)
# 0x400