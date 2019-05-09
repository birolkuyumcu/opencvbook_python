# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

def set_detector_by_name(name):
	det = None
	if name == "Agast" :
		det = cv2.AgastFeatureDetector_create()
	elif name == "FAST" :
		det = cv2.FastFeatureDetector_create()
	elif name == "GFTT" :
		det = cv2.GFTTDetector_create(310)
	elif name == "HARRIS":
		det = cv2.GFTTDetector_create(310,0.001,10,3,useHarrisDetector=True)
	elif name == "KAZE": 
		det = cv2.KAZE_create(False, False, 0.001, 4, 4)
	elif name == "ORB": 
		det = cv2.ORB_create()
	elif name == "STAR":
		det = cv2.xfeatures2d.StarDetector_create()
	elif name == "SURF": 
		det = cv2.xfeatures2d.SURF_create()
	elif name == "SIFT":
		det = cv2.xfeatures2d.SIFT_create()
	elif name == "AKAZE":
		det = cv2.AKAZE_create()
	else:
		print "Not Implemented Error ..."
	return det
	
def set_descriptor(name):
	desc = None
	if name == "SIFT" :
		desc = cv2.xfeatures2d.SIFT_create()
	elif name == "SURF" :
		desc = cv2.xfeatures2d.SURF_create()
	elif name == "ORB" :
		desc = cv2.ORB_create()
	elif name == "BRISK" :
		desc = cv2.BRISK_create()
	elif name == "Brief" :
		desc = cv2.xfeatures2d.BriefDescriptorExtractor_create()
	elif name == "FREAK" :
		desc = cv2.xfeatures2d.FREAK_create()
	elif name == "LATCH" :
		desc = cv2.xfeatures2d.LATCH_create()				
	elif name == "AKAZE" :
		desc = cv2.AKAZE_create()		
	elif name == "KAZE" :
		desc = cv2.KAZE_create()
	elif name == "DAISY" :
		desc = cv2.xfeatures2d.DAISY_create()
	elif name == "LUCID" :
		desc = cv2.xfeatures2d.LUCID_create()

	return desc
	

def Feature2D_Demo():
	wName = "Feature2D Demo  "
	isChanged = True
	
	print wName,"\n + or - for Rotation Ange\n * or / for scale\n! ) for toggle keyPoint drawing mode"
	
	menu = ["A ) Agast",
			"F ) FAST",
			"G ) GFTT",
			"H ) HARRIS",
			"K ) KAZE",
			"O ) ORB",
			"R ) STAR",
			"S ) SURF",
			"T ) SIFT",
			"Z ) AKAZE"]
			
	mkeys = 'AFGHKORSTZ'
	
	featureNames = ["Agast",
					"FAST",
					"GFTT",
					"HARRIS",
					"KAZE",
					"ORB",
					"STAR",
					"SURF",
					"SIFT",
					"AKAZE"]
			
	for item in menu:
		print(item) 
	
	
	oImg = cv2.imread("../datas/cami.jpg")
	cv2.imshow(wName,oImg)
	detector = cv2.FastFeatureDetector_create()
	flag = cv2.DRAW_MATCHES_FLAGS_DEFAULT

	rAngle = 0
	scale = 1
	while True:	
		if isChanged :
			isChanged = False
			rotationMat = cv2.getRotationMatrix2D((oImg.shape[1]/2,oImg.shape[0]/2),rAngle,scale)
			outImg  = cv2.warpAffine(oImg,rotationMat,(oImg.shape[1],oImg.shape[0]))
			print "Rotation Angle of image : ",rAngle," -- Scale Factor : ",scale
			ogray = cv2.cvtColor(outImg,cv2.COLOR_BGR2GRAY)
			keysOut = detector.detect(ogray,None)
			cv2.drawKeypoints(outImg, keysOut[:120],outImg, flags=flag)
			cv2.imshow(wName,outImg)			
			
		else:	
			isChanged = True
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
			elif key == ord('!'):
				if flag == cv2.DRAW_MATCHES_FLAGS_DEFAULT:
					flag = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
				else: 
					flag = cv2.DRAW_MATCHES_FLAGS_DEFAULT
				print " Keypoint Drawing method changed "			
			elif chr(key).upper() in mkeys:
				ix = mkeys.index(chr(key).upper())
				print " Actieve Feature Detector : ",featureNames[ix]
				detector = set_detector_by_name(featureNames[ix])
				pass			
			else:
				isChanged = False
				continue
			

		
	cv2.destroyWindow(wName)
	
