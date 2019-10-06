# 네이버 검색결과 키워드별로 불러와 파일로 저장하기
from Crawler.lib_crawler.naver_api_caller import get1000Result
import json

list = []
result = get1000Result("강남역 맛집")
result2 = get1000Result("강남역 찻집")
list = list + result + result2

file = open("./gangnam.json", "w+")
file.write(json.dumps(list))


