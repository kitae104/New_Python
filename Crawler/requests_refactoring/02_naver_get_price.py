# 회사 코드를 입력하면 주식 가젹 가져오기
import requests
from bs4 import BeautifulSoup

# url을 넣어서 bs_obj를 반환하는 함수
def get_bs_obj(url):
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

# company_code를 받아서 price를 반환하는 함수
def get_price(compay_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + compay_code
    bs_obj = get_bs_obj(url)
    no_today = bs_obj.find("p", {"class":"no_today"})
    blind = no_today.find("span", {"class":"blind"})
    return blind.text

price_samsung = get_price("005930")
print(price_samsung)

price_sk_hynix = get_price("000660")
print(price_sk_hynix)