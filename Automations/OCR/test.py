from PIL import Image
from pytesseract import *

# 만약 path 정보를 못불러올 경우 다음과 같이 설정한다.
pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
filename = "../../Utils/Images/ocr/test.jpg"
image = Image.open(filename)

text = image_to_string(image, lang='kor')

with open("sample.txt", "w", encoding='utf-8') as f:
    f.write(text)

