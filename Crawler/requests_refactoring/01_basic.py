import requests
from bs4 import BeautifulSoup

# url을 넣어서 bs_obj를 반환하는 함수
def get_bs_obj(url):
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

url = "https://finance.naver.com/item/main.nhn?code=005930"
bs_obj = get_bs_obj(url)
print(bs_obj)