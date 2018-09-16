#from PIL import Image
#from pytesseract import image_to_string

#print (image_to_string(Image.open('sample2.jpg')))
#print (image_to_string(Image.open('page.jpg'), lang='eng'))
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd="C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
name = input("Enter the name of image with its extension: ")
im=Image.open(name)
data = (pytesseract.pytesseract.tesseract_cmd.image_to_string(im,lang='eng'))
print(data)
with open('data.txt','w',encoding="utf-8") as file:
		file.write(data)

