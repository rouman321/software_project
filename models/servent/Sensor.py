# -*- coding: utf-8 -*-
from PyQt5.QtCore import *


class Sensor:
    init_interval = 1000#一分钟更新一次还是怎样。。。
    rate = 0.01#风速变化快慢（快了调小）
    def __init__(self, servent):
        # 定时器
        self.timer = QTimer()
        self.timer.setInterval(self.init_interval)
        self.timer.start()

        # 记下作为操作目标的从机状态类
        self.servent = servent
        print('sensor set')
        self.timer.timeout.connect(self.state_update)

    def state_update(self):
        # 做状态更新
        '''
        应该是先调用下计算函数算下现在的温度
        然后通过self.target的set_temp之类的方法（接口去问）来更新它
        不用操作数据库！
        '''
        #风速比率
        if(self.servent.start_blowing==0):
            self.wind_lv = 0
        elif(self.servent.sysW==1):
            self.wind_lv = 0.8
        elif(self.servent.sysW==2):
            self.wind_lv = 1.3
        elif(self.servent.sysW==3):
            self.wind_lv = 1.8
        #根据模式假定风温外温
        if (self.servent.sysModel == 0):#制冷
            self.wind_temp = 18
            self.extern_temp = 30
        elif (self.servent.sysModel == 1):#制热
            self.wind_temp = 30
            self.extern_temp = 15
        #温度向外温靠近+向风温靠近（6倍风速比率补正）
        sT = self.servent.sysT + 6*self.rate*self.wind_lv*(self.wind_temp-self.servent.sysT) + \
                            self.rate*(self.extern_temp-self.servent.sysT)
        self.servent.update_rt(sT)

    def timerStop(self):
        self.timer.stop()