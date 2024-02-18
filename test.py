import cv2 
import pytesseract 


img = cv2.imread('uploads/sample.jpg') 

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

text = pytesseract.image_to_string(gray) 

print(text) 
