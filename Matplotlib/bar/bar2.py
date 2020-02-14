# 가로형 막대 그래프
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate       # 결과 테이블 형태로 출력

# 한글 처리
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/malgun.ttf"   #폰트파일의 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# IPyhton 디스플레이 설정 변경
pd.set_option('display.max_columns', 10)    # 보여지는 열의 개수(안보이는 부분은 ... 으로)
pd.set_option('display.max_colwidth', 10)    # 출력할 열의 너비

# Excel 데이터를 데이터프레임 변환
df = pd.read_excel("../datas/시도별 전출입 인구수.xlsx", fillna=0, header=0)

# 전출지별에서 누락값(NaN)을 앞 데이터로 채움 (엑셀 양식 병합 부분)
df = df.fillna(method='ffill')

# 서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

# 서울에서 '충청남도','경상북도', '강원도', '전라남도'로 이동한 인구 데이터 값만 선택
col_years = list(map(str, range(2010, 2018)))
df_4 = df_seoul.loc[['충청남도','경상북도', '강원도', '전라남도'], col_years]

# 2010-2017년 이동 인구 수를 합계하여 새로운 열로 추가
df_4['합계'] = df_4.sum(axis=1)   # 행정보 합계

# 합계 부분만 가장 큰 값부터 정렬
df_total = df_4[['합계', '2010']].sort_values(by='합계', ascending=True)
# print(tabulate(df_total, headers='keys', tablefmt='psql'))

# 스타일 서식 지정
plt.style.use('ggplot')

# 막대 그래프 그리기
df_total.plot(kind='barh', figsize=(10, 5), width=0.5, color=['orange','skyblue'])

plt.title('서울 -> 타시도 인구 이동', size=30)
plt.ylabel('전입지', size=20)
plt.xlabel('이동인구수', size=20)
# plt.ylim(5000, 30000)
plt.legend(loc='best', fontsize=15)

plt.show()