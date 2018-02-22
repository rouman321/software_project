# -*- coding: utf-8 -*-

from  datetime  import  *
from S_DBFacade import db_lock,cursor,db
myroom = object

class S_servent :
    def __init__(self,R,U,P,M):
        self.roomNo = R  #这个地方的默认数据记得修改呀！！！！
        self.targetT = 28.0
        self.targetW = 3
        self.sysT = 20.0
        self.sysW = 2
        self.sysModel = M

        #根据系统工作模式调整室温初态
        if self.sysModel == 1: #冬季，制热
            self.targetT = 28.0
            self.sysT = 22.0
        else:
            self.targetT = 22.0
            self.sysT = 28.0
        self.loggedOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.eng_cost = 0.00
        self.money_cost = 0.00
        self.start_blowing = 0

        self.usr = U
        self.pwd = P
        self.insert_deal(self.roomNo, self.loggedOn, self.usr, self.pwd, self.targetT, self.targetW, self.sysT, self.sysW, self.sysModel, self.eng_cost, self.money_cost, self.start_blowing)
        print("out")

    #更新修改当前的系统信息
    def update_sys(self,T,W,M):
        self.targetT = T
        self.targetW = W
        self.sysModel = M
        self.updatesys_deal(self.roomNo, self.loggedOn, T, W, M)               #数据库同步修改

    def update_cost(self,MC,EC):
        self.eng_cost = EC
        self.money_cost = MC
        self.updatecost_deal(self.roomNo, self.loggedOn, EC, MC)                #数据库同步修改

    def update_rt(self,sT): #实时温度心跳包
        print("更新实时温度-数据类")
        self.sysT=sT
        self.updatert_deal(self.roomNo, self.loggedOn, sT)

    def update_rw(self,sW,sb):
        self.sysW=sW
        self.start_blowing=sb
        self.updaterw_deal(self.roomNo, self.loggedOn, sW,sb)

    def ret_current_state(self):
        return self.roomNo, self.targetT, self.targetW, self.sysT, self.sysW, self.sysModel, self.loggedOn, self.eng_cost, self.money_cost, self.start_blowing
        #这个地方返回的东西还要再修改一下

    def insert_dbinfo(self):
        self.insert_deal()

    def insert_deal(self,roomNo, loggedOn, usr, pwd, targetT, targetW, sysT, sysW, sysModel, eng_cost, money_cost, start_blowing):
        sql = "insert into clientinfo values (%d, '%s', '%s', '%s', %f, %d, %f, %d, %d, %f, %f, %d)" % \
              (roomNo, loggedOn, usr, pwd, targetT, targetW, sysT, sysW, sysModel, eng_cost, money_cost,start_blowing)
        db_lock.acquire()
        cursor.execute(sql)
        db.commit()
        db_lock.release()

    def updatecost_deal(self, roomNo, loggedOn, EC, MC):
        print("账单-更改数据库")
        sql = "update clientinfo set eng_cost = %f, money_cost = %f where roomNo = %d and loggedOn = '%s'" % (
         EC,MC,roomNo, loggedOn)
        db_lock.acquire()
        row=cursor.execute(sql)
        db.commit()
        db_lock.release()
        print("修改完毕")

    def updatesys_deal(self,roomNo, loggedOn, T, W, M):
        print("设置-更改数据库")
        sql = "update clientinfo set targetT = %f, targetW = %d, sysModel = %d where roomNo = %d and loggedOn = '%s'" % (
            T, W, M, roomNo, loggedOn)
        db_lock.acquire()
        cursor.execute(sql)
        db.commit()
        db_lock.release()
        print("设置-更改数据库完成")

    def updatert_deal(self, roomNo , loggedOn , T):
        print("温度-修改数据库")
        sql = "update clientinfo set sysT=%f where roomNo = %d and loggedOn = '%s'" % (T, roomNo, loggedOn)
        db_lock.acquire()
        cursor.execute(sql)
        db.commit()
        db_lock.release()

    def updaterw_deal(self,roomNo, loggedOn, W, sb):
        sql = "update clientinfo set sysW=%d, start_blowing=%d where roomNo = %d and loggedOn = '%s'" % (W, sb, roomNo, loggedOn)
        print(sql)
        db_lock.acquire()
        cursor.execute(sql)
        db.commit()
        db_lock.release()

