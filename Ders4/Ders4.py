import cv2
import os
import numpy as np

tImg = [None,None]

def morpholoji_intro_demo():
    wName="Morpholoji Demo "
    morphNames = ["Erosion",
                  "Dilation",
                  "Open",
                  "Close",
                  "Gradient",
                  "Top Hat",
                  "Black Hat"]

    print wName + " Intro "
    zImg=np.zeros((480,640,3),np.uint8)
    cImg=cv2.imread(u'../datas/cicek.jpg')
    nRows,nCols,_ = cImg.shape

    print zImg.shape, cImg.shape
    roi = zImg[180:180+nCols,200:200+nRows]
    zImg[200:200+nRows ,180:180+nCols] = cImg
    roi = cImg
    cv2.namedWindow(wName)
    cv2.createTrackbar('Iteration',wName,0,5,track_bar_func)

    for i in range(7):
        tImg[0] = zImg.copy()
        tImg[1] = i
        cv2.putText(tImg[0],morphNames[i],(40,100),cv2.FONT_HERSHEY_COMPLEX_SMALL | cv2.FONT_ITALIC,4,(255,255,255),3)
        cv2.imshow(wName,tImg[0])
        cv2.waitKey(0)
        cv2.setTrackbarPos('Iteration',wName, 0)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

    return

def morpholoji_shape_demo():
    wName="Morpholoji Demo "
    print wName + " Shape "
    zImg=cv2.imread("../datas/shapes.png",0) # cv2.CV_LOAD_IMAGE_GRAYSCALE
    cv2.namedWindow(wName)

    cv2.imshow(wName,zImg)
    cv2.waitKey(0)
    element = cv2.getStructuringElement( cv2.MORPH_ELLIPSE , ( 9, 9 ))
    dst = cv2.morphologyEx( zImg, cv2.MORPH_ERODE, element,iterations=9)
    dst = cv2.morphologyEx( dst, cv2.MORPH_DILATE, element,iterations=9)
    cv2.imshow("MORPH_ELLIPSE Erode + Dialte", dst);
    cv2.waitKey(0);
    cv2.destroyAllWindows()
    return

def track_bar_func(it):
    opTypes = [cv2.MORPH_ERODE,
           cv2.MORPH_DILATE,
           cv2.MORPH_OPEN,
           cv2.MORPH_CLOSE,
           cv2.MORPH_GRADIENT,
           cv2.MORPH_TOPHAT,
           cv2.MORPH_BLACKHAT]

    wName="Morpholoji Demo "
    print it,opTypes[tImg[1]]
    element = cv2.getStructuringElement( cv2.MORPH_ELLIPSE , ( 3, 3 ))
    dest = cv2.morphologyEx(tImg[0], opTypes[tImg[1]], element,iterations=it)
    cv2.imshow(wName,dest);
    return

def main():
    print "Ders 4"
    morpholoji_shape_demo()
    morpholoji_intro_demo()


main()
