import socket
import threading
import time
import xml.dom.minidom as Dom
from struct import *
import sys
from models.main.UserRecord import UserRecord
from PyQt5.QtCore import pyqtSignal,QObject

class communicate(QObject):
    _newServent = pyqtSignal(int,str)
    _updateTemp = pyqtSignal(int,float)
    _quitServent = pyqtSignal(int)
    _stopRR = pyqtSignal()
    _newRequest = pyqtSignal(int,int,int)
    _algorithmActivate=pyqtSignal()
    Model = 1
    freq = 3

    def __init__(self):
        super().__init__()
        self.Freq = 2
        self.HOST, self.PORT = "localhost", 9999
        self.soc = socket.socket()
        self.soc.bind((self.HOST, self.PORT))
        self.soc.listen(10) #max number of clients listening to
        self.socket_list = []  # 包含tuple(conn,addr)
        self.room_dict = {}  # {room_no:(conn,addr)}
        self.socket_dict = {}  # {(conn,addr):room_no}
        self.log = UserRecord()
        self.log.log_sig.connect(self.Login_ACK)

    #------local setting functions
    def AC_Req(self,room_no,Positive,Wind_Level):
        self._newRequest.emit(int(room_no),int(Positive),int(Wind_Level))
        self._algorithmActivate.emit()

    def Temp_Submit(self,Time,Client_No,Temp):
        self._updateTemp.emit(int(Client_No),float(Temp))

    def Login(self,Name,Password,Client_No,conn,addr):
        if Client_No in self.room_dict.keys():
            print("重复登入")
            self.Login_ACK(conn,0,Name,Password)
        else:
            self.room_dict[Client_No] = (conn,addr)
            self.socket_dict[(conn, addr)] = Client_No
            print(Client_No,"in dict")
            res = self.log.Check(Client_No, Name, Password)



    #------info processing functions
    def parse(self,xml,conn,addr):
        root = Dom.parseString(xml).documentElement
        #print(root.nodeName)
        if(root.nodeName == "AC_Req"):
            node = root.getElementsByTagName("Positive")
            Positive = node[0].childNodes[0].data

            node = root.getElementsByTagName("Wind_Level")
            Wind_Level = node[0].childNodes[0].data
            room_no = self.socket_dict[(conn, addr)]
            self.AC_Req(room_no, Positive, Wind_Level)

        if(root.nodeName == "Temp_Submit"):
            node = root.getElementsByTagName("Time")
            Time = node[0].childNodes[0].data

            node = root.getElementsByTagName("Client_No")
            Client_No = node[0].childNodes[0].data
            node = root.getElementsByTagName("Temp")
            Temp = node[0].childNodes[0].data
            self.Temp_Submit(Time,Client_No,Temp)

        if(root.nodeName == "Login"):
            node = root.getElementsByTagName("Name")
            Name = node[0].childNodes[0].data

            node = root.getElementsByTagName("Password")
            Password = node[0].childNodes[0].data

            node = root.getElementsByTagName("Client_No")
            Client_No = node[0].childNodes[0].data

            self.Login(Name,Password,Client_No,conn,addr)

    def recv(self,data,conn,addr):
        print("process:",data)
        while(data):
            print("in recv")
            if (len(data) < 4):
                data = data + conn.recv(1024)
            xml_len = unpack('!i',data[0:4])[0]
            print("xml_len:", xml_len)
            data = data[4:]
            while (len(data) < xml_len):
                data = data + conn.recv(1024)
            xml = data[:xml_len]
            data = data[xml_len:]
            print("xml:", str(xml, "utf-8"))
            self.parse(str(xml, "utf-8"),conn,addr)
            print("data:", data)

    def connection_lost(self,no):
        try:
            soc = self.room_dict[no]
            del self.room_dict[no]
            del self.socket_dict[soc]
            self.socket_list.remove(soc)
            #self._stopRR.emit()
            self._quitServent.emit(int(no))
        except:
            print("connection to %d already closed." % (int(no)))
        pass

    def send(self,no,info):  # no can be a room number or a socket(before Login_ACK)
        if type(no) == int:
            no = str(no)

        if type(no) == str:  # no is a room number
            try:
                sock = self.room_dict[no][0]
                bytes_send = bytes(info, "utf-8")
                sock.sendall(len(bytes_send).to_bytes(4,'big') + bytes_send)
            except:
                self.connection_lost(no)
                print(no,"is not connected",sys.exc_info())
        else:  # no is a socket
            try:
                sock = no
                bytes_send = bytes(info, "utf-8")
                sock.sendall(len(bytes_send).to_bytes(4,'big') + bytes_send)
            except:
                print(no,"connection error")

    def broadcast(self,info):
        for (conn,addr) in self.socket_list:
            print("send:",info)
            try:
                conn.sendall(len(info).to_bytes(4,'big') + bytes(info, "utf-8"))
            except: #disconnected
                print("disconnected:",addr)
                self.socket_list.remove((conn,addr))

    #------message sending functions
    def Login_ACK(self,no,Succeed,Name,Password):
        print(no,Succeed,Name,Password)
        doc = Dom.Document()
        root = doc.createElement("Login_ACK")

        node_Succeed = doc.createElement("Succeed")
        node_Succeed.appendChild(doc.createTextNode(str(Succeed)))
        root.appendChild(node_Succeed)

        node_Name = doc.createElement("Name")
        node_Name.appendChild(doc.createTextNode(str(Name)))
        root.appendChild(node_Name)

        if Succeed == 1:#认证成功，创建从机类
            print("roomno emit",int(no),Name)
            self._newServent.emit(int(no),Name)

        node_Password = doc.createElement("Password")
        node_Password.appendChild(doc.createTextNode(str(Password)))
        root.appendChild(node_Password)

        node_Mode = doc.createElement("Mode")
        node_Mode.appendChild(doc.createTextNode(str(self.Model)))
        root.appendChild(node_Mode)

        self.send(no, root.toxml() + '\n')
        self.Temp_Submit_Freq(int(no),self.freq)
        if Succeed == 0:
            soc = self.room_dict[no]
            del self.room_dict[no]
            del self.socket_dict[soc]

    def Mode(self,no,Heater):
        doc = Dom.Document()
        root = doc.createElement("Mode")

        node_Heater = doc.createElement("Heater")
        node_Heater.appendChild(doc.createTextNode(str(Heater)))
        root.appendChild(node_Heater)

        self.send(no, root.toxml() + '\n')

    def Mode_B(self,Heater): #broadcast
        doc = Dom.Document()
        root = doc.createElement("Mode")

        node_Heater = doc.createElement("Heater")
        node_Heater.appendChild(doc.createTextNode(str(Heater)))
        root.appendChild(node_Heater)

        self.broadcast(root.toxml() + '\n')

    def Wind(self,no,Level,Start_Blowing):
        print("send wind %d %d"%(Level,Start_Blowing))
        doc = Dom.Document()
        root = doc.createElement("Wind")

        node_Level = doc.createElement("Level")
        node_Level.appendChild(doc.createTextNode(str(Level)))
        root.appendChild(node_Level)

        node_Blow = doc.createElement("Start_Blowing")
        node_Blow.appendChild(doc.createTextNode(str(Start_Blowing)))
        root.appendChild(node_Blow)

        self.send(no, root.toxml() + '\n')

    def Fare_Info(self,no,Fare,Energy):
        doc = Dom.Document()
        root = doc.createElement("Fare_Info")

        node_Fare = doc.createElement("Fare")
        node_Fare.appendChild(doc.createTextNode(str(Fare)))
        root.appendChild(node_Fare)

        node_Energy = doc.createElement("Energy")
        node_Energy.appendChild(doc.createTextNode(str(Energy)))
        root.appendChild(node_Energy)

        self.send(no, root.toxml() + '\n')

    def Temp_Submit_Freq(self,no,Temp_Submit_Freq):
        doc = Dom.Document()
        root = doc.createElement("Temp_Submit_Freq")

        node_Freq = doc.createElement("Temp_Submit_Freq")
        node_Freq.appendChild(doc.createTextNode(str(Temp_Submit_Freq)))
        root.appendChild(node_Freq)

        self.send(no, root.toxml() + '\n')

    def Temp_Submit_Freq_B(self,Temp_Submit_Freq): #broadcast
        doc = Dom.Document()
        root = doc.createElement("Temp_Submit_Freq")

        node_Freq = doc.createElement("Temp_Submit_Freq")
        node_Freq.appendChild(doc.createTextNode(str(Temp_Submit_Freq)))
        root.appendChild(node_Freq)

        self.broadcast(root.toxml() + '\n')

    def closeCon(self):
        for (soc,addr) in self.socket_list:
            soc.shutdown(socket.SHUT_RDWR)
            soc.close()
        self.soc.close()
        print("to close server")

class receiver_thread(threading.Thread):
    def __init__(self,conn,addr):
        threading.Thread.__init__(self)
        print("init receiver:",addr)
        self.conn = conn
        self.addr = addr
        global server

    def run(self):
        print("Listen start")
        connectAlive = True
        while (connectAlive):
            try:
                data = self.conn.recv(1024)
                print("data",data)
                server.recv(data,self.conn,self.addr)
            except:
                #print(sys.exc_info())
                connectAlive = False
                pass

class connector_thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        global server

    def run(self):
        print("Listen start")
        connectAlive = True
        while (connectAlive):
            try:
                conn, addr = server.soc.accept()
                conn.settimeout(10)
                print("connected:",conn,addr) #later this part should be moved to communicate.recv() when package is Login
                if (conn,addr) not in server.socket_list:
                    server.socket_list.append((conn,addr))
                    receiver_thread(conn,addr).start()
            except:
                connectAlive = False
                print("连接已断开")
            
server = communicate()
connector_thread().start()
print('通信类已建立Server')

if __name__ == "__main__":
    while(1):
        time.sleep(5)
        server.Temp_Submit_Freq(5)
        inp = input("press ENTER to send ACK")
        server.Login_ACK(103,1,"frank","123456789")
