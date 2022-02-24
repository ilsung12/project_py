import os
import sys
import threading
import socket
from _thread import *
import PyQt5
from PyQt5.QtCore import *
#from Common import *
from encodings import utf_8

# his
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

g_ServerIP = '127.0.0.1'
g_ServerPort = 8801


class PassDataSR(QThread):
    def __init__(self, vServerIP, vServerPort, sec=0, parent=None):
        QThread.__init__(self)
        self.main = parent
        self.woking = True
        self.ServerIP = vServerIP
        self.ServerPort = vServerPort

        self.client_list = []

    def __del__(self):
        self.server_socket.close()
        self.server_connect = False

        if self.client_socket is not None:
            self.client_socket.close()

        self.wait()

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind((self.ServerIP, self.ServerPort))
            server_socket.listen()

            while self.woking:
                print('success0')
                client_socket, addr = server_socket.accept()
                print('success1')
                self.client_list.append(client_socket)
                print('success2')
                # Echo
                start_new_thread(threaded, (client_socket, addr, self))
                print('success3')


            for client in self.client_list:
                print('Disconnected by0')
                client.close()

def threaded(client_socket, addr, parent):
    main = parent

    while True:
        try:

            # 데이터가 수신되면 클라이언트에 다시 전송합니다.(에코)
            data = client_socket.recv(1024)
            print('::: Recive data ::: ', data)
            fname = data[17:57].decode('utf-8')
            print('::: Recive data 2 ::: ', fname)
            
            
            if not data:
                break

            data_str = ''
            for byte in data:
                data_str += str(hex(byte)) + ':'
            print('data_str', data_str)

        except ConnectionResetError as e:
            print('Disconnected by1')
            break

    print('Disconnected by2')
    main.client_list.remove(client_socket)
    client_socket.close()



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
        self.show()
        print('프로그램 시작')


    @pyqtSlot()
    def threadStart(self):
        #global g_connected
        print('서버 연결')
        self.th = PassDataSR(g_ServerIP, g_ServerPort, parent=self)
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