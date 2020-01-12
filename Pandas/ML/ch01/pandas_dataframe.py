import pandas as pd

# 열이름을 key로 하고, 리스트를 value로 갖는 딕셔너리 정의(2차원 배열)
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

# 판다스 DataFrame() 함수로 딕셔너리를 데이터프레임으로 변환.
df = pd.DataFrame(dict_data)

print(df)
#    c0  c1  c2  c3  c4
# 0   1   4   7  10  13
# 1   2   5   8  11  14
# 2   3   6   9  12  15

# 행 인덱스/열 이름 지정하여, 데이터프레임 만들기
df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],
                   index=['준서', '예은'],
                   columns=['나이', '성별', '학교'])

# 행 인덱스, 열 이름 확인하기
print(df)
#     나이 성별   학교
# 준서  15  남  덕영중
# 예은  17  여  수리중

print(df.index)     #행 인덱스
# Index(['준서', '예은'], dtype='object')

print(df.columns)    #열 이름
# Index(['나이', '성별', '학교'], dtype='object')

df.index = ['학생1', '학생2']
df.columns = ['연령', '남녀', '소속']
print(df)
#      연령 남녀   소속
# 학생1  15  남  덕영중
# 학생2  17  여  수리중

# 열 이름과 행 이름 변경하기
df.rename(columns = {'연령':'AAA', '소속':'CCC'}, inplace=True)
df.rename(index={'학생1':'XXX'}, inplace=True)
print(df)
#      AAA 남녀  CCC
# XXX   15  남  덕영중
# 학생2   17  여  수리중

# 행/열 삭제
exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}
index = ['서준', '우현', '인아']
df = pd.DataFrame(exam_data, index)
df2 = df[:]
print(df)

# 행 삭제
df2.drop(['우현', '인아'], axis=0, inplace=True)
print(df2)

# 열 삭제
df3 = df[:]
df3.drop(['수학', '영어'], axis=1, inplace=True)
print(df3)

# 행 선택 - 이름으로 선택
label1 = df.loc['서준']
print(label1)

label2 = df.loc[['서준', '우현']]   # 리스트의 리스트로 사용
print(label2)

# 행 선택 - 위치로 선택
position1 = df.iloc[1]
print(position1)

position2 = df.iloc[[0, 1]]
print(position2)

# 열 선택1
math1 = df['수학']
print(math1)

math2 = df[['수학', '영어']]    # 2개 이상의 열 선택
print(math2)

# 열 선택 2
eng1 = df.영어
print(eng1)

# 슬라이싱 이용하기
res = df.iloc[::2]
print(res)

res = df.iloc[1::2]
print(res)

res = df.iloc[::-1]     # 역순으로 처리하기
print(res)

# 새로운 인덱스 설정하기
exam_data = {
    '이름':['서준', '우현', '인아'],
    '수학':[90, 80, 70],
    '영어' : [ 98, 89, 95],
    '음악' : [ 85, 95, 100],
    '체육' : [ 100, 90, 90]
}

df = pd.DataFrame(exam_data)
df.set_index('이름', inplace=True)
print(df)

# 1개 원소 선택
a = df.loc['서준', '음악']
print(a)

b = df.iloc[0, 2]
print(b)

# 2개 이상의 원소 선택
a = df.loc['서준', ['음악', '영어']]
print(a)

b = df.iloc[0, [1, 2]]
print(b)

c = df.iloc[0, 1:]
print(c)

x = df.loc[['서준', '우현'], ['음악', '체육']]
print(x)

y = df.iloc[[0, 1], 1:]
print(y)