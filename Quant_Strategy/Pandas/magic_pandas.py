# 마법 공식을 판다스를 이용하여 처리하기
import pandas as pd
file_path = "D:\\Projects\\New_Python\\Quant_Strategy\\datas\\마법공식 데이터.xlsx"

# 엑셀 파일 읽어 오기 - 인덱스 컬럼 설정
per_data = pd.read_excel(file_path, sheet_name='PER', index_col=0)
print(per_data)

# PER 값이 0보다 작은 경우 필터링
filtered_per = per_data[per_data['PER']>0]
print(filtered_per)

# PER 데이터프레임 정렬
sorted_per = filtered_per.sort_values(by='PER')
print(sorted_per)

# PER 값으로 순위 만들기
rank_per = sorted_per['PER'].rank()
print(rank_per)

# PER 값으로 작성된 순위를 기존 데이터프레임에 합치기
sorted_per['PER랭킹'] = sorted_per['PER'].rank()
print(sorted_per)

# ROA 데이터 읽어 오기
roa_data = pd.read_excel(file_path, sheet_name='ROA', index_col=0)
print(roa_data)

# NaN값 제거하기
filtered_roa = roa_data.dropna()
print(filtered_roa)

# 컬럼명 변경하기 - 컬럼명을 리스트로 입력
filtered_roa.columns = ['ROA']
print(filtered_roa)

# 정렬하고 순위 매기기
sorted_roa = filtered_roa.sort_values(by='ROA', ascending=False)
print(sorted_roa)
rank_roa = sorted_roa['ROA'].rank(ascending=False)
print(rank_roa)
sorted_roa['ROA랭킹'] = sorted_roa['ROA'].rank(ascending=False)
print(sorted_roa)

# 두 데이터프레임 합치기
total_df = pd.merge(sorted_per, sorted_roa, how='inner', left_index=True, right_index=True)
print(total_df)

# 종합점수 필드 구하기
total_df['종합점수'] = (total_df['PER랭킹'] + total_df['ROA랭킹'])
print(total_df)

# 종합등수를 구한후 정렬해서 보여주기
total_df['종합등수'] = total_df['종합점수'].rank()
print(total_df.sort_values(by='종합등수'))