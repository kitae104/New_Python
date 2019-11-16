# 재무제표 페이지에서 테이블 가져오기
import pandas as pd
import requests

fs_url = "http://comp.fnguide.com/SVO2/ASP/SVD_Finance.asp?pGB=1&gicode=A005380&cID=&MenuYn=Y&ReportGB=D&NewMenuID=103&stkGb=701"
fs_page = requests.get(fs_url)

# 판다스로 테이블 데이터만 찾아서 데이터프레임으로 만들어냄
fs_tables = pd.read_html(fs_page.text)

###############################
# 포괄손익계산서
###############################
temp_df = fs_tables[0]

# 인덱스로 특정 항목 설정
temp_df = temp_df.set_index('IFRS(연결)')

# 필요없는 컬럼 제거하기
temp_df = temp_df[['2016/12', '2017/12', '2018/12', '2019/06']]

# 필요한 행만 선택하기
temp_df = temp_df.loc[['매출액','영업이익','당기순이익']]
# print(temp_df)
# print()

###############################
# 재무상태표
###############################
temp_df2 = fs_tables[2]

# 인덱스로 특정 항목 설정
temp_df2 = temp_df2.set_index('IFRS(연결)')

# 컬럼 항목 설정 - 필요없는 컬럼 제거하기
temp_df2 = temp_df2[['2016/12', '2017/12', '2018/12', '2019/06']]

# 필요한 행만 선택하기
temp_df2 = temp_df2.loc[['자산','부채','자본']]
# print(temp_df2)
# print()

###############################
# 현금흐름표
###############################
temp_df3 = fs_tables[4]

# 인덱스로 특정 항목 설정
temp_df3 = temp_df3.set_index('IFRS(연결)')

# 컬럼 항목 설정 - 필요없는 컬럼 제거하기
temp_df3 = temp_df3[['2016/12', '2017/12', '2018/12', '2019/06']]

# 필요한 행만 선택하기
temp_df3 = temp_df3.loc[['영업활동으로인한현금흐름']]
#print(temp_df3)

# 재무제표 페이지의 데이터프레임들 이어 붙이기
fs_df = pd.concat([temp_df, temp_df2, temp_df3])
print(fs_df)