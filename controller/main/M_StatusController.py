# -*- coding: utf-8 -*-
from models.main.ControlPanel import ControlPanel

class StatusController:
    freq = 5  ########默认初始值，过后要改
    strat = 1  ######默认初始值，策略
    def __init__(self):
        self.new=ControlPanel()

    def changeFreq(self):
        self.new.setFreq(self.freq)

    def changeStrat(self):
        #print("set strat as %d"%(self.strat))
        self.new.setStrat(self.strat)

    def changeStatus(self,Model):
        self.new.setStatu(Model)

    def getConnec(self):
        list=self.new.getConnec()
        return list

    def getFreq(self):
        self.freq=self.new.getFreq()

    def getStrat(self):
        self.strat=self.new.getStrat()

    def getStatu(self):
        return self.new.getStatu()

