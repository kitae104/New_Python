# 네이버 금용에서 필요한 정보 가져오기
# 회사 코드를 입력하면 주식 가젹 가져오기
import requests
from bs4 import BeautifulSoup

# url을 넣어서 bs_obj를 반환하는 함수
def get_bs_obj(company_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

# company_code를 받아서 price를 반환하는 함수
def get_price(company_code):
    bs_obj = get_bs_obj(company_code)
    no_today = bs_obj.find("p", {"class":"no_today"})
    blind = no_today.find("span", {"class":"blind"})
    return blind.text

def get_candle_chart_data(company_code):
    bs_obj = get_bs_obj(company_code)

    td_first = bs_obj.find("td", {"class":"first"})
    blind = td_first.find("span", {"class":"blind"})

    # close 종가(전일)
    close = blind.text

    # high 고가
    table = bs_obj.find("table", {"class":"no_info"})
    trs = table.findAll("tr")
    first_tr = trs[0]
    first_tr_tds = first_tr.findAll("td")
    first_tr_tds_second_td = first_tr_tds[1]
    high = first_tr_tds_second_td.find("span", {"class":"blind"}).text

    # open 시가
    second_tr = trs[1]
    second_tr_tds = second_tr.findAll("td")
    second_tr_tds_first_td = second_tr_tds[0]
    open = second_tr_tds_first_td.find("span", {"class": "blind"}).text

    # low 저가
    second_tr_tds_second_td = second_tr_tds[1]
    low = second_tr_tds_second_td.find("span", {"class": "blind"}).text

    return {"close" : close, "high" : high, "open": open, "low" : low}

# 시가, 종가, 고가, 저가 가져오기
candle_chart_data = get_candle_chart_data("000660")
print(candle_chart_data)

# 여러 정보 한번에 가져오기
company_codes = ["005930", "000660", "005680"]
for code in company_codes:
    print(code)
    candle_chart = get_candle_chart_data(code)
    print(candle_chart)