# 예제-2 OrderedDict.popitem()

import operator
from collections import OrderedDict

# 기본 딕셔너리
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

# 키(key)를 기준으로 정렬한 OrderedDict
ordered_d = OrderedDict(sorted(d.items(), key=operator.itemgetter(0), reverse=False))
print(ordered_d)

# popitem(last=True) 일경우 : LIFO(Last In Last Out)방식으로 pop, default는 True임
for i in range(len(ordered_d)):
    print(ordered_d.popitem(last=True))

print('=' * 50)

# 키(key)를 기준으로 정렬한 OrderedDict
ordered_d = OrderedDict(sorted(d.items(), key=operator.itemgetter(0), reverse=False))
print(ordered_d)

# popitem(last=False) 일경우 : FIFO(First In First Out)방식으로 pop
for i in range(len(ordered_d)):
    print(ordered_d.popitem(last=False))

