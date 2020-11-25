from collections import OrderedDict

# 기본 딕셔너리
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

print(d)

# 키(key)를 기준으로 정렬한 OrderedDict
ordered_d1 = OrderedDict(sorted(d.items(), key=lambda t: t[0]))
print(ordered_d1)

# 값(value)를 기준으로 정렬한 OrderedDict
ordered_d2 = OrderedDict(sorted(d.items(), key=lambda t:t[1]))
print(ordered_d2)

# 키(key)의 길이(len)를 기준으로 정렬한 OrderedDict
ordered_d3 = OrderedDict(sorted(d.items(), key=lambda t:len(t[0])))
print(ordered_d3)

# ordered_d1에 새로운 아이템 추가
ordered_d1.update({'grape': 5})
print(ordered_d1)

def orderedDict_example():
    pairs = [("c", 1), ("b", 2), ("a", 3)]

    # 일반 딕셔너리
    d1 = {}
    for key, value in pairs:
        if key not in d1:
            d1[key] = []
        d1[key].append(value)

    for key in d1:
        print(key, d1[key])

    # OrderedDict
    d2 = OrderedDict(pairs)
    for key in d2:
        print(key, d2[key])


if __name__ == "__main__":
    orderedDict_example()
