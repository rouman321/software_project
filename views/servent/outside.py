# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'outside.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from views.servent.infoshow import Ui_S_Board
from views.servent.S_Cost import Ui_S_Cost
from views.servent.S_login import Ui_S_Login
from models.servent import HeartBeat,Sensor
from models.servent.Servent import S_servent,myroom
from PyQt5.QtWidgets import QMessageBox,QMainWindow
from client import c

class Ui_MainWindow(QMainWindow):
    shutdon = False
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        jpeg = QtGui.QPixmap()
        jpeg.load("pictures/servent/底层背景.jpg")
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.centralwidget.backgroundRole(), QtGui.QBrush(jpeg))
        self.centralwidget.setPalette(palette1);
        # self.centralwidget.setStyleSheet("background-image: url(pictures/background2.png); background-repeat: no-repeat; background-position: center;")
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setMaximumSize(1200, 750)
        self.centralwidget.setMinimumSize(1200, 750)
        self.centralwidget.isMaximized()
        self.centralwidget.showMaximized()

        self.closeWidget = QtWidgets.QWidget(MainWindow)
        self.closeWidget.resize(1200, 750)
        jpeg = QtGui.QPixmap()
        jpeg.load("pictures/servent/关机界面.jpg")
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.closeWidget.backgroundRole(), QtGui.QBrush(jpeg))
        self.closeWidget.setPalette(palette1)
        self.closeWidget.setAutoFillBackground(True)
        self.closeWidget.hide()

        self.ShutDown = QtWidgets.QPushButton(self.centralwidget)
        self.ShutDown.setGeometry(QtCore.QRect(1070,10,60,55))
        self.ShutDown.setObjectName("ShutDown")
        self.ShutDown.setStyleSheet(
            "QPushButton{border-style:outset;border-radius: 10px;border-color: beige;font: bold 14px;}"
            "QPushButton{background-image: url(pictures/servent/CloseButton.png);}"
            "QPushButton:hover{background-image: url(pictures/servent/CloseButton2.png);}"
            "QPushButton:pressed{background-image: url(pictures/servent/CloseButton3.png);}")

        self.InfoShow = QtWidgets.QPushButton(self.centralwidget)
        self.InfoShow.setGeometry(QtCore.QRect(450, 660, 50, 90))
        self.InfoShow.setObjectName("InfoShow")
        self.InfoShow.setStyleSheet(
            "QPushButton{border-style:outset;border-radius: 10px;border-color: beige;font: bold 14px;}"
            "QPushButton{background-image: url(pictures/servent/信息Button.png);}"
            "QPushButton:hover{background-image: url(pictures/servent/信息Button2.png);}"
            "QPushButton:pressed{background-image: url(pictures/servent/信息Button3.png);}")
        self.InfoShow.setEnabled(False)

        self.CostShow = QtWidgets.QPushButton(self.centralwidget)
        self.CostShow.setGeometry(QtCore.QRect(750, 660, 50, 90))
        self.CostShow.setObjectName("CostShow")
        self.CostShow.setStyleSheet(
            "QPushButton{border-style:outset;border-radius: 10px;border-color: beige;font: bold 14px;}"
            "QPushButton{background-image: url(pictures/servent/账单Button.png);}"
            "QPushButton:hover{background-image: url(pictures/servent/账单Button2.png);}"
            "QPushButton:pressed{background-image: url(pictures/servent/账单Button3.png);}")
        self.CostShow.setEnabled(False)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(550, 0, 100, 50))
        self.label.setStyleSheet("font: 75 20pt \"微软雅黑\";color:rgb(150,179,205)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        # pe = QtGui.QPalette()
        # pe.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)  # 设置字体颜色
        # self.label.setPalette(pe)
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 新建登录界面
        self.loginwidget = Ui_S_Login()
        self.loginwidget.setupUi(self.centralwidget)
        self.loginwidget.show()
        self.loginwidget._haslogged.connect(self.logged)

        # 信号与槽
        self.ShutDown.clicked.connect(self.shutdown_request)   #关机请求
        #关机成功信号，关闭窗口or回到登录界面？

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.heart = HeartBeat.HeartBeat()

        c._connectFailed.connect(self.connectFailed)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #self.ShutDown.setText(_translate("MainWindow", "关机"))
        #self.InfoShow.setText(_translate("MainWindow", "信息展示"))
        #self.CostShow.setText(_translate("MainWindow", "账单展示"))
        #self.label.setText(_translate("MainWindow", "房间号"))

    #信息展示
    def infoshow_clk(self):
        self.costwidget.hide()
        self.boardwidget.show()

    #账单展示
    def costshow_clk(self):
        self.boardwidget.hide()
        self.costwidget.show()

    #关机请求
    def shutdown_request(self):
        self.shutdon = True
        print("shutdown_request")
        self.closeWidget.show()
        try:
            self.heart.timerStop()
            self.sensor.timerStop()
            self.boardwidget.timer.stop()
            c.closeCon()
        except:
            print("未登入")
        #QCoreApplication.instance().quit()
        #与主机通信

    # 登录成功后，创建心跳类，还有传感器！！（因为传感器的时间间隔是恒定的）
    # 可能还要在这里创建从机类。。
    def logged(self,roomNo,Name,Password,Mode):
        # 初始化一个servent,修改py文件中的单例指向这个实例
        myroom = S_servent(roomNo,Name,Password,Mode)
        print(myroom)
        self.heart.setServent(myroom)
        self.sensor = Sensor.Sensor(myroom)
        # 新建信息显示界面

        self.boardwidget = Ui_S_Board()
        self.boardwidget.setupUi(self.centralwidget,myroom)
        self.boardwidget.hide()
        print("=============================")

        # 新建账单显示界面
        self.costwidget = Ui_S_Cost()
        self.costwidget.setupUi(self.centralwidget,myroom)
        self.costwidget.hide()
        self.infoshow_clk()

        # 信号与槽
        self.InfoShow.clicked.connect(self.infoshow_clk)  # 信息展示
        self.CostShow.clicked.connect(self.costshow_clk)  # 账单展示

        self.label.setText(str(roomNo))
        self.InfoShow.setEnabled(True)
        self.CostShow.setEnabled(True)

    def connectFailed(self):
        try:
            myroom.start_blowing = 0
        except:
            print("myroom not set")

        #关机引起的断线不做这个处理
        if(self.shutdon == True):
            return

        Message = QMessageBox()  # 一个消息框
        button =  QMessageBox.information(Message, "Message","与主机建立连接失败，是否重试？", QMessageBox.Cancel|QMessageBox.Ok)
        if button == QMessageBox.Cancel:
            self.shutdown_request()
        elif button == QMessageBox.Ok:
            c.reconnect()
    #关机处理
    #def shutdown_ok(self):
