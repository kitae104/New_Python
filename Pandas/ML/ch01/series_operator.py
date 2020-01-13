# 판다스 산술연산
import pandas as pd
import numpy as np

student1 = pd.Series({'국어':np.nan, '영어':80, '수학':90})
student2 = pd.Series({'국어':90, '수학':80, '영어':80})

percentage = student1/200   # 시리즈의 내용과 개별적으로 나누어 진다.
print(percentage)

# 사칙 연산
add = student1 + student2
sub = student1 - student2
mul = student1 * student2
div = student1 / student2

# 데이터프레임 각 열에 시리즈 추가하는 형태로 생성
result = pd.DataFrame([add, sub, mul, div], index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)

# 사칙 연산
add = student1.add(student2, fill_value=0)
sub = student1.sub(student2, fill_value=0)
mul = student1.mul(student2, fill_value=0)
div = student1.div(student2, fill_value=0)

# 데이터프레임 각 열에 시리즈 추가하는 형태로 생성
result = pd.DataFrame([add, sub, mul, div], index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)
