# 문자열 조합
def conbinations(s):
    if len(s) < 2:
        return s
    res = []
    for i, c in enumerate(s):
        res.append(c)
        for j in conbinations(s[:i] + s[i+1:]):
            res.append(c + j)
    return res

if __name__ == "__main__":
    result = conbinations("abc")
    print(len(result),':', result)
