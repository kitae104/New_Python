# -*- coding: utf-8 -*-
# axe 객체 그래프 꾸미기
import pandas as pd
import matplotlib.pyplot as plt

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
print(df.head())

# fillna : 누락 데이터가 들어있는 행의 바로 앞에 위치한 행의 데이터 값으로 채운다
# 전출지별에서 누락값(NaN)을 앞 데이터로 채움 (엑셀 양식 병합 부분)
df = df.fillna(method='ffill')
print(df.head())

# 서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
# 해당되는 mask에는 True가 설정됨
mask = (df['전출지별'] =='서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]     # 서울이 전출지인것만 선택됨
df_seoul = df_seoul.drop(['전출지별'], axis=1)  # 전출지별 컬럼 지우기
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)
print(len(df_seoul))
print(df_seoul.head(), '\n')

# 서울에서 경기도로 이동한 인구 데이터 값만 선택
sr_one = df_seoul.loc['경기도']

# 스타일 서식 지정
plt.style.use('ggplot')

# 그래프 객체 생성 (figure에 2개의 서브 플롯을 생성)
fig = plt.figure(figsize=(20, 5))

# 그림틀 분할 AxesSubplot으로 생성
ax = fig.add_subplot(1, 1, 1)  # 행크기, 열크기, 서브플롯 순서

# x, y축 데이터를 plot 함수에 입력
ax.plot(sr_one, marker='o', markerfacecolor='orange', markersize=10, color='olive', linewidth=2, label='서울->경기')
ax.legend(loc='best')

#y축 범위 지정 (최소값, 최대값)
ax.set_ylim(50000, 800000)

# 축 눈금 라벨 지정 및 75도 회전
ax.set_xticklabels(sr_one.index, rotation=75)

# 축 눈금 라벨 크기
ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)

# 차트 제목 추가
ax.set_title('서울 -> 경기 인구 이동', size=20)

# 축이름 추가
ax.set_xlabel('기간', size=12)
ax.set_ylabel('이동 인구수', size=12)

# 출력
plt.show()