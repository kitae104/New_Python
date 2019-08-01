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

ul = bs_obj.find("ul")
print(ul)       # 첫번째 ul 태그 정보를 추출

hello = bs_obj.find("li")   # 첫번째만 가져옴
print(hello)                # <li>hello</li> 형태로 출력
print(hello.text)           # hello 만 출력

# 모든 li 태그 가져오기 --> findAll을 사용하면 모든 li를 리스트로 반환
lis = bs_obj.findAll("li")
print(lis)
# [<li>hello</li>, <li>bye</li>, <li>welcome</li>, <li>ok</li>, <li>no</li>, <li>sure</li>]

for li in lis:
    print(li)
# <li>hello</li>
# <li>bye</li>
# <li>welcome</li>
# <li>ok</li>
# <li>no</li>
# <li>sure</li>

# byt만 출력하기 --> 리스트에서 특정 원소만 접근
print(lis[1].text)

# 리스트에서 특정 위치에 있는 내용만 출력하기
for li in lis[1:2]:
    print(li.text)