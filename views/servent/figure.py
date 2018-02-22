# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import animation
from matplotlib import pyplot as plt


class Figure_Canvas(FigureCanvas):   # 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplotlib的关键

    def __init__(self, parent=None, width=5.8, height=3.85, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=100)
        # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure

        FigureCanvas.__init__(self, self.fig)
        # 初始化父类
        self.setParent(parent)

        self.axes = self.fig.add_subplot(111)
        # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法

        self.axes.set_xlim(0,60)
        self.axes.set_ylim(16,32)

        self.axes.set_title('line chart')
        self.axes.set_xlabel('time')
        self.axes.set_ylabel('temperature')

        self.syst = []
        self.tart = []
        self.x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
        self.cnt = 0

        self.line1, = self.axes.plot([], [],'b-', label = "实时温度")
        self.line2, = self.axes.plot([], [],'r-', label = "目标温度")

    #def init(self):
        #self.line1.set_data([],[])
        #self.line2.set_data([],[])
        #return self.line1, self.line2
        #print("init")
    def animate(self):
        print("aaaaaa")
        print(self.syst)
        print(self.tart)
        print(self.x[0:self.cnt])
        self.line1.set_data(self.x[0:self.cnt], self.syst)
        self.line2.set_data(self.x[0:self.cnt], self.tart)
        self.draw()
        print("finished")
        #return self.line1, self.line2

    def test(self,ST,TT):
        self.sysT=ST
        self.tarT=TT
        if (self.cnt < 61):
            self.syst.append(self.sysT)
            self.tart.append(self.tarT)
            self.cnt = self.cnt + 1
        else:
            self.syst.pop(0)
            self.tart.pop(0)
            self.syst.append(self.sysT)
            self.tart.append(self.tarT)
        print("eee")
        self.animate()


