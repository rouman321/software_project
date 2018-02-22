# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from views.main import M_statusDisplay, M_subMonitor, M_report, M_insertuser,M_login
from models.main.HeartBeat import HeartBeat
from server import server
import sys
import datetime

class M_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        jpeg = QtGui.QPixmap()
        jpeg.load("pictures/background3.png")
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.centralwidget.backgroundRole(), QtGui.QBrush(jpeg))
        self.centralwidget.setPalette(palette1);
        # self.centralwidget.setStyleSheet("background-image: url(pictures/background2.png); background-repeat: no-repeat; background-position: center;")
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setMaximumSize(1200, 750)
        self.centralwidget.setMinimumSize(1200, 750)
        self.centralwidget.isMaximized()
        self.centralwidget.showMaximized()

        self.closeWidget=QtWidgets.QWidget(MainWindow)
        self.closeWidget.resize(1200,750)
        jpeg = QtGui.QPixmap()
        jpeg.load("pictures/CloseWidget.png")
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.closeWidget.backgroundRole(), QtGui.QBrush(jpeg))
        self.closeWidget.setPalette(palette1)
        self.closeWidget.setAutoFillBackground(True)
        self.closeWidget.hide()
        # 按键声明
        self.homeButton = QtWidgets.QPushButton(self.centralwidget)
        self.homeButton.setGeometry(QtCore.QRect(125, 660, 50, 90))
        self.homeButton.setObjectName("homeButton")
        self.homeButton.setStyleSheet("QPushButton{border-style:outset;border-radius: 10px;border-color: beige;font: bold 14px;}"
                                      "QPushButton{background-image: url(pictures/HomeButton.png);}" 
                                      "QPushButton:hover{background-image: url(pictures/HomeButton2.png);}" 
                                      "QPushButton:pressed{background-image: url(pictures/HomeButton3.png);}")
        self.homeButton.setEnabled(False)

        self.monitorButton = QtWidgets.QPushButton(self.centralwidget)
        self.monitorButton.setGeometry(QtCore.QRect(425, 660, 50, 90))
        self.monitorButton.setObjectName("monitorButton")
        self.monitorButton.setEnabled(False)
        self.monitorButton.setStyleSheet(
            "QPushButton{border-style:outset;border-radius: 10px;border-color: beige;font: bold 14px;}"
            "QPushButton{background-image: url(pictures/MonitorButton.png);}"
            "QPushButton:hover{background-image: url(pictures/MonitorButton2.png);}"
            "QPushButton:pressed{background-image: url(pictures/MonitorButton3.png);}")

        self.reportButton = QtWidgets.QPushButton(self.centralwidget)
        self.reportButton.setGeometry(QtCore.QRect(725, 660, 50, 90))
        self.reportButton.setObjectName("reportButton")
        self.reportButton.setEnabled(False)
        self.reportButton.setStyleSheet(
            "QPushButton{border-style:outset;border-radius: 10px;border-color: beige;font: bold 14px;}"
            "QPushButton{background-image: url(pictures/ReportButton.png);}"
            "QPushButton:hover{background-image: url(pictures/ReportButton2.png);}"
            "QPushButton:pressed{background-image: url(pictures/ReportButton3.png);}")

        self.insertusrButton = QtWidgets.QPushButton(self.centralwidget)
        self.insertusrButton.setGeometry(QtCore.QRect(1025, 660, 50, 90))
        self.insertusrButton.setObjectName("insertusrButton")
        self.insertusrButton.setEnabled(False)
        self.insertusrButton.setStyleSheet(
            "QPushButton{border-style:outset;border-radius: 10px;border-color: beige;font: bold 14px;}"
            "QPushButton{background-image: url(pictures/UserButton.png);}"
            "QPushButton:hover{background-image: url(pictures/UserButton2.png);}"
            "QPushButton:pressed{background-image: url(pictures/UserButton3.png);}")

        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(1070,10,60,55))
        self.closeButton.setObjectName("closeButton")
        self.closeButton.setStyleSheet(
            "QPushButton{border-style:outset;border-radius: 10px;border-color: beige;font: bold 14px;}"
            "QPushButton{background-image: url(pictures/CloseButton.png);}"
            "QPushButton:hover{background-image: url(pictures/CloseButton2.png);}"
            "QPushButton:pressed{background-image: url(pictures/CloseButton3.png);}")


        self.loginWidget=M_login.Ui_Form()
        M_login.Ui_Form.setupUi(self.loginWidget,self.centralwidget)


        self.defaultWidget = M_statusDisplay.Ui_StatusDisplay()
        M_statusDisplay.Ui_StatusDisplay.setupUi(self.defaultWidget, self.centralwidget)
        self.HeartBeat = HeartBeat(self.defaultWidget.controller.freq)  # 创建心跳包
        self.defaultWidget._changedFreq.connect(self.HeartBeat.changeSubmintFreq)

        self.monitorWidget = M_subMonitor.Ui_SubMonitor()
        M_subMonitor.Ui_SubMonitor.setupUi(self.monitorWidget, self.centralwidget)

        self.reportWidget = M_report.Ui_Report()
        M_report.Ui_Report.setupUi(self.reportWidget, self.centralwidget)

        self.insertusrWidget = M_insertuser.Ui_insertusr()
        M_insertuser.Ui_insertusr.setupUi(self.insertusrWidget, self.centralwidget)



        #############堆栈窗口##############
        self.stack = QtWidgets.QStackedWidget(self.centralwidget)
        self.stack.hide()
        self.stack.addWidget(self.defaultWidget.StatusDisplay)
        self.stack.addWidget(self.monitorWidget.SubMonitor)
        self.stack.addWidget(self.reportWidget.Report)
        self.stack.addWidget(self.insertusrWidget.insertusr)
        self.stack.setGeometry(QtCore.QRect(0, 70, 1200, 590))
        # jpeg = QtGui.QPixmap()
        # jpeg.load("pictures/widgetbg2.png")
        # palette1 = QtGui.QPalette()
        # palette1.setBrush(self.stack.backgroundRole(), QtGui.QBrush(jpeg))
        # self.stack.setPalette(palette1)
        # self.stack.setAutoFillBackground(True)

        self.loginWidget._haslogged.connect(self.run)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1053, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        ###############按键们的信号槽########################
        self.homeButton.clicked.connect(self.setHomeWideget)
        self.monitorButton.clicked.connect(self.setMonitorWideget)
        self.reportButton.clicked.connect(self.setReportWidget)
        self.insertusrButton.clicked.connect(self.setInsertWidget)
        #self.closeButton.clicked.connect(sys.exit)
        self.closeButton.clicked.connect(self.close)

        ''''
        self.straconfButton.clicked.connect(self.on_tellmeButton_clicked)

        ################频率微调和滑块信号槽#############
        self.freqSlider.valueChanged.connect(self.freqSpinbox.setValue)
        self.freqSpinbox.valueChanged.connect(self.freqSlider.setValue)
        '''

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    # def exit(self):


    def setMonitorWideget(self):
        self.monitorWidget.updateData()  ####每次打开界面前更新一遍数据
        self.stack.setCurrentWidget(self.monitorWidget.SubMonitor)
        print(self.monitorWidget.messagelist)

    def setHomeWideget(self):
        self.defaultWidget.showMes()
        self.stack.setCurrentWidget(self.defaultWidget.StatusDisplay)

    def setReportWidget(self):
        self.reportWidget.iniUiReport()
        self.stack.setCurrentWidget(self.reportWidget.Report)

    def setInsertWidget(self):
        self.stack.setCurrentWidget(self.insertusrWidget.insertusr)

    def run(self):
        self.homeButton.setEnabled(True)
        self.monitorButton.setEnabled(True)
        self.reportButton.setEnabled(True)
        self.insertusrButton.setEnabled(True)
        self.stack.show()

    def close(self):
        self.centralwidget.hide()
        self.closeWidget.show()
        server.closeCon()
        self.HeartBeat.timer.stop()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.homeButton.setText(_translate("MainWindow", "主页"))
        # self.monitorButton.setText(_translate("MainWindow", "监视"))
        # self.reportButton.setText(_translate("MainWindow", "报表"))
        # self.closeButton.setText(_translate("MainWindow", "关机"))
        # self.insertusrButton.setText(_translate("MainWindow", "用户登记"))



# if __name__ == '__main__':
#      app = QApplication(sys.argv)
#      MainWindow = QMainWindow()
#      ui = M_MainWindow()
#      ui.setupUi(MainWindow)
#      MainWindow.show()
#      sys.exit(app.exec_())


