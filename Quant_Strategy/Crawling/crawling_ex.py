import requests

naver_url = "https://www.naver.com/"
naver_response = requests.get(naver_url)
print(naver_response.text)
