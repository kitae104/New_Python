# 판다스를 이용한 데이터 분석 연습
# import pandas as pd
#
# s = pd.Series([100, 500, 150], index=['카카오', '삼성전자', '현대차'])
# print(s)
# print(s['카카오'])
# print(s[1])
#
# df = pd.DataFrame({'가격':[100, 500, 150], 'PER':[0.5, 1.2, 0.2], 'ROA':[1.01, 3.1, 0.97]}, index=['카카오', '삼성전자', '현대차'])
# print(df)                       # 데이터 프레임 출력
# print(df['가격'])               # 데이터 프레임에서 특정 열 가져오기
# print(df['가격']['삼성전자'])  # 데이터 프레임에서 특정 데이터 가져오기
#
# print(df.loc['카카오'])         # 데이터 프레임에서 특정 행을 기준으로 선택하기
# print(df.loc['카카오']['ROA'])  # 데이터 프레임에서 특정 데이터 가져오기
#
# df2 = pd.DataFrame({'가격':[100, 140, 155, 70, 90],
#                     'PER':[1.1, 0.8, 0.7, 2.3, 3.9],
#                     '거래량':[1000, 800, 890, 700, 2000]},
#                    index=['a', 'b','c', 'd', 'e'])
#
# print(df2)
# print(df2['가격'])
# print(df2[df2['가격'] >= 100]) # 가격이 100이상 사람만 출력
# print(df2[df2['거래량'] < 1000])  # 거래량이 1000 미만인 데이터 출력
#
# # 특정 데이터를 오름차순 정렬해서 가져오기
# print(df2["PER"].sort_values())
# # c    0.7
# # b    0.8
# # a    1.1
# # d    2.3
# # e    3.9
# # Name: PER, dtype: float64
#
# # 특정 데이터를 내림차순 정렬해서 가져오기
# print(df2["PER"].sort_values(ascending=False))
# # e    3.9
# # d    2.3
# # a    1.1
# # b    0.8
# # c    0.7
# # Name: PER, dtype: float64
#
# # 특정 컬럼을 기준으로 데이터 프레임 정렬하기
# print(df2.sort_values(by="PER"))
# #     가격  PER   거래량
# # c  155  0.7   890
# # b  140  0.8   800
# # a  100  1.1  1000
# # d   70  2.3   700
# # e   90  3.9  2000
#
# # 특정 컬럼을 기준으로 데이터 프레임 내림 차순으로 정렬하기
# print(df2.sort_values(by="PER", ascending=False))
# #     가격  PER   거래량
# # e   90  3.9  2000
# # d   70  2.3   700
# # a  100  1.1  1000
# # b  140  0.8   800
# # c  155  0.7   890
#
# # 거래량을 기준으로 순위 만들기 - 작은 수가 1
# print(df2["거래량"].rank())
# # a    4.0
# # b    2.0
# # c    3.0
# # d    1.0
# # e    5.0
# # Name: 거래량, dtype: float64
#
# # 거래량을 기준으로 순위 만들기 - 큰 수가 1
# print(df2["거래량"].rank(ascending=False))
# # a    2.0
# # b    4.0
# # c    3.0
# # d    5.0
# # e    1.0
# # Name: 거래량, dtype: float64