# -*- coding: utf-8 -*-
from __future__ import print_function
import cv2
import numpy as np

def findTemplate(imgBase,imgTemp,locList,method = cv2.TM_CCOEFF_NORMED):
    grayImg = cv2.cvtColor(imgBase,cv2.COLOR_RGB2GRAY)
    cv2.imshow("Debug",grayImg)
    cv2.waitKey()
    ret,grayImg = cv2.threshold(grayImg,10,255,cv2.THRESH_BINARY)
    cv2.imshow("Debug2",grayImg)
    cv2.waitKey()
    imgResult = cv2.matchTemplate( grayImg, imgTemp, method)
    imgResult = (imgResult- imgResult.min()) / (imgResult.max()-imgResult.min())
    cv2.imshow("Debug",imgResult)
    cv2.waitKey()
    minV,maxV,minLoc, maxLoc = cv2.minMaxLoc(imgResult)
    print("Min - Max ",minV," ",maxV )
    if(method == cv2.TM_SQDIFF or method == cv2.TM_SQDIFF_NORMED):
        ret,imgResult = cv2.threshold(imgResult,0.05,255,cv2.THRESH_BINARY_INV )
    else:
        ret,imgResult = cv2.threshold(imgResult,0.95,255,cv2.THRESH_BINARY)
    cv2.imshow("Debug2",imgResult);
    cv2.waitKey()
    imgResult = np.uint8(imgResult)
    image, contours, hierarchy  = cv2.findContours(imgResult,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    locList = []
    for cnt in contours:
        rRect = cv2.minAreaRect(cnt)
        locList.append((rRect[0][0],rRect[0][1]))
    cv2.destroyAllWindows()
    return locList

def matchTemplateDemo():
	print("Template Matching Demo")
	imgSource=cv2.imread("D:/OpenCv4Programmers/datas/pacman2.jpg")
	imgTemp=cv2.imread("D:/OpenCv4Programmers/datas/template.jpg",cv2.IMREAD_GRAYSCALE)
	locList = findTemplate(imgSource,imgTemp,cv2.TM_CCOEFF_NORMED)
	h = imgTemp.shape[0]
	w = imgTemp.shape[1]
	cv2.imshow("Orginal ",imgSource)
	imgResult = imgSource.copy()
	for pt in locList:
		x = int(pt[0])
		y = int(pt[1])
		imgSource = cv2.rectangle( imgSource,(x,y), ( x+w ,y+h ),(0,255,0),2)
	cv2.imshow("Enemies detected ",imgSource)
	cv2.waitKey()
	cv2.destroyAllWindows()
	
def cascadeDemo():
	dedectorFiles = ["D:/OpenCv4Programmers/datas/haarcascades/haarcascade_mcs_nose.xml",
					   "D:/OpenCv4Programmers/datas/lbpcascades/lbpcascade_frontalface.xml"]
	imgFiles = ["D:/OpenCv4Programmers/datas/hababam4-1.jpg",
				"D:/OpenCv4Programmers/datas/hababam3.jpg"]

	dedector = cv2.CascadeClassifier()
	print("Cascade Detection Demo")
	for j in range(2):
		imgSource = cv2.imread(imgFiles[j])
		print("Detecting with ",dedectorFiles[j])
		dedector.load(dedectorFiles[j])
		grayImg = cv2.cvtColor(imgSource,cv2.COLOR_RGB2GRAY)
		grayImg = cv2.equalizeHist(grayImg)
		objList = dedector.detectMultiScale(grayImg)
		for obj in objList:
			x,y,w,h =  obj
			cv2.rectangle(imgSource,(x,y),(x+w,y+h),(0,0,255))                
		winName="Dedected with "+dedectorFiles[j]
		cv2.imshow(winName,imgSource);
		cv2.waitKey()
		cv2.destroyWindow(winName)


if __name__ == '__main__':
	print( u"Ders 10 " ) 
	matchTemplateDemo()
	cascadeDemo()