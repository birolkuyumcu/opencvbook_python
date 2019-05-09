# -*- coding: utf-8 -*-
from __future__ import print_function
import cv2
import numpy as np

def PyramidDemo():
	maxLevel=2
	img1 = cv2.imread("D:/OpenCv4Programmers/datas/frm1.png")
	cv2.imshow("Img1",img1)
	cv2.waitKey(10)
	img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
	ret,pyrLevels = cv2.buildOpticalFlowPyramid(img1,(21,21),maxLevel)
	for i in list(range(0,len(pyrLevels),2)):
		level = pyrLevels[i]
		cv2.imshow("Level %d"%(i/2),level)
		print(" Level ",i/2,"  Size ",level.shape)
		cv2.waitKey(0)   
	cv2.destroyAllWindows()

	
def drawFlow(flow,img, step=16):
    h, w = img.shape[:2]
    y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int)
    fx, fy = flow[y,x].T
    lines = np.vstack([x, y, x+fx, y+fy]).T.reshape(-1, 2, 2)
    lines = np.int32(lines + 0.5)
    outImg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.polylines(outImg, lines, 0, (0, 255, 0))
    for (x1, y1), (_x2, _y2) in lines:
        cv2.circle(outImg, (x1, y1), 1, (0, 255, 0), -1)
    return outImg
	
def DenseOpticalFlows():
	print ("Dense Optical Flow Demo ")

	img1 = cv2.imread("D:/OpenCv4Programmers/datas/frm1.png")
	img2 = cv2.imread("D:/OpenCv4Programmers/datas/frm2.png")

	cv2.imshow("Img1",img1)
	cv2.imshow("Img2",img2)
	cv2.waitKey(10)

	img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
	img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

	#  Farneback
	start = cv2.getTickCount()
	flowFarneback = cv2.calcOpticalFlowFarneback(img1,img2,None, 0.25, 3, 15, 5, 5, 1.2, 0)
	timeSec = (cv2.getTickCount() - start) / cv2.getTickFrequency()
	print (" Farnback Optical flow time " , timeSec , " sec" )

	# DualTVL1
	start = cv2.getTickCount()
	tvl1 = cv2.createOptFlow_DualTVL1()
	flowDualTVL1 = tvl1.calc(img1, img2,None)
	timeSec = (cv2.getTickCount() - start) / cv2.getTickFrequency()
	print (" DualTVL1  Optical flow time " , timeSec , " sec" )

	outImgFarneback = drawFlow(flowFarneback,img2)
	outImgDualTVL1 = drawFlow(flowDualTVL1,img2)


	cv2.imshow("Farneback Optical Flow ",outImgFarneback)
	cv2.imshow("DualTVL1 Optical Flow ",outImgDualTVL1)

	cv2.waitKey(0)
	cv2.destroyAllWindows()


def SparseOpticalFlowDemo():
	img1 = cv2.imread("D:/OpenCv4Programmers/datas/frm1.png")
	img2 = cv2.imread("D:/OpenCv4Programmers/datas/frm2.png")
	
	det = cv2.FastFeatureDetector_create()

	cv2.imshow("Img1",img1)
	cv2.imshow("Img2",img2)
	cv2.waitKey(10)

	img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
	img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

	
	kPoints = det.detect(img1)
	fPointsPrev = []
	for kp in kPoints:
		fPointsPrev.append(kp.pt)
	fPointsPrev = np.float32(fPointsPrev).reshape(-1, 2)
	fPointsPrev = cv2.cornerSubPix(img1,fPointsPrev,(5,5),(-1,-1),
								   criteria=(cv2.TermCriteria_MAX_ITER+cv2.TermCriteria_EPS,30,0.1))
	

	fPoints, status, err = cv2.calcOpticalFlowPyrLK(img1, img2, fPointsPrev, None,
											winSize  = (15, 15),maxLevel = 2,
											criteria=(cv2.TermCriteria_MAX_ITER+cv2.TermCriteria_EPS,30,0.1))
	
	outImg =  cv2.cvtColor(img2,cv2.COLOR_GRAY2BGR)
	for i in range(len(fPoints)):
		if status[i] and  err[i]<=10 and (np.abs(fPoints[i][0]-fPointsPrev[i][0])+np.abs(fPoints[i][1]-fPointsPrev[i][1])>=4):
			prev_point = (int(fPointsPrev[i][0]),int(fPointsPrev[i][1]))
			cur_point = (int(fPoints[i][0]),int(fPoints[i][1]))
			cv2.line(outImg,prev_point,cur_point,(255,0,0));
			cv2.circle(outImg,cur_point,1,(0,0,255));
			print ("Delta X : ",fPoints[i][0]-fPointsPrev[i][0]," Delta Y : ",fPoints[i][1]-fPointsPrev[i][1]," Error : ",err[i])										
	
	cv2.imshow("Flow ",outImg)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	
	
