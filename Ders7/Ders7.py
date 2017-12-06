# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

def resize_demo():
	wName = "Resize Demo "
	print wName," : Press  + or - to resize "
	oImg = cv2.imread("../datas/manzara.jpg")
	cv2.imshow(wName,oImg)
	fx=1
	fy=1
	key = 0
	outImg =oImg
	
	while True:		
		key = cv2.waitKey(-1)		
		if key == ord('+'):
			fx=fx*1.1
			fy=fy*1.1
		elif key == ord('-'):
			fx=fx*0.9;
			fy=fy*0.9;
		elif key == 27:
			break		
		else:
			continue
			
		outImg = cv2.resize(oImg,None,fx=fx,fy=fy)
		cv2.imshow(wName,outImg)
		print "New size of image {}".format((outImg.shape[0],outImg.shape[1]))	

	cv2.destroyWindow(wName)

	
def rotation_demo():
	wName = "Rotation Demo  "
	print wName," : Press + or - for Rotation Angel * or / for scale "
	oImg = cv2.imread("../datas/manzara.jpg")
	cv2.imshow(wName,oImg)

	rAngle = 0
	scale = 1
	while True:	
		key = cv2.waitKey(-1)		
		if key == ord('+'):
			rAngle += 10
			if rAngle >= 360 :
				rAngle = rAngle%360

		elif key == ord('-'):
			rAngle -= 10
			if rAngle < 0 :
				rAngle += 360
				
		elif key == ord('*'):
			scale *=1.1

		elif key == ord('/'):
			scale /=1.1			
				
		elif key == 27:
			break		
		else:
			continue
			
		rotationMat = cv2.getRotationMatrix2D((oImg.shape[1]/2,oImg.shape[0]/2),rAngle,scale)
		outImg  = cv2.warpAffine(oImg,rotationMat,(oImg.shape[1],oImg.shape[0]))
		cv2.imshow(wName,outImg)
		print rAngle
		
	cv2.destroyWindow(wName)
			
def affine_transform_demo():
	wName = "Affine Transform Demo "
	print wName," count "
	oImg = cv2.imread("../datas/RLetters.png")
	cv2.imshow(wName,oImg)	
	print "Gray Scale "
	cv2.waitKey(0)
	tImg = cv2.cvtColor(oImg,cv2.COLOR_BGR2GRAY)
	_,tImg = cv2.threshold(tImg,200,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
	cv2.imshow(wName,tImg)
	cv2.waitKey(0)	
	image, contours, hierarchy = cv2.findContours(tImg,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	out_image = np.zeros((oImg.shape[0],oImg.shape[1],3),np.uint8)
	destCorners = np.float32([[0,63],[0,0],[63,0]])
	for cnt in contours:
		out_image = cv2.drawContours(out_image, [cnt], 0, (255,0,0), -1)		
		rRect = cv2.minAreaRect(cnt)		
		box = cv2.boxPoints(rRect)
		box = np.int0(box)
		corners = np.float32(box[:3])
		out_image = cv2.drawContours(out_image,[box],0,(0,0,255),2)			
		warpMat = cv2.getAffineTransform(corners ,destCorners )		
		outLetter  = cv2.warpAffine(oImg,warpMat,(64,64))
		out_image[:64,:64] = outLetter
		cv2.imshow("out Letter",outLetter)
		cv2.imshow(wName,out_image)
		cv2.waitKey(0)
	cv2.destroyAllWindows()


def perspective_transform_demo():  
	wName="Perspective Transform Demo"
	print wName
	vFileName ="../datas/TomAndJerry.mp4"
	vCap= cv2.VideoCapture(vFileName)
	height = vCap.get(cv2.CAP_PROP_FRAME_HEIGHT)
	width = vCap.get(cv2.CAP_PROP_FRAME_WIDTH)
	initialCorners = np.float32([[0,0],[0,height-1],[width-1,height-1],[width-1,0]])
	transformedCorners = np.zeros_like(initialCorners)
	oImg = cv2.imread("../datas/manzara.jpg")

	i = 0
	fps = vCap.get(cv2.CAP_PROP_FPS)
	while(vCap.isOpened()):
		ret, frame = vCap.read()		
		tImg = oImg.copy()
		
		transformedCorners[0] = [100+80*math.sin((i+30)*math.pi/180),100+80*math.cos((i+30)*math.pi/180)]
		transformedCorners[1] = [100+80*math.sin(i*math.pi/180),200+80*math.cos(i*math.pi/180)]
		transformedCorners[2] = [400+80*math.sin((i+20)*math.pi/180),310+80*math.cos((i+20)*math.pi/180)]
		transformedCorners[3] = [400+80*math.sin(i*math.pi/180),100+80*math.cos(i*math.pi/180)]

		tMatris = cv2.getPerspectiveTransform(initialCorners,transformedCorners)

		# warpPerspective(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]]) -> dst
		cv2.warpPerspective(frame,tMatris,(tImg.shape[1],tImg.shape[0]),tImg,flags=cv2.INTER_LINEAR,borderMode=cv2.BORDER_TRANSPARENT)
		
		for j in range(4):
			cv2.circle(tImg,tuple(transformedCorners[j]),5,(0,0,255),3)
			cv2.line(tImg,tuple(transformedCorners[j]),tuple(transformedCorners[(j+1)%4]),(255,0,0),3)
		cv2.imshow(wName,tImg)
		key = cv2.waitKey(int(1000/fps))
		i += 2
		if key == 27 :
			break
			
	cv2.destroyWindow(wName)
	vCap.release()
	

if __name__ == '__main__':
	print "Ders 7 Geometric Transformations "
	resize_demo()
	rotation_demo()
	affine_transform_demo()
	perspective_transform_demo()

