import numpy as np
import pandas as pd

df1 = pd.read_csv("../../Utils/datas/samsung.csv", index_col=0,
                  header=0, encoding='cp949', sep=',')