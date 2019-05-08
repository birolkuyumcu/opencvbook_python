# -*- coding: utf-8 -*-
from __future__ import print_function
import cv2
import numpy as np
import math

def mat_demo():
    print("Mat Demo")
    wName = 'Mat Demo'
    cv2.namedWindow(wName)
    im = np.random.randint(0,255,(480,640,3),np.uint8)
    print(im.shape)
    cv2.imshow(wName,im)
    cv2.waitKey(500)
    col,row,ch = im.shape
    redROI = im[60:col-60,60:row-60] 
    redROI[:,:] = (0,0,255)
    cv2.imshow(wName,im)
    cv2.waitKey(500)
    cRedROI = redROI.copy()
    col,row,ch = redROI.shape
    greenROI = redROI[40:col-40,20:row-20]
    greenROI[:,:] = (0,255,0)
    cv2.imshow(wName,im)
    cv2.waitKey(500)
    col,row,ch = greenROI.shape
    blueROI = greenROI[40:col-40,20:row-20]
    blueROI[:,:] = (255,0,0)
    cv2.imshow(wName,im)
    cBlueROI = blueROI.copy()
    cv2.waitKey(500)
    im[:,125:165]=(255,255,0)
    im[195:240,:] = (0,255,255)
    cv2.imshow(wName,im)
    cv2.waitKey(500)
    cv2.waitKey(0)
    cv2.destroyWindow(wName);

    cv2.imshow("redROI",redROI);
    cv2.imshow("Clone of redROI",cRedROI);
    cv2.waitKey(0);
    cv2.destroyAllWindows();

    cv2.imshow("blueROI",blueROI);
    cv2.imshow("Copy of blueROI",cBlueROI);
    cv2.waitKey(0);
    cv2.destroyAllWindows();


def drawing_demo():
    wName="Drawing Demo"
    print(wName)

    bImg=cv2.imread("../datas/ebru.bmp")
    tImg=bImg.copy()
    nRows,nCols,_ = bImg.shape
    print(bImg.shape)
    for i in range(361):

        px1 = int(nCols/2)
        py1 = int(nRows/2)
        px2 = int(nCols/2+(120*math.sin(i*math.pi/180)))
        py2 = int(nRows/2+(120*math.cos(i*math.pi/180)))
        cv2.line(tImg,(px1,py1),(px2,py2),(0,0,255),3)
        cv2.putText(tImg,wName,(10+i,10+i),cv2.FONT_HERSHEY_COMPLEX_SMALL | cv2.FONT_ITALIC,2,(255,0,0),3,16)
        cv2.circle(tImg,(int(nCols -1.3*i),400),15,(0,255,255),-1)
        px1 = int(1.3*i)
        py1 = int(380-0.9*i)
        px2 = px1+40
        py2 = py1+40
        cv2.rectangle(tImg,(px1,py1),(px2,py2),(255,255,0),8)
        cv2.imshow(wName,tImg);
        cv2.waitKey(3);
        tImg = bImg.copy()

    cv2.waitKey(0)
    cv2.destroyWindow(wName)

def pixel_demo():
	wName="Pixel Demo"
	print(wName)

	bImg=cv2.imread("../datas/ebru.bmp");
	tImg=bImg.copy()
	nRows,nCols,_ = bImg.shape

	for x in range(nCols):
		for y in range(nRows):
			blue,green,red = bImg[y,x]
			if blue < 70 and green < 70 and red > 128 :
				bImg[y,x] = (0,0,255)
			else:
				bImg[y,x] = (0,0,0)

	cv2.imshow(wName,tImg);
	cv2.imshow(wName+'Transformed',bImg);
	cv2.waitKey(0);
	cv2.destroyAllWindows()

def main():
    mat_demo()
    drawing_demo()
    pixel_demo()



main()
