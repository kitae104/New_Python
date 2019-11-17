import pandas as pd
import requests
from Quant_Strategy.Crawling.fs_module import change_df

###################################
# 투자지표 데이터프레임 만들기
###################################
def make_invest_dataframe(firm_code):
    invest_url = "http://comp.fnguide.com/SVO2/ASP/SVD_Invest.asp?" \
             "pGB=1&cID=&MenuYn=Y&ReportGB=D&NewMenuID=105&stkGb=701" \
             "&gicode=" + firm_code
    # fr_url = "http://comp.fnguide.com/SVO2/ASP/SVD_FinanceRatio.asp?pGB=1&gicode=A005380&cID=&MenuYn=Y&ReportGB=&NewMenuID=104&stkGb=701"
    invest_page = requests.get(invest_url)

    # 판다스로 테이블 데이터만 찾아서 데이터프레임으로 만들어냄
    invest_tables = pd.read_html(invest_page.text)
    #print(invest_tables)

    temp_df = invest_tables[1]

    # 인덱스로 특정 항목 설정
    temp_df = temp_df.set_index(temp_df.columns[0])
    # print(temp_df)

    # 필요없는 컬럼 제거하기
    #temp_df = temp_df[temp_df.columns[:4]]

    # 필요한 행만 선택하기
    temp_df = temp_df.loc[
        ['PER계산에 참여한 계정 펼치기',
         'PCR계산에 참여한 계정 펼치기',
         'PSR계산에 참여한 계정 펼치기',
         'PBR계산에 참여한 계정 펼치기',
         '총현금흐름']
    ]

    # 인덱스 명칭 변경
    temp_df.index = ['PER', 'PCR', 'PSR', 'PBR', '총현금흐름']

    return temp_df

if __name__ == "__main__":
    # df = make_invest_dataframe('A005930')
    # print(df)

    firmcode_list = ['A005930', 'A005380', 'A035420', 'A003550', 'A034730']
    for num, code in enumerate(firmcode_list):
        invest_df = make_invest_dataframe(code)
        invest_df_changed = change_df(code, invest_df)

        if num == 0:
            total_invest = invest_df_changed
        else:
            total_invest = pd.concat([total_invest, invest_df_changed])

    print(total_invest)