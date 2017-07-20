# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

def drawBlobs(inImg,outImg):
	image, contours, hierarchy = cv2.findContours(inImg,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	for cnt in contours:
		(x,y),radius = cv2.minEnclosingCircle(cnt)
		center = (int(x),int(y))
		radius = int(radius)
		if radius >= 20:
			outImg = cv2.circle(outImg,center,radius,(0,0,255),2)	
	

def FrameDiffDemo():
	wName="Frame Diff  Demo "
	print  wName
	vFileName ="../datas/clip1.avi"

	try:
		vCap= cv2.VideoCapture(vFileName)
	except:
		print "Video File " + vFileName +" Not Opened ..."
		return
		
	i = 0
	fps = vCap.get(cv2.CAP_PROP_FPS)
	pFrame = None
	while(vCap.isOpened()):
		ret, frame = vCap.read()
		
		if ret == False :
			break
		
		i += 1
		
		temp = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		if pFrame is None :
			pFrame = temp

			
		if i%5 :
			continue	
		
		diffImg = cv2.absdiff(temp,pFrame)
		cv2.imshow("Diff Image",diffImg)
		
		_,diffImg = cv2.threshold(diffImg,5,255,cv2.THRESH_BINARY)
		element = cv2.getStructuringElement( cv2.MORPH_RECT , ( 3, 3 ))		
		diffImg = cv2.morphologyEx(diffImg,cv2.MORPH_ERODE,element,iterations=1 )
		diffImg = cv2.morphologyEx( diffImg, cv2.MORPH_CLOSE, element,iterations=5 )

		cv2.imshow("Processed Diff Image",diffImg)
		drawBlobs(diffImg,frame)
		cv2.imshow(wName,frame)	
		
		pFrame = temp
		if cv2.waitKey(int(3000/fps)) >= 0:
			break		
		
	vCap.release()	
	cv2.destroyAllWindows()	
	
def BackgroundSubDemo(methodName):
	wName="BackgroundSub " + methodName +" Demo	
	print  wName	
	
	if methodName == "MOG":
		bsMethod = cv2.createBackgroundSubtractorMOG()
	elif methodName == "MOG2":
		bsMethod = cv2.createBackgroundSubtractorMOG2()
	elif methodName == "KNN":
		bsMethod = cv2.createBackgroundSubtractorKNN()	
	elif methodName == "GMG":
		bsMethod = cv2.createBackgroundSubtractorGMG()	
	else:
		print 'Unknown Background Subtraction Method : ',methodName
		return
		
	vFileName ="../datas/clip1.avi"
	try:
		vCap= cv2.VideoCapture(vFileName)
	except:
		print "Video File " + vFileName +" Not Opened ..."
		return
		
	i = 0
	fps = vCap.get(cv2.CAP_PROP_FPS)		
	while(vCap.isOpened()):
		ret, frame = vCap.read()
		if ret == False :
			break	
		
		forImg = bsMethod.apply(frame)
		cv2.imshow("Foreground Image",forImg)
		
		element = cv2.getStructuringElement( cv2.MORPH_RECT , ( 3, 3 ))		
		forImg = cv2.morphologyEx(forImg,cv2.MORPH_ERODE,element,iterations=1 )
		forImg = cv2.morphologyEx(forImg, cv2.MORPH_CLOSE, element,iterations=5 )

		cv2.imshow("Processed Foreground Image",forImg)
		drawBlobs(forImg,frame)
		cv2.imshow(wName,frame)		

		if cv2.waitKey(int(1000/fps)) >= 0:
			break		
		
	vCap.release()	
	cv2.destroyAllWindows()			

if __name__ == '__main__':
	print u"Ders 8 Arka plan silme "
	methodNames = ["MOG2","KNN","MOG", "GMG"]
	FrameDiffDemo()
	for methodName in methodNames:
		try:
			BackgroundSubDemo(methodName)
		except:
			print 'Rebuild OpenCv with opencv_contrib'
