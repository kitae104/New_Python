# 데이터 프레임 만들기
import pandas as pd
from collections import OrderedDict

# 딕셔너리 데이터 타입 사용
persons_dict = {
    'Name' : ['John', 'Sabre', 'Kim', 'Sato'],
    'Country' : ['USA', 'France', 'Korea', 'Japan'],
    'Age' : [31, 33, 28, 40],
    'Job' : ['Student', 'Lawer', 'Developer', 'Chef']
}

print(persons_dict)

# 옵션을 사용하지 않으면 컬럼이 임의의 순서를 가짐
df = pd.DataFrame(persons_dict)
print(df)

# 옵션을 지정하여 순서를 정해줌
df = pd.DataFrame(data=persons_dict, columns=['Name', 'Country', 'Age', 'Job'] )
print(df)
print('-'*50)

# OrderedDic Type 사용하기 --> column 옵션을 주지 않아도 순서가 지켜짐
ordered_persons_dict = OrderedDict(
    [
     ('Name' , ['John', 'Sabre', 'Kim', 'Sato']),
     ('Country', ['USA', 'France', 'Korea', 'Japan']),
     ('Age', [31, 33, 28, 40]),
     ('Job', ['Student', 'Lawer', 'Developer', 'Chef'])
    ]
)
df1 = pd.DataFrame(ordered_persons_dict)
print(df1)
print('-'*50)

# 별도의 index 값을 지정할 수 있음
df1 = pd.DataFrame(ordered_persons_dict, index=['one', 'two', 'three', 'four'])
print(df1)
print('-'*50)