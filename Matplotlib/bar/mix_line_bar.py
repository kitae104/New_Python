# 2축 그래프 그리기
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

# 한글 처리
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# Excel 데이터를 데이터프레임 변환
df = pd.read_excel("../datas/남북한발전전력량.xlsx", convert_float=True)
df = df.loc[5:9]
df.drop('전력량 (억㎾h)', axis='columns', inplace=True)
df.set_index("발전 전력별", inplace=True)
print(tabulate(df, headers='keys', tablefmt='psql'))
df = df.T
print(tabulate(df, headers='keys', tablefmt='psql'))

# 증감율(변동률) 계산
df = df.rename(columns={'합계':'총발전량'})
df['총발전량-1년'] = df['총발전량'].shift()  # 열의 데이터를 1행씩 뒤로 이동
df['증감률'] = ((df['총발전량']/df['총발전량-1년']) -1) * 100 # % 계산
print(tabulate(df, headers='keys', tablefmt='psql'))

# 그래프 설정
plt.style.use('ggplot')                         # 스타일 서식 지정
plt.rcParams['axes.unicode_minus'] = False    # 마이너스 부호 출력 설정

# 2축 그래프 그리기
ax1 = df[['수력', '화력']].plot(kind='bar', figsize=(10, 5), width=0.7, stacked=True)  # 쌓아올린 형태
ax2 = ax1.twinx()   # 쌍둥이 객체 생성
ax2.plot(df.증감률, ls='--', marker='o', markersize=5, color='green', label='전년대비 증감률(%)')

ax1.set_ylim(0, 500)
ax2.set_ylim(-50, 50)

ax1.set_xlabel('연도', size=20)
ax1.set_ylabel('발전량(억 KWh)')
ax2.set_ylabel('전년 대비 증감율(%)')

plt.title('북한 전력 발전량 (1990 ~ 2016)', size=30)
ax1.legend(loc='upper left')

plt.show()