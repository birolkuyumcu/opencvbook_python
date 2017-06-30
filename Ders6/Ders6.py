import cv2
import numpy as np
import matplotlib.pyplot as plt

def area_demo():
    lst = []
    lst.append([0,0])
    lst.append([10,0])
    lst.append([10,10])
    lst.append([5,4])
    cnt = np.array(lst)
    area = cv2.contourArea(cnt)
    print "Contour : ",lst
    print "Contour Area : ", area
    return

def seed_count():
    wName = "Plam Seed "
    print wName + " Count "
    oImg = cv2.imread("../datas/palmseeds3.jpg",cv2.IMREAD_GRAYSCALE)
    cv2.namedWindow(wName)
    cv2.imshow(wName,oImg)
    print " Shapes Gray Scale "
    cv2.waitKey(0)
    ret,tImg = cv2.threshold(oImg,200,255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
    cv2.imshow(wName,tImg)
    print " Shapes from Canny "
    cv2.waitKey(0)
    image, contours, hierarchy = cv2.findContours(tImg,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    out_image = np.zeros((oImg.shape[0],oImg.shape[1],3),np.uint8)
    print " Number of contours : ",len(contours)
    cv2.waitKey(0)
    i = 1
    for cnt in contours:
        out_image = cv2.drawContours(out_image, [cnt], 0, (255,0,0), -1)
        (x,y),radius = cv2.minEnclosingCircle(cnt)
        center = (int(x),int(y))
        radius = int(radius)
        #out_image = cv2.circle(out_image,center,radius,(0,255,0),2)
        cv2.putText(out_image,str(i),center,cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),1)
        i += 1
        cv2.imshow(wName,out_image)

        cv2.waitKey(0)

    cv2.destroyWindow(wName)
    return

def contour_demo():
    wName = "Contour ";
    print wName + " Shapes "
    oImg = cv2.imread("../datas/CShapes.png")
    cv2.namedWindow(wName);
    cv2.imshow(wName,oImg);
    cv2.waitKey(0)
    print " Shapes Gray Scale "
    tImg = cv2.cvtColor(oImg, cv2.COLOR_BGR2GRAY)
    cv2.imshow(wName,tImg);
    cv2.waitKey(0)
    print " Shapes from Canny "
    tImg = cv2.Canny(oImg,120,190,5)
    cv2.imshow(wName,tImg);
    cv2.waitKey(0)
    image, contours, hierarchy = cv2.findContours(tImg,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cv2.imshow(wName,image);
    cv2.waitKey(0)

    #loop
    i = 0
    j = 0
    key = 0
    hierarchy = hierarchy[0]
    while True:
        out_image = oImg.copy()
        out_image = cv2.drawContours(out_image, [contours[i]], 0, (100,155,5), -1)
        print_contour_info(contours[i],out_image,i,hierarchy[i])
        cv2.imshow(wName,out_image)
        key = cv2.waitKey(0)
        if key == 27 :
            break
        if key == 2490368 : # Up
            j = 3
        elif key == 2621440 : # Down
            j = 2
        elif key == 2424832 : # Left
            j = 1
        elif key == 2555904 : # Right
            j = 0
        else :
            j = -1

        if j == -1 :
            continue

        if hierarchy[i][j] != -1 :
            i = hierarchy[i][j]
        print i,' ', hierarchy[i]

    cv2.destroyWindow(wName)

def print_contour_info(cnt,out_image,i,hcnt):

    area = cv2.contourArea(cnt)

    (x,y),radius = cv2.minEnclosingCircle(cnt)
    center = (int(x),int(y))
    radius = int(radius)
    out_image = cv2.circle(out_image,center,radius,(0,255,0),2)

    # Bounding Rect
    x,y,w,h = cv2.boundingRect(cnt)
    bRect = [x,y,w,h]
    out_image = cv2.rectangle(out_image,(x,y),(x+w,y+h),(0,255,255),2)
    # Rotated Rect
    rRect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rRect)
    box = np.int0(box)
    out_image = cv2.drawContours(out_image,[box],0,(0,0,255),2)
    #Moments and Center of mass
    M = cv2.moments(cnt)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    #Hu moments
    huM = cv2.HuMoments(M)

    print 'Contour : ', i
    print 'Area : ', area
    print 'Hierarchy : ',hcnt
    print " Minimum Enclosing Circle - Center : ", center , " Radius : " , radius
    print " Bounding Rect : ", bRect
    size = (int(rRect[1][0]),int(rRect[1][1]))
    print " Rotated Rect - Size :",size, " Angle : ",rRect[2]
    print " Center of Mass : ",(cx,cy)
    print " isConvex : ",cv2.isContourConvex(cnt)
    print " Contour Perimeter : ",cv2.arcLength(cnt,True)
    print " Moments \n "
    for k in M.keys():
        print "  ",k,' : ',M[k]

    print " Hu Moments  : ",huM

    return

def showHist(img):
    hsv_Img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv_Img)
    hist_h = cv2.calcHist( [h], [0], None, [180], [0, 180] )
    hist_s = cv2.calcHist( [s], [0], None, [255], [0, 255] )
    hist_v = cv2.calcHist( [v], [0], None, [255], [0, 255] )
    plt.subplot(3,1,1)
    plt.title('Hue Histogram')
    x_pos = list(range(len(hist_h)))
    plt.bar(x_pos,hist_h)
    plt.subplot(3,1,2)
    plt.title('Saturation Histogram')
    x_pos = list(range(len(hist_s)))
    plt.xlim(0,255)
    plt.bar(x_pos,hist_s)
    plt.subplot(3,1,3)
    plt.title('Value Histogram')
    x_pos = list(range(len(hist_v)))
    plt.xlim(0,255)
    plt.bar(x_pos,hist_v)
    plt.show()

