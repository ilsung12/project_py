import imp
import socket
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import * 
from PyQt5 import QtCore
import time 
import sys
import os


HOST = '127.0.0.1'
PORT = 8081


# Main
class mainGUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

    
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
 
        # 쓰레드 인스턴스 생성
        self.th = transferSvr(self)
 
        # 쓰레드 이벤트 연결
        self.th.threadEvent.connect(self.threadEventHandler)
 
    @pyqtSlot()
    def threadStart(self):
        if not self.th.isRun:
            print('메인 : 쓰레드 시작')
            self.th.isRun = True
            self.th.start()
 
    @pyqtSlot()
    def threadStop(self):
        if self.th.isRun:
            print('메인 : 쓰레드 정지')
            self.th.isRun = False
 
    # 쓰레드 이벤트 핸들러
    # 장식자에 파라미터 자료형을 명시
    @pyqtSlot(int) # byte
    def threadEventHandler(self, n):
        print('메인 : threadEvent(self,' + str(n) + ')')
        

# Thread 돌리기
class transferSvr(QThread):                                                                             
    # 쓰레드의 커스텀 이벤트
    # 데이터 전달 시 형을 명시해야 함
    threadEvent = QtCore.pyqtSignal(int)
    
    def __init__(self, parent=None):
        super().__init__()
        self.n = 0
        self.main = parent
        self.isRun = False

    def run(self):
        while self.isRun:
            print('Thread : ' + str(self.n))
            self.threadEvent.emit(self.n)

            self.n += 1
            self.sleep(1)
                           

    # 파일 보내기
    def send():
        
        with open("C:/test/tiger.jpg", 'rb') as img_file:
            try:
                while True:
                    data = img_file.read(1024)
                    if data:
                        client_socket.send(data)
                    else:
                        break
                # ------------------------------------ #
                # 소켓 닫기
                client_socket.shutdown(socket.SHUT_WR)
                # ------------------------------------ #
            except Exception as e:
                print(e)

    # 답신
    def receive():
        message = client_socket.recv(1024)
        print(message.decode())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = mainGUI()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    transferSvr.send()
    transferSvr.receive()

    app.exec_()