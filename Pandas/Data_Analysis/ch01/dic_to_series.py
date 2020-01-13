import pandas as pd

dic_data = {'a':1, 'b':2, 'c':3}
print(dic_data)
# 딕셔너리 {'a': 1, 'b': 2, 'c': 3}

sr = pd.Series(dic_data)
print(sr)
# Series 출력
# a    1
# b    2
# c    3
# dtype: int64

print(type(sr))

list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)
print(sr)