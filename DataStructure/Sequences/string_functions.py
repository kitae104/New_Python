#문자열 메소드
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