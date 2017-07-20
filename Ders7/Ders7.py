# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

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
	pass
	

if __name__ == '__main__':
	print "Ders 7 Geometric Transformations "
	#resize_demo()
	#rotation_demo()
	affine_transform_demo()
	perspective_transform_demo()

