# 전종목 코드 구해오기
import pandas as pd
import time
import requests
from Quant_Strategy.Crawling.fs_module import make_fs_dataframe, change_df
from Quant_Strategy.Crawling.fr_module import make_fr_dataframe
from Quant_Strategy.Crawling.invest_module import make_invest_dataframe

# 코드를 특정 형태로 만들기
def make_code(x):
    x = str(x)
    return 'A' + '0' * (6 - len(x)) + x

if __name__ == "__main__":
    path = r'D:\Projects\New_Python\Quant_Strategy\datas\data_191117.xls'
    code_data = pd.read_excel(path)
    code_data = code_data[['종목코드','기업명']]

    # apply : 특정 컬럼 전체에 주어진 함수 적용
    code_data['종목코드'] = code_data['종목코드'].apply(make_code)
    # print(code_data)

    # 모든 종목에 대해 재무제표 데이터 가져오기
    for num, code in enumerate(code_data['종목코드']):
        try:
            print(num, code)    # 순서와 현재 코드 출력
            time.sleep(1)       # 잠시 딜레이 제공

            try:
                fs_df = make_fs_dataframe(code)
            except requests.exceptions.Timeout:     # 시간 초과 예외
                time.sleep(60)
                fs_df = make_fs_dataframe(code)     # 일정 시간 경과후 다시 시도

            fs_df_changed = change_df(code, fs_df)

            if num == 0:
                total_fs = fs_df_changed
            else:
                total_fs = pd.concat([total_fs, fs_df_changed])

        except ValueError:
            continue        # 항목이 없거나 오류가 있는 경우를 위해 예외 처리
        except KeyError:
            continue

    total_fs.to_excel(r'D:\Projects\New_Python\Quant_Strategy\Crawling\results\재무제표데이터.xlsx')
    print(total_fs)

    # 모든 종목에 대해 재무비율 데이터 가져오기
    for num, code in enumerate(code_data['종목코드']):
        try:
            print(num, code)    # 순서와 현재 코드 출력
            time.sleep(1)       # 잠시 딜레이 제공

            try:
                fr_df = make_fr_dataframe(code)
            except requests.exceptions.Timeout:     # 시간 초과 예외
                time.sleep(60)
                fr_df = make_fr_dataframe(code)     # 일정 시간 경과후 다시 시도

            fr_changed = change_df(code, fr_df)

            if num == 0:                            # 재무비율 데이터를 데이터프레임 하나로 모으기
                total_fr = fr_changed
            else:
                total_fr = pd.concat([total_fr, fr_changed])
        except ValueError:      # 항목이 없거나 오류가 있는 경우를 위해 예외 처리
            continue
        except KeyError:
            continue

    total_fr.to_excel(r'D:\Projects\New_Python\Quant_Strategy\Crawling\results\재무비율데이터.xlsx')
    print(total_fr)

    # 모든 종목에 대해 투자지표 데이터 가져오기
    for num, code in enumerate(code_data['종목코드']):
        try:
            print(num, code)    # 순서와 현재 코드 출력
            time.sleep(1)       # 잠시 딜레이 제공

            try:
                invest_df = make_invest_dataframe(code)
            except requests.exceptions.Timeout:     # 시간 초과 예외
                time.sleep(60)
                invest_df = make_invest_dataframe(code)     # 일정 시간 경과후 다시 시도

            invest_changed = change_df(code, invest_df)

            if num == 0:                            # 재무비율 데이터를 데이터프레임 하나로 모으기
                total_invest = invest_changed
            else:
                total_invest = pd.concat([total_invest, invest_changed])
        except ValueError:      # 항목이 없거나 오류가 있는 경우를 위해 예외 처리
            continue
        except KeyError:
            continue

    total_invest.to_excel(r'D:\Projects\New_Python\Quant_Strategy\Crawling\results\투자지표데이터.xlsx')
    print(total_invest)