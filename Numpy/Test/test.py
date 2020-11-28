import numpy as np
import pandas as pd

data = {
    'year': [2016, 2017, 2018],
    'GDP rate': [2.8, 3.1, 3.0],
    'GDP': ['1.637M', '1.73M', '1.83M']
}

df = pd.DataFrame(data)
print(df)
'''
   year  GDP rate     GDP
0  2016       2.8  1.637M
1  2017       3.1   1.73M
2  2018       3.0   1.83M
'''

a = np.array(df)
print(a)
'''
[[2016 2.8 '1.637M']
 [2017 3.1 '1.73M']
 [2018 3.0 '1.83M']]
'''

b = np.array(df).reshape(-1, 3)
print(b)
'''
[[2016 2.8 '1.637M']
 [2017 3.1 '1.73M']
 [2018 3.0 '1.83M']]
'''

c = np.array(df).reshape(-1, 1)
print(c)
'''
[[2016]
 [2.8]
 ['1.637M']
 [2017]
 [3.1]
 ['1.73M']
 [2018]
 [3.0]
 ['1.83M']]
'''

d = np.array(df).reshape(1, -1)
print(d)
'''
[[2016 2.8 '1.637M' 2017 3.1 '1.73M' 2018 3.0 '1.83M']]
'''

e = np.array(df).reshape(3, -1)
print(e)
'''
[[2016 2.8 '1.637M']
 [2017 3.1 '1.73M']
 [2018 3.0 '1.83M']]
'''

f = np.array(df).reshape(9, -1)
print(f)
'''
[[2016]
 [2.8]
 ['1.637M']
 [2017]
 [3.1]
 ['1.73M']
 [2018]
 [3.0]
 ['1.83M']]
'''