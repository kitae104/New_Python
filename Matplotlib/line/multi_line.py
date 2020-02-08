# 같은 화면에 그래프 추가
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

# 한글 폰트 처리
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
df_seoul = df_seoul.drop(['전출지별'], axis=1)  # 해당 컬럼 제거
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

# 서울에서 '충청남도','경상북도', '강원도'로 이동한 인구 데이터 값만 선택
col_years = list(map(str, range(1970, 2018)))   # 기간을 문자열로 변환
print(col_years)

# 해당 행과 해당 컬럼을 가지고 df_3 생성
df_3 = df_seoul.loc[['충청남도','경상북도', '강원도'], col_years]
# print(tabulate(df_3.head(), headers='keys', tablefmt='psql'))

# 스타일 서식 지정
plt.style.use('ggplot')

# 그래프 객체 생성 (figure에 1개의 서브 플롯을 생성)
fig = plt.figure(figsize=(14, 5))
ax = fig.add_subplot(1,1,1)     # 1개의 서브 플롯

# axe 객체에 plot 함수로 그래프 출력(여러개 추가)
ax.plot(col_years, df_3.loc['충청남도', :], marker='o', markerfacecolor='green', markersize=10, color='olive', linewidth=2, label='서울->충남')
ax.plot(col_years, df_3.loc['경상북도', :], marker='o', markerfacecolor='blue', markersize=10, color='skyblue', linewidth=2, label='서울->충남')
ax.plot(col_years, df_3.loc['강원도', :], marker='o', markerfacecolor='red', markersize=10, color='magenta', linewidth=2, label='서울->충남')

# 범례 표시
ax.legend(loc='best')

# 차트 제목 추가
ax.set_title('서울 -> 충남, 경북, 강원 인구 이동', size=20)

# 축이름 추가
ax.set_xlabel('기간', size=12)
ax.set_ylabel('이동 인구수', size = 12)

# 축 눈금 라벨 지정 및 90도 회전
ax.set_xticklabels(col_years, rotation=45)

# 축 눈금 라벨 크기
ax.tick_params(axis="x", labelsize=10)
ax.tick_params(axis="y", labelsize=10)

plt.show()