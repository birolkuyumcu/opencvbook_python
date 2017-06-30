# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Tue Aug 16 19:02:51 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!
import cv2
import sys
from PySide import QtCore, QtGui
import numpy as np

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1005, 556)
        self.sourcePanel = QtGui.QLabel(Dialog)
        self.sourcePanel.setGeometry(QtCore.QRect(20, 80, 480, 360))
        self.sourcePanel.setFrameShape(QtGui.QFrame.Panel)
        self.sourcePanel.setText("")
        self.sourcePanel.setObjectName("sourcePanel")
        self.filteredPanel = QtGui.QLabel(Dialog)
        self.filteredPanel.setGeometry(QtCore.QRect(510, 80, 480, 360))
        self.filteredPanel.setFrameShape(QtGui.QFrame.Panel)
        self.filteredPanel.setText("")
        self.filteredPanel.setObjectName("filteredPanel")
        self.pushButtonLoad = QtGui.QPushButton(Dialog)
        self.pushButtonLoad.setGeometry(QtCore.QRect(470, 20, 31, 21))
        self.pushButtonLoad.setObjectName("pushButtonLoad")
        self.label_CName_3 = QtGui.QLabel(Dialog)
        self.label_CName_3.setGeometry(QtCore.QRect(20, 50, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_CName_3.setFont(font)
        self.label_CName_3.setObjectName("label_CName_3")
        self.imageName = QtGui.QLineEdit(Dialog)
        self.imageName.setGeometry(QtCore.QRect(20, 20, 441, 20))
        self.imageName.setText("")
        self.imageName.setObjectName("imageName")
        self.label_CName_4 = QtGui.QLabel(Dialog)
        self.label_CName_4.setGeometry(QtCore.QRect(510, 50, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_CName_4.setFont(font)
        self.label_CName_4.setObjectName("label_CName_4")
        self.comboBoxFilterNames = QtGui.QComboBox(Dialog)
        self.comboBoxFilterNames.setGeometry(QtCore.QRect(110, 460, 391, 22))
        self.comboBoxFilterNames.setObjectName("comboBoxFilterNames")
        self.comboBoxFilterNames.addItem("")
        self.comboBoxFilterNames.addItem("")
        self.comboBoxFilterNames.addItem("")
        self.comboBoxFilterNames.addItem("")
        self.comboBoxFilterNames.addItem("")
        self.comboBoxFilterNames.addItem("")
        self.comboBoxFilterNames.addItem("")
        self.comboBoxFilterNames.addItem("")
        self.comboBoxFilterNames.addItem("")
        self.comboBoxFilterNames.addItem("")
        self.comboBoxFilterNames.addItem("")
        self.comboBoxFilterNames.addItem("")
        self.comboBoxFilterNames.addItem("")
        self.comboBoxFilterNames.addItem("")
        self.label_CName_5 = QtGui.QLabel(Dialog)
        self.label_CName_5.setGeometry(QtCore.QRect(30, 460, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_CName_5.setFont(font)
        self.label_CName_5.setObjectName("label_CName_5")
        self.pushButtonApply = QtGui.QPushButton(Dialog)
        self.pushButtonApply.setGeometry(QtCore.QRect(404, 500, 91, 23))
        self.pushButtonApply.setObjectName("pushButtonApply")
        self.pushButtonSendToOrj = QtGui.QPushButton(Dialog)
        self.pushButtonSendToOrj.setGeometry(QtCore.QRect(530, 460, 161, 23))
        self.pushButtonSendToOrj.setObjectName("pushButtonSendToOrj")
        self.pushButtonSave = QtGui.QPushButton(Dialog)
        self.pushButtonSave.setGeometry(QtCore.QRect(710, 460, 101, 21))
        self.pushButtonSave.setObjectName("pushButtonSave")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #Aded Later
        self.fileName = ''
        self.img = None
        self.out_image = None

        #Event Connections
        self.pushButtonLoad.clicked.connect(self.selectFile)
        self.pushButtonApply.clicked.connect(self.on_apply )
        self.pushButtonSendToOrj.clicked.connect(self.on_sendToOrj )
        self.pushButtonSave.clicked.connect(self.on_Save )


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Filtre Demo", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonLoad.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_CName_3.setText(QtGui.QApplication.translate("Dialog", "Orjinal Görüntü", None, QtGui.QApplication.UnicodeUTF8))
        self.label_CName_4.setText(QtGui.QApplication.translate("Dialog", "Filitrelenmiş  Görüntü", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFilterNames.setItemText(0, QtGui.QApplication.translate("Dialog", "filter2D", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFilterNames.setItemText(1, QtGui.QApplication.translate("Dialog", "boxFilter", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFilterNames.setItemText(2, QtGui.QApplication.translate("Dialog", "bilateralFilter", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFilterNames.setItemText(3, QtGui.QApplication.translate("Dialog", "blur", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFilterNames.setItemText(4, QtGui.QApplication.translate("Dialog", "GaussianBlur", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFilterNames.setItemText(5, QtGui.QApplication.translate("Dialog", "medianBlur", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFilterNames.setItemText(6, QtGui.QApplication.translate("Dialog", "sepFilter2D", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFilterNames.setItemText(7, QtGui.QApplication.translate("Dialog", "Laplacian", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFilterNames.setItemText(8, QtGui.QApplication.translate("Dialog", "Sobel", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFilterNames.setItemText(9, QtGui.QApplication.translate("Dialog", "Scharr", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFilterNames.setItemText(10, QtGui.QApplication.translate("Dialog", "Canny", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFilterNames.setItemText(11, QtGui.QApplication.translate("Dialog", "pyrMeanShiftFiltering", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFilterNames.setItemText(12, QtGui.QApplication.translate("Dialog", "threshold", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFilterNames.setItemText(13, QtGui.QApplication.translate("Dialog", "adaptiveThreshold", None, QtGui.QApplication.UnicodeUTF8))
        self.label_CName_5.setText(QtGui.QApplication.translate("Dialog", " Fitreler :", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonApply.setText(QtGui.QApplication.translate("Dialog", "Uygula", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSendToOrj.setText(QtGui.QApplication.translate("Dialog", "Orjinal Görüntüye Aktar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSave.setText(QtGui.QApplication.translate("Dialog", "Kaydet", None, QtGui.QApplication.UnicodeUTF8))

        # Events
    def selectFile(self):
        fileName = QtGui.QFileDialog.getOpenFileName(Dialog, "Open Image", "..", "Image Files (*.png *.jpg *.bmp)")
        self.imageName.setText(fileName[0])
        self.fileName = fileName[0]
        self.load_Img()

    def load_Img(self):
        self.img = cv2.imread(self.fileName)
        self.showImg(self.sourcePanel,self.img)
        return

    def showImg(self,label,img):
        if len(img.shape) == 2:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        height, width, byteValue = img.shape
        byteValue = byteValue * width
        timg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        image = QtGui.QImage(timg.data, width, height,byteValue, QtGui.QImage.Format_RGB888)
        label.setPixmap(QtGui.QPixmap(image).scaled(label.size(),aspectMode=QtCore.Qt.KeepAspectRatio))

    def on_apply(self):
        func = {"filter2D": self.on_filter2d,
                "boxFilter": self.on_boxFilter,
                "bilateralFilter": self.on_bilateralFilter,
                "blur": self.on_blur,
                "GaussianBlur": self.on_GaussianBlur,
                "medianBlur": self.on_medianBlur,
                "sepFilter2D": self.on_sepFilter2D,
                "Laplacian": self.on_Laplacian,
                "Sobel": self.on_Sobel,
                "Scharr": self.on_Scharr,
                "Canny": self.on_Canny,
                "pyrMeanShiftFiltering": self.on_pyrMeanShiftFiltering,
                "threshold": self.on_threshold,
                "adaptiveThreshold": self.on_adaptiveThreshold
                }
        filter_name = self.comboBoxFilterNames.currentText()
        func[filter_name]()
        self.showImg(self.filteredPanel,self.out_image)
        return

    def on_filter2d(self):
        kernel = [[1,1,1],[1,-7,1],[1,1,1]]
        kernel = np.asanyarray(kernel, np.float32)
        self.out_image = cv2.filter2D(self.img,-1,kernel)


    def on_boxFilter(self):
        self.out_image = cv2.boxFilter(self.img,-1,(7,7))

    def on_bilateralFilter(self):
        self.out_image = cv2.bilateralFilter(self.img,-1,50,9)

    def on_blur(self):
        self.out_image = cv2.blur(self.img,(11,3))

    def on_GaussianBlur(self):
        self.out_image = cv2.GaussianBlur(self.img,(19,19),sigmaX=3,sigmaY=3)

    def on_medianBlur(self):
        self.out_image = cv2.medianBlur(self.img,ksize=11)

    def on_sepFilter2D(self):
        kernelx = [-1,-2,6,-2,-1]
        kernelx = np.asanyarray(kernelx, np.float32)
        kernely = [0,0,1,0,0]
        kernely = np.asanyarray(kernely, np.float32)
        self.out_image = cv2.sepFilter2D(self.img,-1,kernelx,kernely)

    def on_Laplacian(self):
        self.out_image = cv2.Laplacian(self.img,-1,3)

    def on_Sobel(self):
        self.out_image = cv2.Sobel(self.img,-1,2,2,5)

    def on_Scharr(self):
        self.out_image = cv2.Scharr(self.img,-1,0,1)

    def on_Canny(self):
        self.out_image = cv2.Canny(self.img,0,255)
        return;

    def on_pyrMeanShiftFiltering(self):
        self.out_image = cv2.pyrMeanShiftFiltering(self.img,10,20)
        return;

    def on_threshold(self):
        if len(self.img.shape) > 2 :
            gimg = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        else:
            gimg = self.img

        ret,self.out_image = cv2.threshold(gimg,180,255,cv2.THRESH_BINARY_INV)

    def on_adaptiveThreshold(self):
        if len(self.img.shape) > 2 :
            gimg = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        else:
            gimg = self.img
        self.out_image = cv2.adaptiveThreshold(gimg,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,5,1)
        return;

    def on_sendToOrj(self):
        if self.out_image != None :
            self.img = self.out_image.copy()
            self.showImg(self.sourcePanel,self.img)

    def on_Save(self):
        fileName = QtGui.QFileDialog.getSaveFileName(Dialog, "Filtrelenmiş Görüntüyü Kaydet", "..", "Image Files (*.png *.jpg *.bmp)")
        if fileName[0] !='' :
            cv2.imwrite(fileName[0],self.out_image)




# Create the Qt Application
app = QtGui.QApplication(sys.argv)
# Create and show the form
form = Ui_Dialog()
Dialog = QtGui.QDialog()
form.setupUi(Dialog)
Dialog.show()
# Run the main Qt loop
sys.exit(app.exec_())
