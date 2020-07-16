# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(253, 107)
        Dialog.setMinimumSize(QtCore.QSize(221, 92))
        Dialog.setMaximumSize(QtCore.QSize(500, 500))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 71))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 20, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 41, 151))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("background: #bbb")
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 40, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #555")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 70, 87, 31))
        self.pushButton.setObjectName("pushButton")
        self.widget.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/img/img/main/Misc_Birthday_Cake.png\"/></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "You win!"))
        self.label_3.setText(_translate("Dialog", "Rock VS. paper"))
        self.pushButton.setText(_translate("Dialog", "OK"))
import qtkanobu.result.resources_rc
