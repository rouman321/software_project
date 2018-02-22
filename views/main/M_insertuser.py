# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'M_insertuser.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QMessageBox
from controller.main import M_insertUserController

class Ui_insertusr(object):
    def setupUi(self, MainWindow):
        self.insertusr = QWidget(MainWindow)
        self.insertusr.setObjectName("insertusrWidget")
        self.insertusr.resize(1200, 590)
        self.insertusr.setGeometry(QtCore.QRect(0, 70, 1200, 590))
        jpeg = QtGui.QPixmap()
        jpeg.load("pictures/UserBg.png")
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.insertusr.backgroundRole(), QtGui.QBrush(jpeg))
        self.insertusr.setPalette(palette1)
        self.insertusr.setAutoFillBackground(True)

        # self.label = QtWidgets.QLabel(self.insertusr)
        # self.label.setGeometry(QtCore.QRect(250, 120, 80, 20))
        # self.label.setObjectName("label")
        # self.label_2 = QtWidgets.QLabel(self.insertusr)
        # self.label_2.setGeometry(QtCore.QRect(250, 200, 80, 20))
        # self.label_2.setObjectName("label_2")
        # self.label_3 = QtWidgets.QLabel(self.insertusr)
        # self.label_3.setGeometry(QtCore.QRect(250, 280, 80, 20))
        # self.label_3.setObjectName("label_3")

        self.widget3 = QtWidgets.QWidget(self.insertusr)
        self.widget3.setGeometry(QtCore.QRect(375, 150, 450, 50))
        self.widget3.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.widget3.setObjectName("widget3")
        self.roomNoEdit = QtWidgets.QLineEdit(self.widget3)
        self.roomNoEdit.setGeometry(QtCore.QRect(0, 0, 450, 50))
        self.roomNoEdit.setStyleSheet("border-color: rgba(0, 0, 0, 0);font: 11pt 'Adobe Hebrew';")
        self.roomNoEdit.setStyleSheet("QLineEdit{color:rgb(0,204,255);font: 75 12pt \"微软雅黑\";}")
        self.roomNoEdit.setObjectName("roomNoEdit")

        self.widget = QtWidgets.QWidget(self.insertusr)
        self.widget.setGeometry(QtCore.QRect(375, 225, 450, 50))
        self.widget.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.widget.setObjectName("widget")
        self.nameEdit = QtWidgets.QLineEdit(self.widget)
        self.nameEdit.setGeometry(QtCore.QRect(0, 0, 450, 50))
        self.nameEdit.setStyleSheet("border-color: rgba(0, 0, 0, 0);font: 11pt 'Adobe Hebrew';")
        self.nameEdit.setStyleSheet("QLineEdit{color:rgb(0,204,255);font: 75 12pt \"微软雅黑\";}")
        self.nameEdit.setObjectName("lineEdit")

        self.widget2 = QtWidgets.QWidget(self.insertusr)
        self.widget2.setGeometry(QtCore.QRect(375, 300, 450, 50))
        self.widget2.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.widget2.setObjectName("widget2")
        self.pwdEdit = QtWidgets.QLineEdit(self.widget2)
        self.pwdEdit.setGeometry(QtCore.QRect(0, 0, 450, 50))
        self.pwdEdit.setObjectName("pwdEdit")
        self.pwdEdit.setStyleSheet("border-color: rgba(0, 0, 0, 0);font: 11pt 'Adobe Hebrew';")
        self.pwdEdit.setStyleSheet("QLineEdit{color:rgb(0,204,255);font: 75 12pt \"微软雅黑\";}")

        self.ensureButton = QtWidgets.QPushButton(self.insertusr)
        self.ensureButton.setGeometry(QtCore.QRect(475, 400, 250, 50))
        self.ensureButton.setObjectName("ensureButton")
        self.ensureButton.setStyleSheet(
            "QPushButton{border-style:outset;border-radius: 10px;border-color: beige;font: bold 14px;}"
            "QPushButton{background-image: url(pictures/insertuserButton.png);}"
            "QPushButton:hover{background-image: url(pictures/insertuserButton2.png);}"
            "QPushButton:pressed{background-image: url(pictures/insertuserButton3.png);}")
        self.ensureButton.clicked.connect(self.insertUser)

        self.retranslateUi(self.insertusr)
        QtCore.QMetaObject.connectSlotsByName(self.insertusr)

    def retranslateUi(self, insertusr):
        _translate = QtCore.QCoreApplication.translate
        insertusr.setWindowTitle(_translate("insertusr", "Form"))
        # self.label.setText(_translate("insertusr", "房间号："))
        # self.label_2.setText(_translate("insertusr", "用户名："))
        # self.label_3.setText(_translate("insertusr", "身份证号："))
        # self.ensureButton.setText(_translate("insertusr", "确认"))

    def insertUser(self):
        # 取输入的用户名与密码
        roomNo = self.roomNoEdit.text()
        userName = self.nameEdit.text()
        passwd = self.pwdEdit.text()

        # 调用控制器的登录认证函数
        controller=M_insertUserController.InsertUserController()
        print(roomNo,userName,passwd)
        message=controller.insert(roomNo,userName,passwd)

        # 根据认证结果弹窗，执行下一步
        Message = QMessageBox()  # 一个消息框
        # 消息框的类型（内置了五种好像）（本体，标题，正文，按键组）
        QMessageBox.information(Message, "Message",message, QMessageBox.Ok)
        self.roomNoEdit.clear()
        self.nameEdit.clear()
        self.pwdEdit.clear()