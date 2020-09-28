# coding: utf-8
import numpy as np

#공부시간 X와 성적 Y의 리스트를 만듭니다.
x = [2, 4, 6, 8]
y = [81, 93, 91, 97]

# x와 y의 평균값
mx = np.mean(x)
my = np.mean(y)

# 기울기 공식의 분모
divisor = sum([(i-mx)**2 for i in x])

def top(x, mx, y, my):
    d = 0
    for i in range(len(x)):
        d += (x[i] - mx) * (y[i] - my)
    return d

# 기울기 공식의 분자
dividend = top(x, mx, y, my)

print('분모 :', divisor)
print('분자 :', dividend)

a = dividend / divisor
print('기울기(a) : ', a)
b = my - (mx * a)
print('절편(b) : ', b)