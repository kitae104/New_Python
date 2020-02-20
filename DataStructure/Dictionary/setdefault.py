# 딕셔너리 메소드
# setdefault 사용하기
def usual_dict(dict_data):
    """ dict[key] 사용 """
    newdata = {}
    for k, v in dict_data:
        if k in newdata:
            newdata[k].append(v)
        else:
            newdata[k] = [v]

    return newdata

def setdefault_dict(dict_data):
    """ setdefault() 메서드 사용 """
    newdata = {}
    for k, v in dict_data:
        newdata.setdefault(k, []).append(v)

    return newdata

if __name__ == "__main__":
    dict_data = (("key1", "value1"),
                 ("key1", "value2"),
                 ("key2", "value3"),
                 ("key2", "value4"),
                 ("key2", "value5"))

    print(usual_dict(dict_data))
    print(setdefault_dict(dict_data))

# update
d = {'a':1, 'b':2}
print(d)
d.update({'b':10})      # 해당 키가 있으면 갱신
print(d)
d.update({'c':20})      # 없으면 추가
print(d)

# get
dic1 = dict(name='AAA', age=17, hobby='game')
print(dic1.get('name'))
print(dic1['name'])
# print(dic1['ABC'])    # 없으면 오류

# items, values, keys
dic = dict(name='AAA', age=17, hobby='game')
print(dic.items())
print(dic.values())
print(dic.keys())

dic_copy = dic.items()              # 읽기 전용객체 생성
#print(dic)
#dic_copy['address'] = 'seoul'
print(dic_copy)

dic['address'] = 'seoul'        # 원본은 추가가능
print(dic)
print(dic_copy)                   # 변경 사항 적용됨

# pop, popitem
dic = dict(name='AAA', age=17, hobby='game', address = 'seoul')
res = dic.pop('age')        # 해당 키는 제거되고 값은 반환됨
print(res)
print(dic)

res = dic.popitem()     # 맨마지막 아이템 반환
print(res)
print(dic)

# clear
dic.clear()
print(dic)