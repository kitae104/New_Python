import bs4

html_str = """ 
<html>
    <body>
        <ul class="greet">
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
        <ul class="reply">
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        </ul>
    </body>
</html>
"""

# 해당 문자열을 html.parser 를 통해서 읽어와 객체를 생성
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
# print(bs_obj)

ul_greet = bs_obj.find("ul")    # 첫번째 ul 추출
# print(ul_reply)

# 태그와 속성을 함께 사용해서 정보 추출
ul_reply = bs_obj.find("ul", {"class":"reply"}) # class 속성이 reply인 경우 추출
print(ul_reply)

lis = ul_reply.findAll("li")
print(lis)

for li in lis:
    print(li)

for li in lis:
    print(li.text)