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

from controller.main.M_LoginController import M_LoginController


#这玩意一定要改
class Ui_Form(QWidget):
    #告知主窗口登录完成的信号
    _haslogged = pyqtSignal()

    def setupUi(self,MainWindow):
        #继承在主窗口上
        self.parent = MainWindow

        #子界面上的作画区
        self.Form = QWidget(MainWindow)  # 生成在父界面上
        self.Form.setGeometry(QtCore.QRect(0, 70, 1200, 590))
        self.Form.setObjectName("Form")
        self.Form.resize(1200, 590)
        # self.Form.setStyleSheet("background-color: rgba(255, 170, 0, 190);")
        jpeg = QtGui.QPixmap()
        jpeg.load("pictures/LoginBg.png")
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.Form.backgroundRole(), QtGui.QBrush(jpeg))
        self.Form.setPalette(palette1)
        self.Form.setAutoFillBackground(True)

        #标题栏
        # self.label = QtWidgets.QLabel(self.Form)
        # self.label.setGeometry(QtCore.QRect(60, 18, 301, 41))
        # self.label.setStyleSheet("border-bottom:1px groove  rgb(255, 85, 0);background-color: rgb(255, 255, 255,160);")
        # self.label.setObjectName("label")

        #输入框-登录名
        self.widget = QtWidgets.QWidget(self.Form)
        self.widget.setGeometry(QtCore.QRect(430, 180, 370, 50))
        self.widget.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.widget.setObjectName("widget")
        # #lable_账号
        # self.label_id = QtWidgets.QLabel(self.widget)
        # self.label_id.setGeometry(QtCore.QRect(0, 0, 60, 50))
        # self.label_id.setStyleSheet("border-right:1px groove  rgb(255, 85, 0);")
        # self.label_id.setAlignment(QtCore.Qt.AlignCenter)
        # self.label_id.setObjectName("label_id")
        # input_账号
        self.lineEdit_id = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_id.setGeometry(QtCore.QRect(0, 0, 370, 50))
        self.lineEdit_id.setStyleSheet("border-color: rgba(0, 0, 0, 0);font: 11pt 'Adobe Hebrew';")
        self.lineEdit_id.setStyleSheet("QLineEdit{color:rgb(255,255,255);font: 75 12pt \"微软雅黑\";}")
        self.lineEdit_id.setObjectName("lineEdit")


        # 输入框-密码
        self.widget_2 = QtWidgets.QWidget(self.Form)
        self.widget_2.setGeometry(QtCore.QRect(430, 290, 370, 50))
        self.widget_2.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.widget_2.setObjectName("widget_2")
        # lable_密码
        # self.label_pwd = QtWidgets.QLabel(self.widget_2)
        # self.label_pwd.setGeometry(QtCore.QRect(0, 0, 60, 50))
        # self.label_pwd.setStyleSheet("border-right:1px groove  rgb(255, 85, 0);")
        # self.label_pwd.setAlignment(QtCore.Qt.AlignCenter)
        # self.label_pwd.setObjectName("label_pwd")
        # input_密码
        self.lineEdit_pwd = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_pwd.setGeometry(QtCore.QRect(0, 0, 370, 50))
        self.lineEdit_pwd.setStyleSheet("border-color: rgba(255, 255, 255, 0);font: 11pt 'Adobe Hebrew'")
        self.lineEdit_pwd.setStyleSheet("QLineEdit{color:rgb(255,255,255);font: 75 12pt \"微软雅黑\";}")
        self.lineEdit_pwd.setObjectName("lineEdit_2")
        self.lineEdit_pwd.setEchoMode(QtWidgets.QLineEdit.Password)

        #登录按钮
        self.pushButton = QtWidgets.QPushButton(self.Form)
        self.pushButton.setGeometry(QtCore.QRect(325, 460, 550, 50))
        # self.pushButton.setStyleSheet("border-radius:10px;background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet(
            "QPushButton{border-style:outset;border-radius: 10px;border-color: beige;font: bold 14px;}"
            "QPushButton{background-image: url(pictures/LoginButton.png);}"
            "QPushButton:hover{background-image: url(pictures/LoginButton.png);}"
            "QPushButton:pressed{background-image: url(pictures/LoginButton.png);}")
        self.pushButton.clicked.connect(self.checkInp)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.Form)

        self.logincontroller = M_LoginController()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Form.setWindowTitle(_translate("Form", "Form"))
        # self.label_id.setText(_translate("Form", "账号"))
        # self.pushButton.setText(_translate("Form", "登录"))
        # self.label.setText(_translate("Form", "管理员登录"))
        # self.label_pwd.setText(_translate("Form", "密码"))

    def hide(self):
        self.Form.hide()

    def show(self):
        self.Form.show()
        self.Form.raise_()

    #交互请求：登录
    def checkInp(self):
        #取输入的用户名与密码
        userName = self.lineEdit_id.text()
        passwd = self.lineEdit_pwd.text()

        #调用控制器的登录认证函数

        res ,message= self.logincontroller.Login(userName,passwd)

        #根据认证结果弹窗，执行下一步
        Message = QMessageBox()#一个消息框
        #消息框的类型（内置了五种好像）（本体，标题，正文，按键组）
        if res == True:
            QMessageBox.information(Message,"Message", message,QMessageBox.Ok)
            self.hide()
            self._haslogged.emit()
        else:
            QMessageBox.information(Message, "Message", message, QMessageBox.Ok)
            self.lineEdit_pwd.clear()



