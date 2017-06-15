# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from client import c
import time

class HeartBeat:
    init_interval = 1000
    current_interval = 1000

    def __init__(self):
        #定时器
        self.timer = QTimer()
        self.timer.setInterval(self.init_interval)
        self.timer.start()

        #记下作为心跳操作目标的从机状态类
        self.target = None
        print('timer set')
        self.timer.timeout.connect(self.state_update)
        c.temp_freq_change.connect(self.freq_change)

    def state_update(self):
        print("current freq is:", self.current_interval)
        if self.target == None:
            return
        print("current freq is:",self.current_interval)
        #做状态更新
        #当前时间
        current_time=time.localtime(time.time())
        #转化为datetime格式
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',current_time)

        serverNo = self.target.roomNo

        current_temp = self.target.sysT
        c.Temp_Submit(current_temp,serverNo,current_temp)

    def freq_change(self,Temp_Submit_freq):
        if Temp_Submit_freq!=self.current_interval:
            self.current_interval = Temp_Submit_freq
            self.timer.setInterval(self.current_interval*1000)
            print("freq changed as %d"%(Temp_Submit_freq))

    def setServent(self,target):
        self.target = target

    def timerStop(self):
        self.timer.stop()