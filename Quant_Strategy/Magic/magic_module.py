import operator
import xlrd     # 엑셀을 사용하기 위한 모듈

def magic(file_path):
    wb = xlrd.open_workbook(file_path)
    per_sh = wb.sheet_by_name("PER")

    per_dict = {}       # 딕셔너리
    for i in range(1, per_sh.nrows):
        data = per_sh.row_values(i)     # i 번째의 행의 내용을 가져온다.
        name = data[0]                  # 회사명 추출
        per = data[1]                   # 회사의 per 추출
        if per > 0:
            per_dict[name] = per        # 딕셔너리에 저장

    # key 값이 아닌 뒤의 데이터를 기준으로 정렬할 경우
    sorted_per = sorted(per_dict.items(), key=operator.itemgetter(1))

    #PER 랭킹 매기기
    per_rank = {}                       # 랭킹을 관리하는 딕셔너리
    for num, firm in enumerate(sorted_per):
        per_rank[firm[0]] = num + 1     # 이름 : 랭킹 형태로 저장

    roa_sh = wb.sheet_by_name("ROA")

    roa_dict = {}

    for i in range(1, roa_sh.nrows):
        data = roa_sh.row_values(i)  # i 번째의 행의 내용을 가져온다.
        name = data[0]      # 회사명 추출
        roa = data[1]       # 회사의 roa 추출
        if roa != '':
            roa_dict[name] = roa  # 딕셔너리에 저장

    # key 값이 아닌 뒤의 데이터를 기준으로 내림 차순으로 정렬할 경우
    sorted_roa = sorted(roa_dict.items(), key=operator.itemgetter(1), reverse=True)

    roa_rank = {}

    for num, firm in enumerate(sorted_roa):
        roa_rank[firm[0]] = num + 1

    # 종합 랭킹 매기기
    total_rank = {}

    for name in roa_rank.keys():
        if name in per_rank.keys():
            total_rank[name] = roa_rank[name] + per_rank[name]

    sorted_total = sorted(total_rank.items(), key=operator.itemgetter(1))

    file_path = "D:\\Projects\\New_Python\\Quant_Strategy\\datas\\마법공식 데이터2.xlsx"

    magic_rank = {}
    for num, firm in enumerate(sorted_total):
        magic_rank[firm[0]] = num + 1

    # 상위 30개 항목 출력하기
    for num, key in enumerate(magic_rank.keys()):
        if num == 30:
            break
        print(key,':',magic_rank[key])

if __name__ == "__main__":
    file_path = "D:\\Projects\\New_Python\\Quant_Strategy\\datas\\마법공식 데이터.xlsx"
    magic(file_path)