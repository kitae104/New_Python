import operator
from collections import OrderedDict

# 기본 딕셔너리
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

# 키(key)를 기준으로 정렬한 OrderedDict
ordered_d = OrderedDict(sorted(d.items(), key=operator.itemgetter(0), reverse=False))
print(ordered_d)

# move_to_end(key, last=True)인 경우: 해당 (key, value)가 맨 오른쪽(뒤)으로 이동함
ordered_d.move_to_end('banana', last=True)
print("move_to_end('banana', last=True) >>> {}".format(ordered_d))

# move_to_end(key, last=False)인 경우: 해당 (key, value)가 맨 왼쪽(앞)으로 이동함
ordered_d.move_to_end('banana', last=False)
print("move_to_end('banana', last=False) >>> {}".format(ordered_d))
