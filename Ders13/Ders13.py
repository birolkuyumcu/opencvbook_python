# -*- coding: utf-8 -*-

import cv2
import numpy as np

classNames = { 0: 'background',
				1: 'aeroplane', 2: 'bicycle', 3: 'bird', 4: 'boat',
				5: 'bottle', 6: 'bus', 7: 'car', 8: 'cat', 9: 'chair',
				10: 'cow', 11: 'diningtable', 12: 'dog', 13: 'horse',
				14: 'motorbike', 15: 'person', 16: 'pottedplant',
				17: 'sheep', 18: 'sofa', 19: 'train', 20: 'tvmonitor' }
		
Colors = np.random.uniform(0, 255, size=(len(classNames), 3))

# Ağ yapısını tutan prototxt dosyası
model_proto = "../datas/dnn/MobileNetSSD_deploy.prototxt"
# Eğitilmiş Ağ ağırlıklarını içeren caffemodel uzantılı dosya
model_weight = "../datas/dnn/MobileNetSSD_deploy.caffemodel"
net = cv2.dnn.readNetFromCaffe(model_proto, model_weight)

def dnn_detect(image,thresh = 0.5 ):
	inWidth = 300
	inHeight = 300
	inScaleFactor = 0.007843
	meanVal = 127.5
	swapRB = False
	
	rows, cols = image.shape[:2]
	frame = cv2.resize(image,(inWidth, inHeight))

	# Creates 4-dimensional blob from image. 
	# subtract mean values, scales values by scalefactor, 
	# swap Blue and Red channels.
	# blobFromImage ( image,scalefactor,size,mean,swapRB,crop ) 
	blob = cv2.dnn.blobFromImage(frame, inScaleFactor, 
								(inWidth, inHeight), 
								(meanVal, meanVal, meanVal), swapRB)

	net.setInput(blob)
	detections = net.forward()	
	
	# loop over the detections	
	for i in range(detections.shape[2]):
		confidence = detections[0, 0, i, 2]
		if confidence > thresh:
			class_id = int(detections[0, 0, i, 1])
			xLeftBottom = int(detections[0, 0, i, 3] * cols)
			yLeftBottom = int(detections[0, 0, i, 4] * rows)
			xRightTop   = int(detections[0, 0, i, 5] * cols)
			yRightTop   = int(detections[0, 0, i, 6] * rows)

			cv2.rectangle(image, (xLeftBottom, yLeftBottom), (xRightTop, yRightTop),
							Colors[class_id], 2)
							
			if class_id in classNames:
				label = classNames[class_id] + ": " + "%0.1f"%confidence
				labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
				yLeftBottom = max(yLeftBottom, labelSize[1])
				cv2.rectangle(image, (xLeftBottom, yLeftBottom - labelSize[1]),
									 (xLeftBottom + labelSize[0], yLeftBottom + baseLine),
									 (255, 255, 255), cv2.FILLED)
				cv2.putText(image, label, (xLeftBottom, yLeftBottom),
					cv2.FONT_HERSHEY_SIMPLEX, 0.5, Colors[class_id], 2)	

				
	return image
				

def image_mode():
	print "Image Mode "
	try:
		im = cv2.imread("../datas/hababam5.jpg")
	except:
		print "Image Not Opened ..."
		return

	cv2.namedWindow('Image')
	cv2.imshow('Image',im)
	print "Image Loaded press any key ..."
	cv2.waitKey(0)
	im = dnn_detect(im)
	cv2.imshow('Detections',im)
	print "Detections Showed press any key ..."
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def webcam_mode():
    print  "DNN WebCam Mode "
    wName="DNN WebCam Mode"

    try:
        vCap= cv2.VideoCapture(0)
    except:
        print "Web Cam Not Opened ..."
        return

    fps = vCap.get(cv2.CAP_PROP_FPS)

    if fps > 0 :
        print 'fps correctly readed'
    else:
        print 'fps not readed correctly so fixed it '
        fps = 23.0

    print "WebCam capture fps : ",int(fps)
    while(vCap.isOpened()):
		ret, frame = vCap.read()
		if ret == False :
			break
		frame = dnn_detect(frame)
		cv2.imshow(wName,frame)
		key = cv2.waitKey(int(1000/fps))
		if key == 27:# ESC key
			break

    vCap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
	print u"Ders 13 Derin Yapay Sinir Ağları ( DNN ) Modülü ..."
	image_mode()
	webcam_mode()
