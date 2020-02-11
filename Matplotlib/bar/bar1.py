# 세로형 막대 그래프
import pandas as pd
import matplotlib.pyplot as plt

# 한글 처리
from matplotlib import font_manager, rc
font_path = "../datas/시도별 전출입 인구수.xlsx" # 폰트 경로
font_name = font_manager.FontProperties(fname=font_path).getName()
rc('font', family=font_name)

# IPyhton 디스플레이 설정 변경
pd.set_option('display.max_columns', 10)    # 보여지는 열의 개수(안보이는 부분은 ... 으로)
pd.set_option('display.max_colwidth', 10)    # 출력할 열의 너비