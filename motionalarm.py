#!/usr/bin/python3 

import cv2
import time
import numpy as np
from gtts import gTTS
import os
#loading pictures from camera
#starting camera
cap=cv2.VideoCapture(0)
#taking pic 1
tts=gTTS(text="warning",lang='en')
tts.save("Warning.mp3")
while cap.isOpened():
	tp1=cap.read()[1]
	tp2=cap.read()[1]
	tp3=cap.read()[1]
	gray1=cv2.cvtColor(tp1,cv2.COLOR_BGR2GRAY)	
	gray2=cv2.cvtColor(tp2,cv2.COLOR_BGR2GRAY)
	gray3=cv2.cvtColor(tp3,cv2.COLOR_BGR2GRAY)
	newimage1=cv2.GaussianBlur(gray1, (21, 21), 0)
	newimage2=cv2.GaussianBlur(gray2, (21, 21), 0)
	newimage3=cv2.GaussianBlur(gray3, (21, 21), 0)
	#creating difference between first and second

	#diff1=cv2.subtract(tp1,tp2)	
	#can also be done by numpy array subtraction
	#cv2.imshow('nishant1',tp1)
	#cv2.imshow('nishant2',tp2)
	#cv2.imshow('nishant3',tp3)
	#cv2.imshow('nishant4',tp4)
	#most accurate result by cv2

	f_diff1=cv2.absdiff(newimage1,newimage2)
	f_diff2=cv2.absdiff(newimage2,newimage3)
	f_diff3=cv2.bitwise_and(f_diff1,f_diff2)
	#cv2.imshow('nishant',f_diff3)
	#cv2.imshow('nishant1',tp1)
	thresh=cv2.threshold(f_diff3, 10, 255, cv2.THRESH_BINARY)[1]
	thresh = cv2.dilate(thresh, None, iterations=2)
	cv2.imshow('nishant',thresh)
	#cv2.imshow('nishant1',f_diff1)
	#cv2.imshow('nishant2',f_diff2)
	print(thresh)
	if np.array_equal(thresh,np.zeros((480,640))):
		pass
	else:
		os.system("mpg321 Warning.mp3")
	if cv2.waitKey(1) & 0xff == ord('q'):
		break
	

cv2.destroyAllWindows(0)
cap.release()
