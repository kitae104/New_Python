#선 그래프
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

print(len(sr_one))
print(sr_one.head(), '\n')

# print(sr_one.index, '\n')
# print(sr_one.values, '\n')

# 스타일 서식 지정
plt.style.use('ggplot')

# 그림 사이즈 지정(가로 10인치, 세로 6인치)
plt.figure(figsize=(12, 6))

# x, y축 데이터를 plot 함수에 입력
# plt.plot(sr_one.index, sr_one.values)
# 스타일 문자열은 색깔(color), 마커(marker), 선 종류(line style)의 순서로 지정한다. 
plt.plot(sr_one, marker='o', markersize=10) # 마커 표시

# x축 눈금 라벨 회전하기
plt.xticks(size=10, rotation=90)     # 90도 회전(반시계 방향)
# plt.xticks(rotation='vertical')     # 90도 회전

# 차트 제목 추가
plt.title('서울 -> 경기 인구 이동', size=30)

# 축이름 추가
plt.xlabel('기간', size=15)
plt.ylabel('이동 인구수', size=15)

#범례 표시
plt.legend(labels=['서울->경기'], loc='best', fontsize=13)

# y축 범위 지정 (최소값, 최대값)
plt.ylim(50000, 800000)     # y축 범위 늘리기

# 주석 표시 - 화살표
plt.annotate('',
             xy=(20, 620000),       #화살표의 머리 부분(끝점) - x는 인덱스 번호
             xytext=(2, 290000),    #화살표의 꼬리 부분(시작점) - y는 데이터 위치
             xycoords='data',       #좌표체계
             arrowprops=dict(arrowstyle='->', color='skyblue', lw=5), #화살표 서식
             )

plt.annotate('',
             xy=(47, 450000),       #화살표의 머리 부분(끝점)
             xytext=(30, 580000),   #화살표의 꼬리 부분(시작점)
             xycoords='data',       #좌표체계
             arrowprops=dict(arrowstyle='->', color='olive', lw=5),  #화살표 서식
             )

# 주석 표시 - 텍스트
plt.annotate('인구이동 증가(1970-1995)',  #텍스트 입력
             xy=(10, 550000),            #텍스트 위치 기준점
             rotation=25,                #텍스트 회전각도(반시계방향)
             va='baseline',              #텍스트 상하 정렬
             ha='center',                #텍스트 좌우 정렬
             fontsize=15,                #텍스트 크기
             )

plt.annotate('인구이동 감소(1995-2017)',  #텍스트 입력
             xy=(40, 560000),            #텍스트 위치 기준점
             rotation=-11,               #텍스트 회전각도
             va='baseline',              #텍스트 상하 정렬
             ha='center',                #텍스트 좌우 정렬
             fontsize=15,                #텍스트 크기
             )


# 출력
plt.show()