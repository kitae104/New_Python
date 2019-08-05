import requests
from urllib.parse import urlparse

keyword = "디퓨져"
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword # json 결과
result = requests.get(urlparse(url).geturl(),
                      headers={"X-Naver-Client-Id":"Client-Id",
                              "X-Naver-Client-Secret":"Client-Secret"})
json_obj = result.json()
print(json_obj)