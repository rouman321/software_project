# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'infoshow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
#数据类
from views.servent.figure import Figure_Canvas
from controller.servent.SBoardControl import S_BoardController
from datetime  import  *


class Ui_S_Board(QtWidgets.QWidget):
    init_interval = 1000 #界面更新频率
    #start = QtCore.pyqtSignal()
    def setupUi(self, parent,servent):
        self.S_Board = QtWidgets.QWidget(parent) #生成在父界面上
        self.S_Board.setObjectName("S_Board")
        self.S_Board.resize(1200, 590)
        self.S_Board.setGeometry(QtCore.QRect(0,70,1200,590))  #展示窗口定位
        jpeg = QtGui.QPixmap()
        jpeg.load("pictures/servent/信息背景.jpg")
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.S_Board.backgroundRole(), QtGui.QBrush(jpeg))
        self.S_Board.setPalette(palette1)
        self.S_Board.setAutoFillBackground(True)

        self.windshow = QtWidgets.QComboBox(self.S_Board)
        self.windshow.setGeometry(QtCore.QRect(350, 430, 110, 30))
        self.windshow.setStyleSheet("border-radius:3px;padding:2px 4px;"
                                       "background-color: rgb(91,155,213,190);"
                                       "color:rgb(255,255,255);font: 9pt '微软雅黑'}")
        self.windshow.setObjectName("windshow")
        self.windshow.addItem("")
        self.windshow.addItem("")
        self.windshow.addItem("")


        self.windstate = QtWidgets.QLabel(self.S_Board)    #当前状态
        self.windstate.setGeometry(QtCore.QRect(1000, 70, 150, 50))
        self.windstate.setStyleSheet("font: 75 12pt \"微软雅黑\";")
        # self.windlabel.setAlignment(QtCore.Qt.AlignCenter)
        pe = QtGui.QPalette()
        pe.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)  # 设置字体颜色
        self.windstate.setPalette(pe)
        self.windstate.setObjectName("windstate")

        # self.wslabel = QtWidgets.QLabel(self.S_Board)  # 当前状态
        # self.wslabel.setGeometry(QtCore.QRect(800, 100, 150, 50))
        # self.wslabel.setStyleSheet("font: 75 20pt \"微软雅黑\";")
        # # self.windlabel.setAlignment(QtCore.Qt.AlignCenter)
        # pe = QtGui.QPalette()
        # pe.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)  # 设置字体颜色
        # self.wslabel.setPalette(pe)
        # self.wslabel.setObjectName("windstate")


        # self.windlabel = QtWidgets.QLabel(self.S_Board)
        # self.windlabel.setGeometry(QtCore.QRect(200, 0, 150, 50))
        # self.windlabel.setStyleSheet("font: 75 20pt \"微软雅黑\";")
        # #self.windlabel.setAlignment(QtCore.Qt.AlignCenter)
        # pe = QtGui.QPalette()
        # pe.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)  # 设置字体颜色
        # self.windlabel.setPalette(pe)
        # self.windlabel.setObjectName("windlabel")

        self.rwshow = QtWidgets.QLabel(self.S_Board)
        self.rwshow.setGeometry(QtCore.QRect(100,400,150,100))
        self.rwshow.setStyleSheet("font: 75 24pt \"微软雅黑\";")
        # self.windlabel.setAlignment(QtCore.Qt.AlignCenter)
        pe = QtGui.QPalette()
        pe.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)  # 设置字体颜色
        self.rwshow.setPalette(pe)
        self.rwshow.setObjectName("rwshow")

        # self.rwlabel = QtWidgets.QLabel(self.S_Board)
        # self.rwlabel.setGeometry(QtCore.QRect(200, 100, 150, 50))
        # self.rwlabel.setStyleSheet("font: 75 20pt \"微软雅黑\";")
        # # self.windlabel.setAlignment(QtCore.Qt.AlignCenter)
        # pe = QtGui.QPalette()
        # pe.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)  # 设置字体颜色
        # self.rwlabel.setPalette(pe)
        # self.rwlabel.setObjectName("rwlabel")

        # self.dtlabel = QtWidgets.QLabel(self.S_Board)
        # self.dtlabel.setGeometry(QtCore.QRect(500, 0, 150, 50))
        # self.dtlabel.setStyleSheet("font: 75 20pt \"微软雅黑\";")
        # # self.windlabel.setAlignment(QtCore.Qt.AlignCenter)
        # pe = QtGui.QPalette()
        # pe.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)  # 设置字体颜色
        # self.dtlabel.setPalette(pe)
        # self.dtlabel.setObjectName("dtlabel")
        self.dtshow_cold = QtWidgets.QComboBox(self.S_Board)
        self.dtshow_cold.setGeometry(QtCore.QRect(350, 180, 110, 30))
        self.dtshow_cold.setStyleSheet("border-radius:3px;padding:2px 4px;"
                                       "background-color: rgb(91,155,213,190);"
                                       "color:rgb(255,255,255);font: 9pt '微软雅黑'}")
        self.dtshow_cold.setObjectName("dtshow_cold")
        self.dtshow_cold.addItem("25")
        self.dtshow_cold.addItem("24")
        self.dtshow_cold.addItem("23")
        self.dtshow_cold.addItem("22")
        self.dtshow_cold.addItem("21")
        self.dtshow_cold.addItem("20")
        self.dtshow_cold.addItem("19")
        self.dtshow_cold.addItem("18")
        self.dtshow_hot = QtWidgets.QComboBox(self.S_Board)
        self.dtshow_hot.setGeometry(QtCore.QRect(350, 180, 110, 30))
        self.dtshow_hot.setStyleSheet("border-radius:3px;padding:2px 4px;"
                                       "background-color: rgb(91,155,213,190);"
                                       "color:rgb(255,255,255);font: 9pt '微软雅黑'}")
        self.dtshow_hot.setObjectName("dtshow_hot")
        self.dtshow_hot.addItem("30")
        self.dtshow_hot.addItem("29")
        self.dtshow_hot.addItem("28")
        self.dtshow_hot.addItem("27")
        self.dtshow_hot.addItem("26")
        self.dtshow_hot.addItem("25")

        # self.rtlabel = QtWidgets.QLabel(self.S_Board)
        # self.rtlabel.setGeometry(QtCore.QRect(500, 100, 150, 50))
        # self.rtlabel.setStyleSheet("font: 75 20pt \"微软雅黑\";")
        # # self.windlabel.setAlignment(QtCore.Qt.AlignCenter)
        # pe = QtGui.QPalette()
        # pe.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)  # 设置字体颜色
        # self.rtlabel.setPalette(pe)
        # self.rtlabel.setObjectName("rtlabel")
        self.rtshow = QtWidgets.QLabel(self.S_Board)
        self.rtshow.setGeometry(QtCore.QRect(90,150,180,100))
        self.rtshow.setStyleSheet("font: 75 24pt \"微软雅黑\";")
        # self.windlabel.setAlignment(QtCore.Qt.AlignCenter)
        pe = QtGui.QPalette()
        pe.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)  # 设置字体颜色
        self.rtshow.setPalette(pe)
        self.rtshow.setObjectName("rtshow")



        # self.modellabel = QtWidgets.QLabel(self.S_Board)
        # self.modellabel.setGeometry(QtCore.QRect(800, 0, 150, 50))
        # self.modellabel.setStyleSheet("font: 75 20pt \"微软雅黑\";")
        # # self.windlabel.setAlignment(QtCore.Qt.AlignCenter)
        # pe = QtGui.QPalette()
        # pe.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)  # 设置字体颜色
        # self.modellabel.setPalette(pe)
        # self.modellabel.setObjectName("modellabel")
        self.modelshow = QtWidgets.QLabel(self.S_Board)
        self.modelshow.setGeometry(QtCore.QRect(710, 70, 100, 50))
        self.modelshow.setStyleSheet("font: 75 12pt \"微软雅黑\";")
        # self.windlabel.setAlignment(QtCore.Qt.AlignCenter)
        pe = QtGui.QPalette()
        pe.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)  # 设置字体颜色
        self.modelshow.setPalette(pe)
        self.modelshow.setObjectName("modelshow")

        self.gridLayoutWidget = QtWidgets.QWidget(self.S_Board)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(550, 140, 600, 390))  # 定义gridLayout控件的大小和位置，4个数字分别为左边坐标，上边坐标，长，宽
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        # 在gridLayoutWidget 上创建一个网格Layout，注意以gridLayoutWidget为参
        self.gridLayout_2.setObjectName("gridLayout_2")
        # ===通过graphicview来显示图形
        self.graphicview = QtWidgets.QGraphicsView(self.S_Board)
        # 第一步，创建一个QGraphicsView，注意同样以gridLayoutWidget为参
        self.graphicview.setObjectName("graphicview")
        self.gridLayout_2.addWidget(self.graphicview, 0, 0)
        #第二步，将该QGraphicsView放入Layout中

        self.dr = Figure_Canvas()
        #实例化一个FigureCanvas
        self.graphicscene = QtWidgets.QGraphicsScene()
        # 第三步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        self.graphicscene.addWidget(self.dr)
        # 第四步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        self.graphicview.setScene(self.graphicscene)
        # 第五步，把QGraphicsScene放入QGraphicsView
        self.graphicview.show()
        # 最后，调用show方法呈现图形

        self.controller = S_BoardController(servent)

        self.retranslateUi(self.S_Board)
        QtCore.QMetaObject.connectSlotsByName(self.S_Board)

        # 刷新定时器
        self.timer = QtCore.QTimer()
        self.timer.setInterval(self.init_interval)

        #信号与槽连接
        self.timer.timeout.connect(self.painting)
        self.windshow.currentIndexChanged.connect(self.wind_change)
        self.dtshow_hot.currentIndexChanged.connect(self.t_raise)
        self.dtshow_cold.currentIndexChanged.connect(self.t_raise)

        self.getCurrentState()

        self.wpre = datetime.now()#用来处理命令发送问题的 待定！！！
        self.tpre = datetime.now()#用来处理命令发送问题的 待定！！！

        self.timer.start()
        self.controller._modelchanged.connect(self.alertModelChange)
        print("success init infoshow")

    def alertModelChange(self,reset):
        # 根据判断结果，决定是否弹窗
        if reset == True:
            print("to show message box")
            Message = QMessageBox()  # 一个消息框
            # 消息框的类型（内置了五种好像）（本体，标题，正文，按键组）
            QMessageBox.information(Message, "Message", "主机当前工作模式发生变化，从机已重置", QMessageBox.Ok)
        self.show()

    def retranslateUi(self, S_Board):
        _translate = QtCore.QCoreApplication.translate
        S_Board.setWindowTitle(_translate("S_Board", "Form"))
        self.windshow.setItemText(0, _translate("S_Board", "high"))
        self.windshow.setItemText(1, _translate("S_Board", "mid"))
        self.windshow.setItemText(2, _translate("S_Board", "low"))
        self.windstate.setText(_translate("S_Board", "待机"))
        # self.windlabel.setText(_translate("S_Board", "目标风速"))
        self.rwshow.setText(_translate("S_Board", "mid"))
        # self.rwlabel.setText(_translate("S_Board", "实际风速"))
        # self.dtlabel.setText(_translate("S_Board", "目标温度"))
        self.dtshow_cold.setItemText(0, _translate("S_Board", "25"))
        self.dtshow_cold.setItemText(1, _translate("S_Board", "24"))
        self.dtshow_cold.setItemText(2, _translate("S_Board", "23"))
        self.dtshow_cold.setItemText(3, _translate("S_Board", "22"))
        self.dtshow_cold.setItemText(4, _translate("S_Board", "21"))
        self.dtshow_cold.setItemText(5, _translate("S_Board", "20"))
        self.dtshow_cold.setItemText(6, _translate("S_Board", "19"))
        self.dtshow_cold.setItemText(7, _translate("S_Board", "18"))
        # self.rtlabel.setText(_translate("S_Board", "实际温度"))
        self.rtshow.setText(_translate("S_Board", "29度"))
        self.dtshow_hot.setItemText(0, _translate("S_Board", "30"))
        self.dtshow_hot.setItemText(1, _translate("S_Board", "29"))
        self.dtshow_hot.setItemText(2, _translate("S_Board", "28"))
        self.dtshow_hot.setItemText(3, _translate("S_Board", "27"))
        self.dtshow_hot.setItemText(4, _translate("S_Board", "26"))
        self.dtshow_hot.setItemText(5, _translate("S_Board", "25"))
        # self.modellabel.setText(_translate("S_Board", "当前模式"))
        self.modelshow.setText(_translate("S_Board", "制冷"))
        # self.wslabel.setText(_translate("S_Board", "当前状态"))

    def hide(self):
        self.S_Board.hide()

    def show(self):
        #raise函数？？？？？
        self.S_Board.show()
        if(self.sysModel == 0):
            self.dtshow_cold.show()
            self.dtshow_hot.hide()
            self.modelshow.setText("制冷")
        else:
            self.dtshow_hot.show()
            self.dtshow_cold.hide()
            self.modelshow.setText("供暖")
        self.getCurrentState()  # 更新数据
        if (self.sysModel == 1):
            index_temp = self.dtshow_hot.findText('%d' % int(self.targetT))
            self.dtshow_hot.setCurrentIndex(index_temp)
        else:
            index_temp = self.dtshow_cold.findText('%d' % int(self.targetT))
            self.dtshow_cold.setCurrentIndex(index_temp)
        if (self.targetW == 1):
            ww = 'low'
        elif (self.targetW == 2):
            ww = 'mid'
        else:
            ww = 'high'
        index_temp = self.windshow.findText(ww)
        self.windshow.setCurrentIndex(index_temp)

    def painting(self):
        self.getCurrentState() #更新数据
        print("painting")
        self.dr.test(self.sysT,self.targetT)
        self.rtshow.setText("%.2f℃" % self.sysT)

        if (self.sysW == 1):
            ww = 'low'
        elif (self.sysW == 2):
            ww = 'mid'
        elif(self.sysW == 3):
            ww = 'high'
        else:
            ww= "不送风"
        if (self.start_blowing == 0):
            self.windstate.setText("待机中")
            ww = "不送风"
        else:
            self.windstate.setText("运行中")
        self.rwshow.setText(ww)

    def wind_change(self):
        now = datetime.now() #信息发送处理
        #if((int)(now - self.wpre).seconds >= 1):
        print("into")
        tempw=self.windshow.currentText()
        if(tempw == "low"):
            ww = 1
        elif(tempw == "mid"):
            ww = 2
        else:
            ww = 3
        self.controller.Wind_Change(ww)


    def t_raise(self):
        print("into")
        if(self.sysModel == 1):
            print(self.dtshow_hot.currentText())
            self.controller.T_raise(float(self.dtshow_hot.currentText()))
        else:
            print(self.dtshow_hot.currentText())
            self.controller.T_raise(float(self.dtshow_cold.currentText()))

    def getCurrentState(self):
        self.roomNo, self.targetT, self.targetW, self.sysT, self.sysW, self.sysModel, self.loggedOn, self.eng_cost, self.money_cost, self.start_blowing = self.controller.getCurrentState()

