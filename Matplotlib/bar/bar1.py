# 세로형 막대 그래프
import pandas as pd
import matplotlib.pyplot as plt

# 한글 처리
from matplotlib import font_manager, rc
font_path = "../datas/시도별 전출입 인구수.xlsx" # 폰트 경로
font_name = font_manager.FontProperties(fname=font_path).getName()
rc('font', family=font_name)