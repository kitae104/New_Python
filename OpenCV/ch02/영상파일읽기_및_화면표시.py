# 영상 파일 읽기 및 화면 표시
import cv2

imageFile = "../data/lena.jpg"
img = cv2.imread(imageFile, cv2.IMREAD_COLOR)   # 컬러
img2 = cv2.imread(imageFile, 0)                 # 0 : 그래이 스케일 cv2.IMREAD_GRAYSCALE

cv2.imshow('Lena Color', img)
cv2.imshow('Lena Grayscale', img2)

cv2.waitKey()                       # 키보드 입력 대기
cv2.destroyAllWindows()             # 모든 윈도우 파괴