def histogram_demo():
    wName = "Histogram Demo "
    print wName
    oImg=cv2.imread("../datas/manzara2.jpg")
    cv2.namedWindow(wName)
    cv2.imshow(wName,oImg)
    cv2.waitKey(0)
    showHist(oImg)
    cv2.waitKey(0)
    hsv_Img = cv2.cvtColor(oImg, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv_Img)
    s = cv2.equalizeHist(s)
    hsv_Img = cv2.merge((h,s,v))
    oImg = cv2.cvtColor(hsv_Img, cv2.COLOR_HSV2BGR)
    cv2.imshow(wName,oImg)
    showHist(oImg)
    cv2.waitKey(0)
    cv2.destroyWindow(wName)
    return

def line_detection_demo():
    wName = "Line Detection Demo ";
    print wName
    oImg=cv2.imread("../datas/optik.jpg")
    cv2.namedWindow(wName)
    cv2.imshow(wName,oImg)
    cv2.waitKey(0)
    tImg = cv2.cvtColor(oImg, cv2.COLOR_BGR2GRAY)
    ret,tImg = cv2.threshold(tImg,50,255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
    cv2.imshow(wName,tImg)
    cv2.waitKey(0)
    minLineLength = 200
    maxLineGap = 10
    lines = cv2.HoughLinesP(tImg,1,np.pi/180,200,minLineLength,maxLineGap)
    lines = lines[:,0,:]
    i = 0
    print lines.shape[0]," Lines detected "
    for l in lines:
        cv2.line(oImg,(l[0],l[1]),(l[2],l[3]),(0,0,255),2)
        print i+1,") Starting Point : ",(l[0],l[1])," - Ending Point : ",(l[2],l[3])
        i +=1
    cv2.imshow(wName,oImg)
    cv2.waitKey(0)
    cv2.destroyWindow(wName)

def circle_detection_demo():
    wName = "Circle Detection Demo ";
    print wName
    oImg = cv2.imread("../datas/Currency.png")
    cv2.namedWindow(wName)
    cv2.imshow(wName,oImg)
    cv2.waitKey(0)
    tImg = cv2.cvtColor(oImg, cv2.COLOR_BGR2GRAY)
    tImg = cv2.GaussianBlur( tImg,(9, 9 ), 1, 1 )
    cv2.imshow(wName,tImg)
    cv2.waitKey(0)
    tImg = cv2.Canny(tImg,10,200)
    cv2.imshow(wName,tImg)
    cv2.waitKey(0)
    circles = cv2.HoughCircles(tImg,cv2.HOUGH_GRADIENT,1,tImg.shape[0]/4)
    circles = circles[0,:,:]
    circles = np.uint16(np.around(circles))

    currecyValuesStr = ["5 Krs" ,"25 Krs","1 TL" ]

    print circles.shape[0]," Currecy detected "
    i = 0
    for c in circles:
        cv2.circle(oImg,(c[0],c[1]),c[2],(0,0,255),2)
        if c[2] > 89 :
            v = currecyValuesStr[2]
        elif c[2] >67:
            v = currecyValuesStr[1]
        else:
            v = currecyValuesStr[0]
        cv2.putText(oImg,v,(c[0],c[1]),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),1)
        print i+1," ) Currency ; Center : ",(c[0],c[1]), " -  Radius : ", c[2], " Value : ",v
        i +=1
    cv2.imshow(wName,oImg)
    cv2.waitKey(0)
    cv2.destroyWindow(wName)


def main():
    print "Ders 6 Information Extraction "
    seed_count()
    area_demo()
    contour_demo()
    histogram_demo()
    line_detection_demo()
    circle_detection_demo()


main()
