import sys
import glob
import js
import matplotlib.pyplot as plt
import numpy as np
import PIL
from PIL import Image

# 이미지 열기
print(PIL.__version__);
fp = open("./data/bad.png", "rb")
print(fp.fileno().__sizeof__())



