# 실시간 검색어
import requests
import bs4

naver_url = "https://www.naver.com/"
naver_response = requests.get(naver_url)
# print(naver_response.text)

naver_bs = bs4.BeautifulSoup(naver_response.text, 'lxml')
# print(naver_bs)

# result = naver_bs.find('span', class_='ah_k')
result_list = naver_bs.find_all('span', class_='ah_k')
# print(result_list)
print(result_list[0].text)

for span in result_list:
    print(span.text)


