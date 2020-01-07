import pandas as pd

# k:v 구조를 갖는 딕셔너리를 만들고, 변수 dict_data에 저장
dict_data = {'a': 1, 'b': 2, 'c': 3}

# 판다스 Series() 함수로 딕셔너리(dict_data)를 시리즈로 변환. 변수 sr에 저장
sr = pd.Series(dict_data)

# 변수 sr의 자료형 출력
print(sr)
# a    1
# b    2
# c    3
# dtype: int64

print(sr['b'])
# 2

print(sr[[1, 2]])
# b    2
# c    3
# dtype: int64

print(sr[['a', 'b']])
# a    1
# b    2
# dtype: int64

# 리스트를 시리즈로 변환하여 변수 sr에 저장
list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)
print(sr)
# 0    2019-01-02
# 1          3.14
# 2           ABC
# 3           100
# 4          True
# dtype: object

print(sr[0])
# 2019-01-02

idx = sr.index
val = sr.values

print(idx)
# RangeIndex(start=0, stop=5, step=1)
print(val)
# ['2019-01-02' 3.14 'ABC' 100 True]

