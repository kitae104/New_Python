import pandas as pd

# 판다스 DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
data = {'name' : [ 'Jerry', 'Riah', 'Paul'],
        'algol' : [ "A", "A+", "B"],
        'basic' : [ "C", "B", "B+"],
        'c++' : [ "B+", "C", "C+"],
        }

df = pd.DataFrame(data)
df.set_index('name', inplace=True)
print(df)

df.to_csv('../../result/df_sample.csv')
df.to_json('../../result/df_sample.json')
df.to_excel('../../result/df_sample.xlsx')
