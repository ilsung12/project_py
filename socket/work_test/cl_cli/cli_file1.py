from cProfile import run
from cgitb import Hook
import socket
import os
import sys
from time import sleep

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

HOST = '127.0.0.1'
PORT = 8081

g_connected = False
g_filePath = "C:/test/"
g_fileName = "tiger1.jpg"
g_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class mainGUI(QDialog):
    global HOST
    global PORT

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
        
 
        print('서버 연결')
        
        self.connectedSvr()

        timer = QtCore.QTimer(self)
        timer.setInterval(3000)
        timer.timeout.connect(self.reConnectedSvr)
        timer.start()

        print("서버 연결 재시작 타이머")

        # 쓰레드 인스턴스 생성
        self.th = sendSvr(self)
        
 
        # 쓰레드 이벤트 연결
        # self.th.connect(self.threadEventHandler)
        # print('쓰레드 연결')

        self.show()
        print('프로그램 시작')


    # 서버에 소켓 연결
    def connectedSvr(self):
        global g_connected
        global g_client_socket
        global g_fileName
        global g_filePath
        print('connectedSvr 1')
        try:
            if g_connected == False:
                g_client_socket.connect((HOST, PORT))
                print('서버에 연결 되었습니다.')
                g_connected = True
            else:
                print('서버에 연결할 수 없습니다.')
                g_connected = False

        except Exception as ex:
            print('Error connectedSvr : ', ex)
            

    def reConnectedSvr(self):
        global g_connected
        global g_client_socket
        global g_fileName
        global g_filePath

        print('RE:connectedSvr ')
        try:
            # 연결이 False 면,
            if g_connected == False:
                print('reconnected =====> run1')

                # 연결을 시작하자
                if g_client_socket.connect((HOST, PORT)) == None:
                    print('연결요청중입니다.')
                    g_client_socket.connect((HOST, PORT))
                    print('서버에 연결 되었습니다.')
                    g_connected = True


        except Exception as ex:
            print('Error reConnectedSvr : ', ex)
 
    @pyqtSlot()
    def threadStart(self):
        global g_connected

        if not self.th.isRun:
            print('MainUI : 쓰레드 시작')
            print('g_connected==', g_connected)
            self.th.isRun = True
            self.th.start()
            
 
    @pyqtSlot()
    def threadStop(self):
        if self.th.isRun:
            print('MainUI : 쓰레드 정지')
            self.th.isRun = False
            


class sendSvr(QThread):
    def __init__(self, sec=0, parent=None):
        QThread.__init__(self)
        print('g_connected==', g_connected)
        self.main = parent
        self.isRun = False
        
    
    def run(self):
        global g_connected
        global g_client_socket
        global HOST
        global PORT


        cnt = 0
        try:
            while self.isRun:
            
                cnt += 1

                print(cnt)
                self.send()
                self.receive()
        except Exception as ex:
            print('TH Error', ex)
                

    def send(self):
        # for i in range(1, 5):
        #     saveCnt = i
        global g_connected
        global g_fileName
        global g_filePath

        # 보내는 파일
        
        with open(g_filePath + g_fileName, 'rb') as f:
            try:
                while True:
                    data = f.read(1024)
                    print('쓰레드 동작중')
                    if data:
                        g_client_socket.sendall(data)
                        #sleep(1)
                        #g_client_socket.shutdown(socket.SHUT_WR)
                    else:
                        break
                # ------------------------------------ #
                g_client_socket.shutdown(socket.SHUT_WR)
                g_connected = False
                g_client_socket.close()
                print('소켓연결을 종료했습니다.')                  
                #sleep(1)
                # ------------------------------------ #
            except Exception as e:
                print(e)
            


    def receive(self):
        global g_client_socket
            # 성공 -> '수신 완료 
        message = g_client_socket.recv(1024)
        print(message.decode())


if __name__ == '__main__':
    # g_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # g_client_socket.connect((HOST, PORT))
    # print(type(client_socket))
    
    app = QApplication(sys.argv)
    form = mainGUI()


    # if os.path.exists(g_filePath):
    #     sendSvr.send()
    #     sendSvr.receive()
    
    
    app.exec_()