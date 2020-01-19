# 판다스에서 그래프 그리기
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("../../data/남북한발전전력량.xlsx")

df_ns = df.iloc[[0,5], 2:]  # 0과 5번 행에 있는 남한, 북한 발전량 합계 데이터만 추출 3번째 컬럼 부터 추출
df_ns.index = ['남한', '북한']          # 행 인덱스 변경
df_ns.columns = df_ns.columns.map(int)  # 열 이름의 자료형을 정수로 변경
print(df_ns)

# 행과 열을 전치
tdf_ns = df_ns.T
print(tdf_ns.tail())

# 선 그래프 그리기
# plt.plot(tdf_ns.index, tdf_ns.values)   # 인덱스와 값을 입력
# plt.xlabel('년도')    # index 정보
# plt.ylabel("합계")    #
# plt.grid()
# plt.show()

# 바 그래프 그리기
# tdf_ns.plot(kind='bar', figsize=(10, 5), width=0.7, color=['yellow', 'red'])     # 그래프 종류 선택
#
# plt.plot(tdf_ns.index, tdf_ns.values)   # 인덱스와 값을 입력
# plt.xlabel('년도')    # index 정보
# plt.ylabel("합계")    #
# plt.grid()
# plt.show()

tdf_ns.plot(kind='hist')
plt.show()