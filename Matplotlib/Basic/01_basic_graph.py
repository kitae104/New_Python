# 기본 그래프
import matplotlib.pyplot as plt

# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/malgun.ttf"   #폰트파일의 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 그림 크기 지정
plt.figure(figsize=(6, 5))     # 가로 6인치, 세로 5인치

# 축에 대한 정보
plt.axis([0, 6, 0, 10])     # x축은 0~6, y축은 0~10

# 데이터와 모양 선택
plt.plot([1,2,3,4], [2,4, 6, 8])     # 그래프, 파란색 선
# plt.plot([1,2,3,4], [2,4, 6, 8], '*')     # 그래프, 파란색 별표

# 타이틀 설정
plt.title('타이틀')

# x, y 축 라벨
plt.xlabel('x label')   # y측 라벨
plt.ylabel('y label')   # y측 라벨

#범례 표시
plt.legend(labels=['범례1'], loc='best')

# 그래프 보기
plt.show()