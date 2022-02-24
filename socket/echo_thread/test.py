from encodings import utf_8
import os
from sqlite3 import connect
import sys
import threading
import socket
import time

import PyQt5
from PyQt5.QtCore import *

# his
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

g_ServerIP = '127.0.0.1'
g_ServerPort = 8801
#g_ClientPort = 55733

class PassDataSR(QThread):
    def __init__(self, vServerIP, vServerPort, sec=0, parent=None):
        QThread.__init__(self)
        self.main = parent
        self.isRun = True
        self.isSock = False
        print('>>>>',vServerIP,':',vServerPort)
        self.ServerIP = vServerIP
        self.ServerPort = vServerPort

        self.server_socket = None
        self.server_connect = False

        self.client_socket = None

    def __del__(self):
        self.server_socket.close()
        self.server_connect = False

        if self.client_socket is not None:
            self.client_socket.close()

        self.wait()


    def run(self):
        #if self.isSock:
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.ServerIP, self.ServerPort))
        self.server_socket.listen()

        #print('self.server_socket.accept()==>',self.server_socket.accept())
        self.client_socket, self.client_address = self.server_socket.accept()
        print('self.client_socket ==>', self.client_socket)
        print('self.client_address ==>', self.client_address)

        self.server_connect = True
        print('server_connected', self.server_connect)
                   
                   
        while self.server_connect: 
            data = self.client_socket.recv(1024)
            
            if len(data) > 0:
                print('::: Recive data ::: ', data)
                fname = data[17:57].decode('utf-8')
                print('::: Recive data 2 ::: ', fname)
                self.isSock = False
            
        # self.client_socket.close
        # time.sleep(1) 

        #return self.run()




# his
class mainGUI(QDialog):
    global g_ServerPort
    global g_ServerIP

    def __init__(self, parent=None):
        super().__init__(parent)
        global g_connected
    
        # GUI 컨트롤 생성 및 배치
        self.btn1 = QPushButton("쓰레드 시작", self)
        self.btn2 = QPushButton("쓰레드 정지", self)
 
        vertBox = QVBoxLayout()
        vertBox.addWidget(self.btn1)
        vertBox.addWidget(self.btn2)
        self.setLayout(vertBox)
        self.setGeometry(700, 500, 300, 100)
 
        self.btn1.clicked.connect(self.threadStart)
        self.btn2.clicked.connect(self.threadStop)
        
        # 쓰레드 인스턴스 생성
        
 
        # 쓰레드 이벤트 연결
        # self.th.connect(self.threadEventHandler)
        # print('쓰레드 연결')

        self.show()
        print('프로그램 시작')


    @pyqtSlot()
    def threadStart(self):
        global g_connected
        print('서버 연결')
        self.th = PassDataSR(g_ServerIP, g_ServerPort, parent=self)
        self.th.isSock = True
        self.th.start()
            
 
    @pyqtSlot()
    def threadStop(self):
        if self.th.isRun:
            print('MainUI : 쓰레드 정지')
            self.th.isRun = False
 

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    form = mainGUI()
        
    app.exec_()