def MeanshiftDemo():
	wName="Meanshift Demo";
	print (wName)
	vFileName ="D:/OpenCv4Programmers/datas/clip1.avi";
	vCap = cv2.VideoCapture(vFileName)

	term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

	if vCap.isOpened():
		fps = vCap.get(cv2.CAP_PROP_FPS)
		cv2.namedWindow(wName)
		initialized = False
		
		while(vCap.isOpened()):
			ret, frame = vCap.read()
			if ret == False :
				break
			image = frame.copy()
			hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
			hue=hsv[:,:,0]
			
			if initialized == False:
				track_window = (115,27, 36, 26)
				x,y,w,h = track_window
				roi=hue[y:y+h,x:x+w]            
				roi_hist = cv2.calcHist([roi],[0],None,[16],[0,180])
				cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)   
				initialized = True
				continue

		   
			backproj = cv2.calcBackProject([hue],[0],roi_hist,[0,180],1)
			ret, track_window = cv2.meanShift(backproj, track_window, term_crit)
			#print(ret,track_window)
			
			x,y,w,h = track_window
			roi=hue[y:y+h,x:x+w]            
			roi_hist = cv2.calcHist([roi],[0],None,[16],[0,180])
			cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)   
			
			cv2.rectangle(frame,(x,y), (x+w,y+h),(0,0,255),2)
			print ("Center of Tracking Window (Y Axis ) : ", y+h/2)
			if y<=260 and y+h >=260 :
				lineColor=(255,0,0)
				print("Passing Line....")
			else:
				lineColor=(0,255,255)        
			
			cv2.line(frame,(0,260),(640,260),lineColor,3)        
			cv2.imshow(wName,frame)
			cv2.imshow("BackProject",backproj)
			key = cv2.waitKey(int(1000/fps))    
			if key == 27 :
				break     
			
		cv2.destroyAllWindows()
	else:
		print("Video File ",vFileName," Not Opened ..." )

	
def CamshiftDemo():
	wName="Camshift Demo";
	print (wName)
	vFileName ="D:/OpenCv4Programmers/datas/clip1.avi";
	vCap = cv2.VideoCapture(vFileName)

	term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

	if vCap.isOpened():
		fps = vCap.get(cv2.CAP_PROP_FPS)
		cv2.namedWindow(wName)
		initialized = False
		
		while(vCap.isOpened()):
			ret, frame = vCap.read()
			if ret == False :
				break
			image = frame.copy()
			hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
			mask = cv2.inRange(hsv, ( 0, 30, 10), (180, 150, 80))
			hue=hsv[:,:,0]
			
			if initialized == False:
				track_window = (115,27, 36, 26)
				x,y,w,h = track_window
				roi=hue[y:y+h,x:x+w]  
				mask_roi = mask[y:y+h,x:x+w]
				roi_hist = cv2.calcHist([roi],[0],mask_roi,[16],[0,180])
				cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)   
				initialized = True
				continue

		   
			backproj = cv2.calcBackProject([hue],[0],roi_hist,[0,180],1)
			backproj &= mask
			ret, track_window = cv2.CamShift(backproj, track_window, term_crit)
			#print(ret,track_window)
			
			x,y,w,h = track_window
			roi=hue[y:y+h,x:x+w]
			mask_roi = mask[y:y+h,x:x+w]
			roi_hist = cv2.calcHist([roi],[0],mask_roi,[16],[0,180])
			cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)   
			
			cv2.rectangle(frame,(x,y), (x+w,y+h),(0,0,255),2)
			print ("Center of Tracking Window (Y Axis ) : ", y+h/2)
			if y<=260 and y+h >=260 :
				lineColor=(255,0,0)
				print("Passing Line....")
			else:
				lineColor=(0,255,255)        
			
			cv2.line(frame,(0,260),(640,260),lineColor,3)        
			cv2.imshow(wName,frame)
			cv2.imshow("BackProject",mask)
			key = cv2.waitKey(int(1000/fps))    
			if key == 27 :
				break     
			
		cv2.destroyAllWindows()
	else:
		print("Video File ",vFileName," Not Opened ..." )
	

if __name__ == '__main__':
	print(u"Ders 11 ")
	PyramidDemo()
	DenseOpticalFlows()
	SparseOpticalFlowDemo()
	MeanshiftDemo()
	CamshiftDemo()