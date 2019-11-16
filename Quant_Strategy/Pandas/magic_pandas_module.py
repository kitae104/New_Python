# 마법 공식을 판다스를 이용한 모듈로 작성하기
import pandas as pd

def magic_by_pd(file_path):
    # 엑셀 파일 읽어 오기 - 인덱스 컬럼 설정
    per_data = pd.read_excel(file_path, sheet_name='PER', index_col=0)

    # PER 값이 0보다 작은 경우 필터링
    filtered_per = per_data[per_data['PER']>0]

    # PER 데이터프레임 정렬
    sorted_per = filtered_per.sort_values(by='PER')

    # PER 값으로 순위 만들기
    rank_per = sorted_per['PER'].rank()

    # PER 값으로 작성된 순위를 기존 데이터프레임에 합치기
    sorted_per['PER랭킹'] = sorted_per['PER'].rank()

    # ROA 데이터 읽어 오기
    roa_data = pd.read_excel(file_path, sheet_name='ROA', index_col=0)

    # NaN값 제거하기
    filtered_roa = roa_data.dropna()

    # 컬럼명 변경하기 - 컬럼명을 리스트로 입력
    filtered_roa.columns = ['ROA']

    # 정렬하고 순위 매기기
    sorted_roa = filtered_roa.sort_values(by='ROA', ascending=False)
    rank_roa = sorted_roa['ROA'].rank(ascending=False)
    sorted_roa['ROA랭킹'] = sorted_roa['ROA'].rank(ascending=False)

    # 두 데이터프레임 합치기
    total_df = pd.merge(sorted_per, sorted_roa, how='inner', left_index=True, right_index=True)

    # 종합점수 필드 구하기
    total_df['종합점수'] = (total_df['PER랭킹'] + total_df['ROA랭킹'])

    # 종합등수를 구한후 정렬해서 보여주기
    total_df['종합등수'] = total_df['종합점수'].rank()

    return total_df.sort_values(by='종합등수')

if __name__ == "__main__":
    file_path = "D:\\Projects\\New_Python\\Quant_Strategy\\datas\\마법공식 데이터.xlsx"
    res = magic_by_pd(file_path)
    print(res)