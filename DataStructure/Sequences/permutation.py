# 문자열 순열 : 서로다른 n개 중에 r개를 골라 순서를 고려해 나열한 경우의 수
import itertools

def perm(s):
    if len(s) < 2:
        return s
    res = []
    for i, c in enumerate(s):
        print(s[:i], '+' , s[i+1:])
        for cc in perm(s[:i] + s[i+1:]):
            res.append(c+cc)
    return res

def perm2(s):
    res = itertools.permutations(s)
    return ["".join(i) for i in res]

if __name__ == "__main__":
    val = "012"
    print(perm(val))
    print(perm2(val))