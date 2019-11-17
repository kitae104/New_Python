import pandas as pd
import requests
from Quant_Strategy.Crawling.fs_module import change_df

###################################
# 재무 비율 데이터프레임 만들기
###################################
def make_fr_dataframe(firm_code):
    fr_url = "http://comp.fnguide.com/SVO2/ASP/SVD_FinanceRatio.asp?" \
             "pGB=1&cID=&MenuYn=Y&ReportGB=D&NewMenuID=104&stkGb=701" \
             "&gicode=" + firm_code
    # fr_url = "http://comp.fnguide.com/SVO2/ASP/SVD_FinanceRatio.asp?pGB=1&gicode=A005380&cID=&MenuYn=Y&ReportGB=&NewMenuID=104&stkGb=701"
    fr_page = requests.get(fr_url)

    # 판다스로 테이블 데이터만 찾아서 데이터프레임으로 만들어냄
    fr_tables = pd.read_html(fr_page.text)
    #print(fr_tables)

    temp_df = fr_tables[0]

    # 인덱스로 특정 항목 설정
    temp_df = temp_df.set_index(temp_df.columns[0])

    # 필요없는 컬럼 제거하기
    temp_df = temp_df[temp_df.columns["2015/12", "2016/12", "2017/12", "2018/12", "2019/06"]]

    # 필요한 행만 선택하기
    temp_df = temp_df.loc[
        ['유동비율계산에 참여한 계정 펼치기',
         '부채비율계산에 참여한 계정 펼치기',
         '영업이익률계산에 참여한 계정 펼치기',
         'ROA계산에 참여한 계정 펼치기',
         'ROIC계산에 참여한 계정 펼치기']
    ]

    # 인덱스 명칭 변경
    temp_df.index = ['유동비율', '부채비율', '영업이익률', 'ROA', 'ROIC']

    return temp_df

if __name__ == "__main__":

    firmcode_list = ['A005930', 'A005380', 'A035420', 'A003550', 'A034730']
    for num, code in enumerate(firmcode_list):
        fr_df = make_fr_dataframe(code)
        fr_df_changed = change_df(code, fr_df)

        if num == 0:
            total_fr = fr_df_changed
        else:
            total_fr = pd.concat([total_fr, fr_df_changed])

    print(total_fr)