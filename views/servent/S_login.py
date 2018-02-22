# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'M_login.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QMessageBox
from controller.servent.S_LoginController import S_LoginController


#这玩意一定要改
class Ui_S_Login(QWidget):
    #告知主窗口登录完成的信号
    _haslogged = pyqtSignal(int,str,str,int)

    def setupUi(self,parent):
        #继承在主窗口上
        self.parent = parent

        #子界面上的作画区
        self.Form = QWidget(parent) #生成在父界面上
        self.Form.setGeometry(QtCore.QRect(0, 70, 1200,590))
        self.Form.setObjectName("Form")
        self.Form.resize(1200,590)
        jpeg = QtGui.QPixmap()
        jpeg.load("pictures/servent/LoginBg.jpg")
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.Form.backgroundRole(), QtGui.QBrush(jpeg))
        self.Form.setPalette(palette1)
        self.Form.setAutoFillBackground(True)

        #标题栏
        # self.label = QtWidgets.QLabel(self.Form)
        # self.label.setGeometry(QtCore.QRect(60, 18, 301, 41))
        # self.label.setStyleSheet("border-bottom:1px groove  rgb(255, 85, 0);background-color: rgb(255, 255, 255,160);")
        # self.label.setObjectName("label")
        # 输入框-房间号
        self.widget_room = QtWidgets.QWidget(self.Form)
        self.widget_room.setGeometry(QtCore.QRect(430, 160, 370, 50))
        self.widget_room.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.widget_room.setObjectName("widget_room")
        # lable_房间号
        # self.label_room = QtWidgets.QLabel(self.widget_room)
        # self.label_room.setGeometry(QtCore.QRect(0, 0, 80, 50))
        # self.label_room.setStyleSheet("border-right:1px groove  rgb(255, 85, 0);")
        # self.label_room.setAlignment(QtCore.Qt.AlignCenter)
        # self.label_room.setObjectName("label_room")
        # input_房间号
        self.lineEdit_room = QtWidgets.QLineEdit(self.widget_room)
        self.lineEdit_room.setGeometry(QtCore.QRect(0,0,370,50))
        self.lineEdit_room.setStyleSheet("border-color: rgba(0, 0, 0, 0);font: 11pt 'Adobe Hebrew';")
        self.lineEdit_room.setStyleSheet("QLineEdit{color:rgb(255,255,255);font: 75 12pt \"微软雅黑\";}")
        self.lineEdit_room.setObjectName("lineEdit_room")

        #输入框-登录名
        self.widget = QtWidgets.QWidget(self.Form)
        self.widget.setGeometry(QtCore.QRect(430, 260, 370, 50))
        self.widget.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.widget.setObjectName("widget")
        #lable_登录名
        # self.label_id = QtWidgets.QLabel(self.widget)
        # self.label_id.setGeometry(QtCore.QRect(0, 0, 80, 50))
        # self.label_id.setStyleSheet("border-right:1px groove  rgb(255, 85, 0);")
        # self.label_id.setAlignment(QtCore.Qt.AlignCenter)
        # self.label_id.setObjectName("label_id")
        #input_登录名
        self.lineEdit_id = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_id.setGeometry(QtCore.QRect(0,0,370,50))
        self.lineEdit_id.setStyleSheet("border-color: rgba(0, 0, 0, 0);font: 11pt 'Adobe Hebrew';")
        self.lineEdit_id.setStyleSheet("QLineEdit{color:rgb(255,255,255);font: 75 12pt \"微软雅黑\";}")
        self.lineEdit_id.setObjectName("lineEdit")


        # 输入框-身份证号
        self.widget_2 = QtWidgets.QWidget(self.Form)
        self.widget_2.setGeometry(QtCore.QRect(430, 360, 370, 50))
        self.widget_2.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.widget_2.setObjectName("widget_2")
        # lable_身份证号
        # self.label_card = QtWidgets.QLabel(self.widget_2)
        # self.label_card.setGeometry(QtCore.QRect(0, 0, 80, 50))
        # self.label_card.setStyleSheet("border-right:1px groove  rgb(255, 85, 0);")
        # self.label_card.setAlignment(QtCore.Qt.AlignCenter)
        # self.label_card.setObjectName("label_card")
        # input_身份证号
        self.lineEdit_card = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_card.setGeometry(QtCore.QRect(0,0,370,50))
        self.lineEdit_card.setStyleSheet("border-color: rgba(0, 0, 0, 0);font: 11pt 'Adobe Hebrew';")
        self.lineEdit_card.setStyleSheet("QLineEdit{color:rgb(255,255,255);font: 75 12pt \"微软雅黑\";}")
        self.lineEdit_card.setObjectName("lineEdit_2")

        #登录按钮

        self.pushButton = QtWidgets.QPushButton(self.Form)
        self.pushButton.setGeometry(QtCore.QRect(325, 470, 550, 50))
        # self.pushButton.setStyleSheet("border-radius:10px;background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet(
            "QPushButton{border-style:outset;border-radius: 10px;border-color: beige;font: bold 14px;}"
            "QPushButton{background-image: url(pictures/servent/LoginButton.png);}"
            "QPushButton:hover{background-image: url(pictures/servent/LoginButton.png);}"
            "QPushButton:pressed{background-image: url(pictures/servent/LoginButton.png);}")
        self.pushButton.clicked.connect(self.checkInp)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.Form)
        self.logincontroller = S_LoginController()
        self.logincontroller._haslogged.connect(self.loginRes)
        self.logincontroller._inputFailed.connect(self.showMessageBox)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Form.setWindowTitle(_translate("Form", "Form"))
        # self.label_room.setText(_translate("Form", "房间号"))
        # self.label_id.setText(_translate("Form", "用户名"))
        # self.pushButton.setText(_translate("Form", "登录"))
        # self.label.setText(_translate("Form", "从机用户登录"))
        # self.label_card.setText(_translate("Form", "身份证号"))

    def hide(self):
        self.Form.hide()

    def show(self):
        self.Form.show()
        self.Form.raise_()

    #交互请求：登录
    def checkInp(self):
        #取输入的用户名与身份证号
        roomNo = self.lineEdit_room.text()
        userName = self.lineEdit_id.text()
        id_card = self.lineEdit_card.text()

        #调用控制器的登录认证函数
        self.logincontroller.Login(roomNo,userName,id_card)

    def showMessageBox(self,res,Msg):
        #根据认证结果弹窗，执行下一步
        Message = QMessageBox()#一个消息框
        #消息框的类型（内置了五种好像）（本体，标题，正文，按键组）
        if res == True:
            QMessageBox.information(Message,"Message", Msg,QMessageBox.Ok)
        else:
            QMessageBox.information(Message, "Message", Msg, QMessageBox.Ok)

    def loginRes(self,roomNo,res,Name,Password,Mode):
        #根据认证结果弹窗，执行下一步
        if res == 1:
            self.showMessageBox(True,"登录成功！")
            self.hide()
            self._haslogged.emit(roomNo,Name,Password,Mode)
        else:
            self.showMessageBox(False, "登录失败，请检查输入,或确定房间是否已被登录")



