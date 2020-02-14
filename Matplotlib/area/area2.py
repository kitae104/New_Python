# 면적 그래프 (stacked=True) 인 경우
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate       # 결과 테이블 형태로 출력

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

# 전출지별에서 누락값(NaN)을 앞 데이터로 채움
df = df.fillna(method='ffill')

# 서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]     # mask에 해당하는 데이터만 추출해서 새로운 데이터프레임 생성
df_seoul = df_seoul.drop(['전출지별'], axis=1)  # 해당 컬럼 삭제
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)   # 컬럼 이름 변경
df_seoul.set_index(['전입지'], inplace=True)   # 새로운 인덱스 설정

# 서울에서 '충청남도','경상북도', '강원도', '전라남도'로 이동한 인구 데이터 값만 선택
col_year = list(map(str, range(1970, 2018)))    # 연도 정보를 문자열 리스트로 변경
df_4 = df_seoul.loc[['충청남도','경상북도', '강원도', '전라남도'], col_year]
df_4 = df_4.transpose()   # 행과 열을 전치
# print(tabulate(df_4, headers='keys', tablefmt='psql'))

# 스타일 서식 지정
plt.style.use('ggplot')

# 데이터프레임의 인덱스를 정수형으로 변경 (x축 눈금 라벨 표시)
df_4.index = df_4.index.map(int)

# 면적 그래프 그리기
df_4.plot(kind='area', stacked=True, alpha=0.2, figsize=(10, 5))

plt.title('서울 -> 타시도 인구 이동', size=30, color='brown', weight='bold')
plt.ylabel('이동 인구 수', size=20, color='blue')
plt.xlabel('기간', size=20, color='blue')
plt.legend(loc='best', fontsize=15)

plt.show()



