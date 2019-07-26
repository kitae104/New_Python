# 데이터프레임을 파일로 저장하기
import pandas as pd

# 딕셔너리 데이터 타입 사용
persons_dict = {
    'Name' : ['John', 'Sabre', 'Kim', 'Sato'],
    'Country' : ['USA', 'France', 'Korea', 'Japan'],
    'Age' : [31, 33, 28, 40],
    'Job' : ['Student', 'Lawer', 'Developer', 'Chef']
}

df = pd.DataFrame(data=persons_dict, columns=['Name', 'Country', 'Age', 'Job'])
print(df)

df.to_csv('../data/persons_01.csv', sep=',')    # 콤마로 분리해서 저장
df.to_csv('../data/persons_01.tsv', sep='\t')   # 탭으로 분리해서 저장
df.to_csv('../data/persons_01.txt', sep=' ')    # 공백으로 분리해서 저장

# JSON 파일로 저장하기
df.to_json('../data/persons_04.json')