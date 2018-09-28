#Importing all the libraries needed
import cv2
import pytesseract
import numpy as np
import argparse


#Extracting file path from arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="input image")
args = vars(ap.parse_args())

#Reading image
image = cv2.imread(args["image"])


#After reading the file, we will extract infromation about the licence owner from the image.

#Extracting Name
crop1 = image[98:117,175:350]
crop1 = cv2.cvtColor(crop1, cv2.COLOR_BGR2GRAY)
ret, crop1 = cv2.threshold(crop1, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#cv2.imwrite("pro1.jpg",crop1)
#cv2.imshow("Pro",crop1)





#Extracting  Gaurdian name
crop2 = image[114:133,177:350]
crop2 = cv2.cvtColor(crop2, cv2.COLOR_BGR2GRAY)
ret, crop2 = cv2.threshold(crop2, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
crop2 = cv2.resize(crop2,(175,19),interpolation=cv2.INTER_AREA)
#cv2.imshow("Pro2",crop2)





#Extracting Address
crop3 = image[165:202,175:500]
crop3 = cv2.cvtColor(crop3, cv2.COLOR_BGR2GRAY)
ret, crop3 = cv2.threshold(crop3, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#cv2.imwrite("pro3.jpg",crop3)
#cv2.imshow("Pro3",crop3)



#Extracting DOB
crop4 = image[132:152,235:390]
crop4 = cv2.cvtColor(crop4, cv2.COLOR_BGR2GRAY)
ret, crop4 = cv2.threshold(crop4, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#cv2.imwrite("pro4.jpg",crop4)
#cv2.imshow("Pro4",crop4)



#Extracting Blood Group
crop5 = image[132:152,235:455	]
crop5 = cv2.cvtColor(crop5, cv2.COLOR_BGR2GRAY)
crop5 = cv2.resize(crop5, None, fx=2, fy=2)
crop5 = cv2.GaussianBlur(crop5, (5, 5), 0)
#cv2.imwrite("pro5.jpg",crop5)
#cv2.imshow("Pro5",crop5)



#Extracting DL number
crop6 = image[80:99,40:378]
crop6 = cv2.cvtColor(crop6, cv2.COLOR_BGR2GRAY)
ret, crop6 = cv2.threshold(crop6, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
crop6 = cv2.resize(crop6,(175*3,19*3),interpolation=cv2.INTER_AREA)
#cv2.imwrite("pro6.jpg",crop6)
#cv2.imshow("Pro6",crop6)



# Using pytesseract to extract text from all croped images
result1 = pytesseract.image_to_string(crop1)
result2 = pytesseract.image_to_string(crop2)
result3 = pytesseract.image_to_string(crop3)
result4 = pytesseract.image_to_string(crop4)
result5 = pytesseract.image_to_string(crop5)
result6 = pytesseract.image_to_string(crop6)

#Some processing
result6 = result6.split(" ")
result3 = result3.split("\n")
result5 = result5.split(" ")
k = ""
for st in result3:
	k = k+st
	k = k+" "

result3 = k 

#Printing results on screen
print("Name of card owner :",result1)
print("S/D/W of (Guardian name) :",result2)
print("Address :",result3)
print("Date of Birth :",result4)
print("Blood Group :",result5[-1])
print("DL number :",result6[-1])





#Press any key to exit	
cv2.waitKey(0)
