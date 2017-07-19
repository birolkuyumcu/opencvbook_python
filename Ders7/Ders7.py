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
	pass

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

