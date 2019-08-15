# 쇼핑몰 상품 정보 수집하기
import requests
import Crawler.lib_crawler.crawler as crawler

url = "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3301&mallGb=KOR&orderClick=sgx"
result = crawler.crawl(url)
print(result)
