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
print(bs_obj)