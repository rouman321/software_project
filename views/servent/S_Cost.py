# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'S_Cost.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from controller.servent.S_CostController import S_CostController

class Ui_S_Cost(QWidget):
    def setupUi(self, parent,servent):
        self.controller = S_CostController(servent)
        self.parent = parent

        # 子界面上的作画区
        self.Form = QWidget(parent)  # 生成在父界面上
        self.Form.setGeometry(QtCore.QRect(0,70,1200,590))
        self.Form.setObjectName("Form")
        self.Form.resize(1200, 590)
        jpeg = QtGui.QPixmap()
        jpeg.load("pictures/servent/消费背景.jpg")
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.Form.backgroundRole(), QtGui.QBrush(jpeg))
        self.Form.setPalette(palette1)
        self.Form.setAutoFillBackground(True)

        #################消费结果展示界面￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥
        self.displayborad = QtWidgets.QWidget(self.Form)
        self.displayborad.setGeometry(QtCore.QRect(0,0,1200,590))
        self.displayborad.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.displayborad.setObjectName("displayborad")
        ##时间消费展示
        self.time_display = QtWidgets.QWidget(self.displayborad)
        self.time_display.setGeometry(QtCore.QRect(0,160, 550, 100))
        self.time_display.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.time_display.setObjectName("time_display")
        # self.timecost_label = QtWidgets.QLabel(self.time_display)
        # self.timecost_label.setGeometry(QtCore.QRect(35, 20, 221, 81))
        self.timecost_lcd = QtWidgets.QLCDNumber(self.time_display)
        self.timecost_lcd.setGeometry(QtCore.QRect(0,10,500,80))
        self.timecost_lcd.setStyleSheet("background-color: rgb(255, 255, 255,0);color:rgb(255,255,255)")
        self.timecost_lcd.setObjectName("timecost_lcd")
        self.timecost_lcd.setDigitCount(10)
        # font = QtGui.QFont()
        # font.setFamily("00 Starmap Truetype")
        # font.setPointSize(11)
        # self.timecost_label.setFont(font)
        # self.timecost_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.timecost_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        # self.timecost_label.setObjectName("timecost_label")

        ##金钱消费展示
        self.monycost_display = QtWidgets.QWidget(self.displayborad)
        self.monycost_display.setGeometry(QtCore.QRect(700, 140, 400, 110))
        self.monycost_display.setObjectName("monycost_display")
        self.monycost_display.setStyleSheet("background-color: rgba(0,0,0,0);")
        # self.monycost_label = QtWidgets.QLabel(self.monycost_display)
        # self.monycost_label.setGeometry(QtCore.QRect(50, 15, , 81))
        # font = QtGui.QFont()
        # font.setFamily("00 Starmap Truetype")
        # font.setPointSize(11)
        # self.monycost_label.setFont(font)
        # self.monycost_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.monycost_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        # self.monycost_label.setObjectName("monycost_label")
        self.monycost_lcd = QtWidgets.QLCDNumber(self.monycost_display)
        self.monycost_lcd.setGeometry(QtCore.QRect(50,15,300,80))
        self.monycost_lcd.setStyleSheet("background-color: rgb(255, 255, 255,0);color:rgb(255,255,255)")
        self.monycost_lcd.setObjectName("monycost_lcd")
        self.timecost_lcd.setDigitCount(10)

        ##能量消费展示
        self.energe_display = QtWidgets.QWidget(self.displayborad)
        self.energe_display.setGeometry(QtCore.QRect(700, 380, 400, 110))
        self.energe_display.setObjectName("energe_display")
        self.energe_display.setStyleSheet("background-color: rgba(0,0,0,0);")
        # self.energy_label = QtWidgets.QLabel(self.energe_display)
        # self.energy_label.setGeometry(QtCore.QRect(35, 20, 221, 81))
        # font = QtGui.QFont()
        # font.setFamily("00 Starmap Truetype")
        # font.setPointSize(11)
        # self.energy_label.setFont(font)
        # self.energy_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.energy_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        # self.energy_label.setObjectName("energy_label")
        self.energy_lcd = QtWidgets.QLCDNumber(self.energe_display)
        self.energy_lcd.setGeometry(QtCore.QRect(50,15,300,80))
        self.energy_lcd.setStyleSheet("background-color: rgb(255, 255, 255,0);color:rgb(255,255,255)")
        self.energy_lcd.setObjectName("energy_lcd")
        self.timecost_lcd.setDigitCount(10)

        ######小贴士####################################################
        # self.notes = QtWidgets.QWidget(self.Form)
        # self.notes.setGeometry(QtCore.QRect(110, 430, 600, 80))
        # self.notes.setStyleSheet("background-color: rgba(170, 255, 127, 180);")
        # self.notes.setObjectName("notes")
        # self.label = QtWidgets.QLabel(self.notes)
        # self.label.setGeometry(QtCore.QRect(20, 10, 541, 60))
        # font = QtGui.QFont()
        # font.setFamily("00 Starmap Truetype")
        # font.setPointSize(12)
        # self.label.setFont(font)
        # self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.label.setObjectName("label")


        #self.closeButton= QtWidgets.QPushButton(self.Form)
        #self.closeButton.setGeometry(QtCore.QRect(740, 20, 40, 40))
        # self.pushButton.setStyleSheet("border-radius:10px;background-color: rgb(255, 255, 255);")
        #self.closeButton.setObjectName("closeButton")
        #self.closeButton.clicked.connect(self.hide)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.Form)

        #刷新定时器
        self.timer = QTimer()
        self.timer.setInterval(800)
        self.timer.start()
        self.timer.timeout.connect(self.showCost)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Form.setWindowTitle(_translate("Form", "Form"))
        # self.timecost_label.setText(_translate("Form", "已使用时长："))
        # self.monycost_label.setText(_translate("Form", "已消费金额（元）："))
        # self.energy_label.setText(_translate("Form", "已消费能量（kwh):"))
        # self.label.setText(_translate("Form", "小贴士：空调虽然舒适，也不要忘记节能噢~"))

    def show(self):
        self.Form.raise_()
        self.Form.show()
        self.showCost()
        self.timer.start()

    def hide(self):
        self.Form.hide()
        self.timer.stop()

    def showCost(self):
        self.timecost_lcd.display("%02d:%02d:%02d" % (self.controller.getTimeCost()))
        self.energy_lcd.display("%.2f" % (self.controller.getEngCost()))
        self.monycost_lcd.display("%.2f" % (self.controller.getMoneyCost()))



