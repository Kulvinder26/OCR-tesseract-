Optical Character Recognition to identify different texts from Driving license


******************************************************************************
The code is written in python.
In order to run the code you'll need following dependencies(python libraries) :

>> Opencv3
>> pytesseract
>> numpy
>> argparse


Note : pytesseract is a python wrapper of Tesseract ocr (Opensource ocr software 
provided by Google, for more info check : https://github.com/tesseract-ocr), so
for running pytesseract, tesseract is also needed to be installed on the machine.


*******************************************************************************
After you have fulfiled the above mentioned requirements
You can run the code with the following command:


$ python ocrproject.py --image <"PATH OF IMAGE">/<"NAME OF FILE">.jpg


for help see this: 

luckyme@kulvinder-ubuntu: $ python ocrproject.py --image /home/luckyme/fold/dl3.jpg

"dl3.jpg" is the name of file.
"/home/luckyme/fold/" is the path of image file.
"ocrproject.py" is the name of python program. 

for more help refer to demo.jpg.

********************************************************************************
If code runs successfully, you'll get this result :

Name of card owner : ANURAG BREJA
S/D/W of (Guardian name) : BODH RAJ BREJA
Address : HNO-178 A2/B MIG FLATS PASCHIM VIHAR, DELHI 110063 
Date of Birth : 09/02/1976
Blood Group : U
DL number : DL-0420110149646


*********************************************************************************
To exit press any key.



In case of any issues, contact: kulvindersingh97@gmail.com
