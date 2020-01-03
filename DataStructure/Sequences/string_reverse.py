# 문자열 반전하기
def revert(s):
    if s:
        s = s[-1] + revert(s[:-1])

    return s

def revert2(s):
    return s[::-1]

def rev_str(s):
    new_word = []
    slist = s.split(" ")
    #slist.reverse()                # 역순으로 만들기
    #for word in slist:
    for word in slist[::-1]:        # 뒤에서 부터 하나씩 가져오기
        new_word.append(word)

    return " ".join(new_word)

if __name__ ==  "__main__":
    str1 = "안녕 우리들 세상아~"
    str2 = revert(str1)
    str3 = revert2(str2)

    print(str2)
    print(str3)

    str4 = rev_str(str1)
    print(str4)