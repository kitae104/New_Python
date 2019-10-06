import requests
from urllib.parse import quote

def get1000Result(keyword):
    list = []
    for num in range(0, 10):
        list = list + call("강남역 맛집", num * 100 + 1)['items']
    return list

def call(keyword, start):
    encText = quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&display=100" + "&start="+str(start)
    result = requests.get(url,
                          headers={"X-Naver-Client-Id": "b8nqJPaL_YGrUy_PQ5qO",
                                   "X-Naver-Client-Secret": "zNI58zPp8v"})
    print(result)
    return result.json()



