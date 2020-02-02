# 서로 다른 데이터프레임들의 구성 형태와 속성이 균일하다면, 행 또는 열 중에 어느 한 방향으로 붙여도 데이터의 일관성을 유지할 수 있다.
# concat() : 기존의 데이터프레임의 형태를 유지하면서 이어 붙이는 개념
import pandas as pd

# 데이터프레임 만들기
df1 = pd.DataFrame({'a': ['a0', 'a1', 'a2', 'a3'],
                    'b': ['b0', 'b1', 'b2', 'b3'],
                    'c': ['c0', 'c1', 'c2', 'c3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'a': ['a2', 'a3', 'a4', 'a5'],
                    'b': ['b2', 'b3', 'b4', 'b5'],
                    'c': ['c2', 'c3', 'c4', 'c5'],
                    'd': ['d2', 'd3', 'd4', 'd5']},
                   index=[2, 3, 4, 5])

print(df1, '\n')
print(df2, '\n')

# 2개의 데이터프레임을 위 아래 행 방향으로 이어 붙이듯 연결하기
res1 = pd.concat([df1, df2], axis=0)
print(res1, '\n')

# ignore_index=True 옵션 설정하기
# 기존행의 인덱스는 무시하고 새로운 행 인덱스 설정
res2 = pd.concat([df1, df2], ignore_index=True)
print(res2, '\n')

# 2개의 데이터프레임을 좌우 열 방향으로 이어 붙이듯 연결하기
res3 = pd.concat([df1, df2], axis=1, join='outer')
print(res3, '\n')

# join='inner' 옵션 적용하기(교집합) - 공통적으로 있는 경우만
res4 = pd.concat([df1, df2], axis=1, join='inner')
print(res4, '\n')

# 시리즈 만들기
sr1 = pd.Series(['e0', 'e1', 'e2', 'e3'], name='e')
sr2 = pd.Series(['f0', 'f1', 'f2'], name='f', index=[3, 4, 5])
sr3 = pd.Series(['g0', 'g1', 'g2', 'g3'], name='g')
print(sr1)
print(sr2)
print(sr3)

# df1과 sr1을 좌우 열 방향으로 연결하기
res5 = pd.concat([df1, sr1], axis=1)
print(res5, '\n')

# df2과 sr2을 좌우 열 방향으로 연결하기
res6 = pd.concat([df2, sr2], axis=1, sort=True)
print(res6, '\n')

# sr1과 sr3을 좌우 열 방향으로 연결하기
res7 = pd.concat([sr1, sr3], axis=1)
print(res7, '\n')

# sr1과 sr3을 열의 위아래 방향으로 연결하기
res8 = pd.concat([sr1, sr3], axis=0, ignore_index=True)
print(res8, '\n')