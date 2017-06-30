import cv2
import os
import math
import numpy as np

def clear_images():
    fnms = ['../datas/ebru.png','../datas/ebru.jpg']
    for f in fnms:
        if os.path.isfile(f):
            os.remove(f)

def image_read_write():
    print "Image Read Write "
    clear_images()
    try:
        """

        cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
        cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
        cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

        """
        im = cv2.imread("../datas/ebru.bmp")
    except:
        print "Image Not Opened ..."
        return

    cv2.namedWindow('Ebru_Bmp')
    cv2.imshow('Ebru_Bmp',im)
    print "Ebru.bmp Loaded press any key ..."
    cv2.waitKey(0)
    cv2.imwrite('../datas/ebru.png',im)
    prm=[cv2.IMWRITE_JPEG_QUALITY,50]
    cv2.imwrite('../datas/ebru.jpg',im,prm)
    im = cv2.imread("../datas/ebru.png")
    cv2.imshow('Ebru_Png',im)
    print "Ebru_Png Loaded press any key ..."
    im = cv2.imread("../datas/ebru.jpg")
    cv2.imshow('Ebru_Jpg',im)
    print "Ebru_Jpg Loaded press any key ..."
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def video_player():
    print  "Video Player "
    vFileName ="../datas/TomAndJerry.mp4"
    wName="Video Player"

    try:
        vCap= cv2.VideoCapture(vFileName)
    except:
        print "Video File " + vFileName +" Not Opened ..."
        return

    fps = vCap.get(cv2.CAP_PROP_FPS)
    print "Video Running fps : ",int(fps)
    while(vCap.isOpened()):
        ret, frame = vCap.read()
        if ret == False :
            break
        cv2.imshow(wName,frame)
        if cv2.waitKey(int(1000/fps)) >= 0:
            break

    vCap.release()
    cv2.destroyAllWindows()

def webcam_player():
    print  "WebCam Player "
    wName="WebCam Player"

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
        cv2.imshow(wName,frame)
        if cv2.waitKey(int(1000/fps)) >= 0:
            break

    vCap.release()
    cv2.destroyAllWindows()

def ipcam_player(ipUrl):
    print  "IPCam Player "
    wName=ipUrl

    try:
        vCap= cv2.VideoCapture(ipUrl)
    except:
        print "Ip Cam Not Opened ..."
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
        cv2.imshow(wName,frame)
        if cv2.waitKey(int(1000/fps)) >= 0:
            break

    vCap.release()
    cv2.destroyAllWindows()


def main():
    image_read_write()
    webcam_player()
    video_player()	
	
	# if not work find working IPCam adress
    ipcam_player("http://195.67.26.73/mjpg/video.mjpg") 







main()
