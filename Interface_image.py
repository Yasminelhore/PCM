# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QTextEdit
from PyQt5.QtGui import QPixmap
import math
import numpy as np
import matplotlib.pyplot as plt
import sklearn.neural_network as nrl_net 
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets


def DB_img(path,extension,a):
    lst = np.array([])
    for i in range(1,a):
        full_path = path+str(i)+extension
        lst = np.append(lst,full_path)  
    return lst

def img_reading(path,extension,a):
    db_img = DB_img(path,extension,a)
    lst_img = np.array([])
    for i in range(db_img.size):
        image_flatten = transformation(db_img[i])
        lst_img = np.append(lst_img,image_flatten)    
    return lst_img

def transformation(path_image):
    image = cv2.imread(path_image)
    image_gray =  cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, image_bin = cv2.threshold(image_gray, 100, 255, cv2.THRESH_BINARY) 
    image_flatten = image_bin.flatten()
    return image_flatten

def apprentissage():
    D = np.array([])
    D = np.append(D,[(1,1,1,1,1,2,2,2,3,3,4,4,5,5,5,6,6,7,7,8,8,9,9,9,9,9,10,10,11,11,12,12,13,13,14,14,15,15,15,16,16,17,17,18,18,19,19,20,20,21,21,21,22,22,23,23
    ,24,24,25,25,26,26)])
    D = np.reshape(D,(62,1))

    path = "C:/Users/yas_f/Downloads/TAD/TP_3/images/apprentissage/"
    extension = ".png"
    a = 63
    lst = img_reading(path,extension,a)
    lst = np.reshape(lst,(a-1,2500))
    cl = nrl_net.MLPClassifier(hidden_layer_sizes=(100, 50),activation='identity',max_iter=1000,alpha= 0.05,learning_rate='invscaling',solver='adam',shuffle= True
    ,n_iter_no_change=30,max_fun=15000)
    cl.fit(lst,D)
    E = cl.loss_
    E_Graph = cl.loss_curve_
    
    path = "C:/Users/yas_f/Downloads/TAD/TP_3/images/TEST/"
    extension = ".png"
    a = 42

    D = np.array([])
    D = np.append(D,[(1,1,2,2,3,3,4,4,5,5,6,6,7,8,8,9,9,10,10,11,12,13,13,14,14,15,15,16,16,17,18,19,19,20,21,21,22,23,24,25,26)])
    D = np.reshape(D,(41,1))

    lst = img_reading(path,extension,a)
    lst = np.reshape(lst,(a-1,2500))
    score = cl.score(lst,D)
    return E,E_Graph,cl,score  

Apprentissage_op = apprentissage()   

           

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 160, 111, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.fct_getimage)

        self.test = QtWidgets.QPushButton(self.centralwidget)
        self.test.setGeometry(QtCore.QRect(480, 160, 111, 28))
        self.test.setObjectName("test")
        self.test.clicked.connect(self.tmp_fct)

        self.lettre = QtWidgets.QLabel(self.centralwidget)
        self.lettre.setGeometry(QtCore.QRect(314, 470, 271, 61))
        self.lettre.setText("")
        self.lettre.setObjectName("lettre")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 210, 320, 250))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(200, 40, 351, 81))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "CHOISISEZ IMAGE"))
        self.test.setText(_translate("MainWindow", "erreur"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Le Classifieur Neurenal PMC</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p></body></html>"))

    def fct_getimage(self):
        filename = QFileDialog.getOpenFileName()
        Ui_MainWindow.path = filename[0]
        self.label_3.setPixmap(QtGui.QPixmap(Ui_MainWindow.path).scaled(300, 300, QtCore.Qt.KeepAspectRatio))
        test_sample = transformation(filename[0])
        v_test = Apprentissage_op[2].predict(test_sample.reshape(1, -1))
        lettre = chr(ord('@')+int(v_test))
        self.lettre.setText("le caractère que vous aves choisi est : "+lettre)
        #le pourcentage de chaque lettre dans l'image
        predict = Apprentissage_op[2].predict_proba(test_sample.reshape(1, -1))
        l , c = predict.shape
        for i in range(l):
            for j in range(c):
                print("lettre :",chr(ord('`')+j+1)," pourcentage : ",predict[i][j]*100,"%")

            
    def tmp_fct(self):
        #calcul du taux d'apprentissage 
        print("la valeur de taux d'apprentissage est :  " +str((Apprentissage_op[3]*100))+"%")
         #calcul de l'erreur global
        print("erreur globale est :"+str((Apprentissage_op[0]*100))+" %")
        plt.plot( Apprentissage_op[1])
        plt.ylabel("Erreur Quadratique moyenne")
        plt.xlabel("nombre d iterations")
        plt.title("La courbe EQM en fonction du NI")
        plt.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    


   