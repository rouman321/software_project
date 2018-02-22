# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'M_statusdisplay.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from controller.main import M_StatusController
from PyQt5.QtCore import pyqtSignal,QTimer

class Ui_StatusDisplay(QWidget):

    _changedFreq = pyqtSignal(int)

    mtemp=0.00
    mvelocity=0
    controller=M_StatusController.StatusController()
    mfreq=0
    mstrat=0
    mconnec=[]
    mstatus=""

    def setupUi(self, MainWindow):
        self.reflashTimer = QTimer()
        self.reflashTimer.setInterval(2000)
        self.reflashTimer.timeout.connect(self.showCurrentRoom)
        self.reflashTimer.start()

        self.StatusDisplay = QWidget(MainWindow)
        self.StatusDisplay.setObjectName("StatusDisplay")
        self.StatusDisplay.resize(1200, 590)
        self.StatusDisplay.setGeometry(QtCore.QRect(0, 70, 1200, 590))
        jpeg = QtGui.QPixmap()
        jpeg.load("pictures/StatusBg.png")
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.StatusDisplay.backgroundRole(), QtGui.QBrush(jpeg))
        self.StatusDisplay.setPalette(palette1);
        self.StatusDisplay.setAutoFillBackground(True)

        self.tempLabel = QtWidgets.QLabel(self.StatusDisplay)
        self.tempLabel.setGeometry(QtCore.QRect(650, 150, 200, 100))
        self.tempLabel.setObjectName("tempLabel")
        self.tempLabel.setStyleSheet("QLabel{color:rgb(255,255,255);font: 75 30pt \"微软雅黑\";}")

        self.veloLabel = QtWidgets.QLabel(self.StatusDisplay)
        self.veloLabel.setGeometry(QtCore.QRect(950, 150, 150, 90))
        self.veloLabel.setObjectName("veloLabel")
        self.veloLabel.setStyleSheet("QLabel{color:rgb(255,255,255);font: 75 24pt \"微软雅黑\";}")

        self.statuLabel = QtWidgets.QLabel(self.StatusDisplay)
        self.statuLabel.setGeometry(QtCore.QRect(220, 195, 200, 40))
        self.statuLabel.setObjectName("statuLabel")
        self.statuLabel.setStyleSheet("QLabel{color:rgb(255,255,255);font: 75 12pt \"微软雅黑\";}")

        self.statuWidget = QtWidgets.QWidget(self.StatusDisplay)
        self.statuWidget.setGeometry(QtCore.QRect(75, 260, 440, 40))
        self.statuWidget.setObjectName("statuWidget")

        self.modelRadioButton = QtWidgets.QRadioButton(self.statuWidget)
        self.modelRadioButton.setGeometry(QtCore.QRect(0, 0, 132, 34))
        self.modelRadioButton.setObjectName("radioButton")
        self.modelRadioButton.setText("制冷")
        self.modelRadioButton.setStyleSheet("QRadioButton{color:rgb(255,255,255);font: 75 9pt \"微软雅黑\";}")

        self.modelRadioButton_2 = QtWidgets.QRadioButton(self.statuWidget)
        self.modelRadioButton_2.setGeometry(QtCore.QRect(160, 0, 132, 34))
        self.modelRadioButton_2.setObjectName("radioButton_2")
        self.modelRadioButton_2.setText("制热")
        self.modelRadioButton_2.setStyleSheet("QRadioButton{color:rgb(255,255,255);font: 75 9pt \"微软雅黑\";}")

        self.ModelStraconfButton = QtWidgets.QPushButton(self.statuWidget)
        self.ModelStraconfButton.setGeometry(QtCore.QRect(325, 0, 112, 34))
        self.ModelStraconfButton.setObjectName("straconfButton")
        self.ModelStraconfButton.setStyleSheet(
            "QPushButton{border-style:outset;border-radius: 10px;border-color: beige;font: bold 14px;}"
            "QPushButton{background-image: url(pictures/statuButton.png);}"
            "QPushButton:hover{background-image: url(pictures/statuButton.png);}"
            "QPushButton:pressed{background-image: url(pictures/statuButton3.png);}")
        self.ModelStraconfButton.clicked.connect(self.on_ModelButton_clicked)

        self.roomWidget = QtWidgets.QWidget(self.StatusDisplay)
        self.roomWidget.setGeometry(QtCore.QRect(650, 390, 450, 100))
        self.roomWidget.setObjectName("roomWidget")

        self.roomLabel = QtWidgets.QLabel(self.roomWidget)
        self.roomLabel.setGeometry(QtCore.QRect(0, 0, 450, 100))
        self.roomLabel.setObjectName("roomLabel")
        self.roomLabel.setStyleSheet("QLabel{color:rgb(255,255,255);font: 75 14pt \"微软雅黑\";}")

        ##############获取频率——spinbox############
        self.freqSpinbox = QtWidgets.QSpinBox(self.StatusDisplay)
        self.freqSpinbox.setGeometry(QtCore.QRect(145, 120, 100, 40))
        self.freqSpinbox.setObjectName("freqSpinbox")
        self.freqSpinbox.setRange(1, 20)
        self.freqSpinbox.setStyleSheet("border-radius:3px;padding:2px 4px;background-color: rgb(91,155,213,190);color:rgb(255,255,255);font: 8pt '微软雅黑'}")

        self.freqButton = QtWidgets.QPushButton(self.StatusDisplay)
        self.freqButton.setGeometry(QtCore.QRect(330, 123, 112, 34))
        self.freqButton.setObjectName("freqButton")
        self.freqButton.setStyleSheet(
            "QPushButton{border-style:outset;border-radius: 10px;border-color: beige;font: bold 14px;}"
            "QPushButton{background-image: url(pictures/freqButton.png);}"
            "QPushButton:hover{background-image: url(pictures/freqButton.png);}"
            "QPushButton:pressed{background-image: url(pictures/freqButton3.png);}")

        self.freqLabel = QtWidgets.QLabel(self.StatusDisplay)
        self.freqLabel.setGeometry(QtCore.QRect(220, 55, 200, 40))
        self.freqLabel.setObjectName("freqLabel")
        self.freqLabel.setStyleSheet("QLabel{color:rgb(255,255,255);font: 75 12pt \"微软雅黑\";}")

       # self.freqButton.clicked.connect(self.freqChanged)
        ##############获取策略——RadioButton#################
        self.stratWidget = QtWidgets.QWidget(self.StatusDisplay)
        self.stratWidget.setGeometry(QtCore.QRect(75, 410, 452, 22))
        self.stratWidget.setObjectName("stratWidget")

        self.radioButton = QtWidgets.QRadioButton(self.stratWidget)
        self.radioButton.setGeometry(QtCore.QRect(0, 0, 132, 22))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setStyleSheet("QRadioButton{color:rgb(255,255,255);font: 75 9pt \"微软雅黑\";}")

        self.radioButton_2 = QtWidgets.QRadioButton(self.stratWidget)
        self.radioButton_2.setGeometry(QtCore.QRect(160, 0, 132, 22))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setStyleSheet("QRadioButton{color:rgb(255,255,255);font: 75 9pt \"微软雅黑\";}")

        self.radioButton_3 = QtWidgets.QRadioButton(self.stratWidget)
        self.radioButton_3.setGeometry(QtCore.QRect(320, 0, 132, 22))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.setStyleSheet("QRadioButton{color:rgb(255,255,255);font: 75 9pt \"微软雅黑\";}")
        self.radioButton_3.hide()

        self.stratLabel = QtWidgets.QLabel(self.StatusDisplay)
        self.stratLabel.setGeometry(QtCore.QRect(220, 331, 200, 40))
        self.stratLabel.setObjectName("stratLabel")
        self.stratLabel.setStyleSheet("QLabel{color:rgb(255,255,255);font: 75 12pt \"微软雅黑\";}")

        self.straconfButton = QtWidgets.QPushButton(self.StatusDisplay)
        self.straconfButton.setGeometry(QtCore.QRect(250, 470, 112, 34))
        self.straconfButton.setObjectName("straconfButton")
        self.straconfButton.setStyleSheet(
            "QPushButton{border-style:outset;border-radius: 10px;border-color: beige;font: bold 14px;}"
            "QPushButton{background-image: url(pictures/stratButton.png);}"
            "QPushButton:hover{background-image: url(pictures/stratButton.png);}"
            "QPushButton:pressed{background-image: url(pictures/stratButton3.png);}")

        self.showMes()

        self.straconfButton.clicked.connect(self.on_tellmeButton_clicked)

        # ################频率微调和滑块信号槽#############
        # self.freqSlider.valueChanged.connect(self.freqSpinbox.setValue)
        self.freqButton.clicked.connect(self.freqChanged)

        self.retranslateUi(self.StatusDisplay)
        QtCore.QMetaObject.connectSlotsByName(self.StatusDisplay)

    def on_tellmeButton_clicked(self):
        #print("radio changed")
        if (self.radioButton.isChecked()):
            self.controller.strat=1
        if (self.radioButton_2.isChecked()):
            self.controller.strat=2
        if (self.radioButton_3.isChecked()):
            self.controller.strat=3
        self.controller.changeStrat()
        self.showMes()

    def on_ModelButton_clicked(self):
        if (self.modelRadioButton.isChecked()):
            self.controller.changeStatus(0)
        if (self.modelRadioButton_2.isChecked()):
            self.controller.changeStatus(1)
        self.showMes()

    def freqChanged(self):
        self.controller.freq=int(self.freqSpinbox.value())
        print("to change freq as %d" % (self.controller.freq))
        self._changedFreq.emit(self.controller.freq)
        self.controller.changeFreq()
        self.showMes()


    def retranslateUi(self, StatusDisplay):
        _translate = QtCore.QCoreApplication.translate
        StatusDisplay.setWindowTitle(_translate("StatusDisplay", "Form"))
        # self.straconfButton.setText(_translate("StatusDisplay", "确认"))
        # self.freqButton.setText(_translate("StatusDisplay", "确认"))
        # self.label.setText(_translate("StatusDisplay", "温度："))
        # self.label_2.setText(_translate("StatusDisplay", "风速："))
        # self.label_3.setText(_translate("StatusDisplay", "工作模式："))
        self.radioButton.setText(_translate("StatusDisplay", "时间片轮询"))
        self.radioButton_2.setText(_translate("StatusDisplay", "高速风优先"))
        self.radioButton_3.setText(_translate("StatusDisplay", "先来先服务"))
        # self.label_4.setText(_translate("StatusDisplay", "当前连接房间："))

    def showMes(self):
        del self.mconnec[:]
        self.controller.getFreq()
        self.controller.getStrat()
        print("status is ",self.controller.getStatu())
        if(self.controller.getStatu()==0):
            self.mtemp=22.0
            self.modelRadioButton.setChecked(True)
            self.modelRadioButton_2.setChecked(False)
            self.statuLabel.setText("制冷")
        else:
            self.mtemp=28.0
            self.modelRadioButton.setChecked(False)
            self.modelRadioButton_2.setChecked(True)
            self.statuLabel.setText("制热")

        self.tempLabel.setText(str(self.mtemp)+'℃')
        self.showCurrentRoom()
        #####刷新测试
        #self.roomLabel.setNum(time.clock())

        if self.controller.strat==1:
            self.radioButton.setChecked(True)
            self.radioButton_2.setChecked(False)
            self.radioButton_3.setChecked(False)
            self.stratLabel.setText("时间片轮询")
        elif self.controller.strat==2:
            self.radioButton.setChecked(False)
            self.radioButton_2.setChecked(True)
            self.radioButton_3.setChecked(False)
            self.stratLabel.setText("高速风优先抢占")
        elif self.controller.strat==3:
            self.radioButton.setChecked(False)
            self.radioButton_2.setChecked(False)
            self.radioButton_3.setChecked(True)
            self.stratLabel.setText("先来先服务")

        self.freqSpinbox.setValue(self.controller.freq)
        self.freqLabel.setNum(self.controller.freq)

    def showCurrentRoom(self):
        list = self.controller.getConnec()
        x = 0
        connecstr = ""
        while x<len(list):
            connecstr+=str(list[x])
            if(x==2):
                connecstr += "\n"
            else:
                connecstr += "\t"
            x += 1
        self.roomLabel.setText(connecstr)

        if connecstr == "":
            self.veloLabel.setText("待机中")
        else:
            self.veloLabel.setText("工作中")
