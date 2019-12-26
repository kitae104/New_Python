# 리스트 컴프리헨션 : 반복문의 표현식
# [ 항목 for 항목 in 반복 가능한 객체]
# [ 표현식 for 항목 in 반복 가능한 객체]
# [ 표현식 for 항목 in 반복 가능한 객체 if 조건문문
a = [y for  y in range(1900, 1920)]
print(a)
# [1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919]

a = [y for  y in range(1900, 1920) if y%4 == 0]
print(a)
# [1900, 1904, 1908, 1912, 1916]

b = [2**i for i in range(13)]
print(b)
# [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

c = [x for x in a if x%8 == 0]
print(c)
# [1904, 1912]

d = [str(round(355/113.0, i)) for i in range(1, 6)]
print(d)
# ['3.1', '3.14', '3.142', '3.1416', '3.14159']

words = "Buffy is awesome and a wampire slayer".split()
print(words)
# ['Buffy', 'is', 'awesome', 'and', 'a', 'wampire', 'slayer']

e = [[w.upper(), w.lower(), len(w)] for w in words]
for i in e:
    print(i)
# ['BUFFY', 'buffy', 5]
# ['IS', 'is', 2]
# ['AWESOME', 'awesome', 7]
# ['AND', 'and', 3]
# ['A', 'a', 1]
# ['WAMPIRE', 'wampire', 7]
# ['SLAYER', 'slayer', 6]