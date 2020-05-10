# 영상 파일 저장
import cv2

imageFile = "../data/lena.jpg"
img = cv2.imread(imageFile, cv2.IMREAD_COLOR)   # 컬러

cv2.imwrite('../result/Lena.bmp', img)
cv2.imwrite('../result/Lena.png', img)

# 압축률 9의 png 파일로 생성, 디폴트는 3
cv2.imwrite('../result/Lena2.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])

# 90%의 품질을 갖는 jpg 파일 생성, 품질범위 [0, 100] 높을 수록 좋다.
cv2.imwrite('../result/Lena2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])