def DescriptionDemo():
	featureNames = ["Agast",
					"FAST",
					"GFTT",
					"HARRIS",
					#"KAZE",
					"ORB",
					"STAR",
					#"BRISK",
					"AKAZE",
					"SURF", # dont use each other
					"SIFT"	# dont use each other				
					]
					
	descNames = ["SIFT","SURF","ORB","BRISK",
				"Brief","FREAK","LATCH","AKAZE"
				]#"KAZE","DAISY","LUCID"]					
					

	img1 = cv2.imread("../datas/mevlana1.png")
	img2 = cv2.imread("../datas/mevlana2.png")
	gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY);
	gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY);
	matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
	
	FLANN_INDEX_KDTREE = 0
	index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 10)
	search_params = dict(checks=50)   
	flann = cv2.FlannBasedMatcher(index_params,search_params)
	
	wName = "Matches";
	for j,detect_name in enumerate(featureNames):
		print j
		detector = set_detector_by_name(detect_name)
		#print "Before detect"
		keys1 = detector.detect(gray1)
		keys2 = detector.detect(gray2)
		#print "After detect"
		
		for i , desc_name in enumerate(descNames):
			print "Before desc"
			descriptor = set_descriptor(desc_name)
			print "After desc"
			try:
				print "Before compute"
				_,desc1 = descriptor.compute(gray1,keys1)
				_,desc2 = descriptor.compute(gray2,keys2)
				print "After compute"
				try :
					matches = matcher.match(desc1,desc2)
					print 'BForce Mode Actieve'					
				except:	
					matches = flann.match(desc1,desc2)
					print 'Flann Mode Actieve'
					
					
				print "After match"
				matches = sorted(matches, key = lambda x:x.distance)
				print "Before draw Matches"
				img3 = cv2.drawMatches(img1,keys1,img2,keys2,matches[:10],None, flags=2)			
				print "After draw match"
				cv2.imshow(wName,img3)
				print detect_name,' --> ',desc_name
				key = cv2.waitKey(0)
				if key == 27:
					break
			except:
				print "Incompatable ",detect_name,desc_name
		if key == 27:
			break
	cv2.destroyWindow(wName)

#def setFeatureDetector(int i, string& featureName, cv::Ptr<cv::FeatureDetector> &detector);
#def setFeatureDescriptor(int i, string& descriptorName,  cv::Ptr<cv::DescriptorExtractor> &dExt);

def Feature2D_MatchingDemo():
	wName = "Feature2D_MatchingDemo"
	img1 = cv2.imread("../datas/mevlana1.png")
	img2 = cv2.imread("../datas/mevlana2.png")
	gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY);
	gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY);
	
	detector = cv2.xfeatures2d.SURF_create()
	keys1,desc1 = detector.detectAndCompute(gray1,None)
	keys2,desc2 = detector.detectAndCompute(gray2,None)
	
	matchers = []
	
	FLANN_INDEX_KDTREE = 0
	index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 10)
	search_params = dict(checks=50)   
	flann = cv2.FlannBasedMatcher(index_params,search_params)
	
	bf = cv2.BFMatcher()

	matchers.append(flann)
	matchers.append(bf)
	
	for matcher in matchers:	
		matches1to2 = matcher.match(desc1,desc2)	
		matches2to1 = matcher.match(desc2,desc1)		
		#matches = sorted(matches, key = lambda x:x.distance)
		img3 = cv2.drawMatches(img1,keys1,img2,keys2,matches1to2[:100],None, flags=2)
		cv2.imshow(wName,img3)		
		key = cv2.waitKey(0)
		
		good = []
		for i in range(len(matches1to2)):
			m1to2 = matches1to2[i]
			m2to1 = matches2to1[m1to2.trainIdx]
			if m2to1.trainIdx == m1to2.queryIdx and  m1to2.trainIdx == m2to1.queryIdx :
				good.append(m1to2)

		img3 = cv2.drawMatches(img1,keys1,img2,keys2,good[:100],None, flags=2)
		cv2.imshow(wName,img3)		
		key = cv2.waitKey(0)				
		
		if key == 27:
			break	
	
	cv2.destroyWindow(wName)

if __name__ == '__main__':
	print u"Ders 9  2D Öznitelikler ve Eşleştirmeleri "
	Feature2D_Demo()
	DescriptionDemo()
	Feature2D_MatchingDemo()