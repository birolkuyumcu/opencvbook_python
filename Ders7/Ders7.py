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
	pass

def perspective_transform_demo():
	pass
	

if __name__ == '__main__':
	print "Ders 7 Geometric Transformations "
	resize_demo()
	rotation_demo()
	affine_transform_demo()
	perspective_transform_demo()

