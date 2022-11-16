import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img1 = cv2.imread('hello.jpg')
img_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
text = pytesseract.image_to_string(img1)
with open('page1.txt', 'w') as file:
    file.write(text)


