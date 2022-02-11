import imp
import socket
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import * 
from PyQt5 import QtCore
import time 
import sys
import os

g_connected = False
g_filePath = ''
g_fileName = ''
g_client_socket = ''

HOST = '127.0.0.1'
PORT = 8081



# Main
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

        # 쓰레드 인스턴스 생성
        self.th = SendData(self)
 
        # 쓰레드 이벤트 연결
        self.th.threadEvent.connect(self.threadEventHandler)
        print('쓰레드 연결')

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
            print('connectedSvr 2')
            if g_connected == False:
                print('connectedSvr 3')
                g_filePath = "C:/test/"
                g_fileName = "tiger1.jpg"
                mFileName = g_filePath + g_fileName

                g_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                net_fileName = mFileName.encode()
                g_client_socket.sendto(net_fileName, (HOST, PORT))
                print('Sending {}...'.format(mFileName))
                # g_client_socket.connect((HOST, PORT))

                print('서버에 연결 되었습니다.')
                g_connected = True
            else:
                print('서버에 연결할 수 없습니다.')
                g_connected = False

        except Exception as ex:
            print('Error Contents : ', ex)
            g_connected = False

 
    @pyqtSlot()
    def threadStart(self):
        if not self.th.isRun:
            print('MainUI : 쓰레드 시작')
            self.th.isRun = True
            self.th.start()
            
 
    @pyqtSlot()
    def threadStop(self):
        if self.th.isRun:
            print('MainUI : 쓰레드 정지')
            self.th.isRun = False
        
 
    # 쓰레드 이벤트 핸들러
    # 장식자에 파라미터 자료형을 명시
    @pyqtSlot(str) # byte
    def threadEventHandler(self):
        print('threadEventHandler')
        

# Thread 돌리기
class SendData(QThread):                                                                             
    # 쓰레드의 커스텀 이벤트
    # 데이터 전달 시 형을 명시해야 함    
    threadEvent = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        QThread.__init__(self)
        self.main = parent
        self.isRun = False
        
    
    # def __del__(self):
    #     self.wait()

    def run(self):
        global g_connected
        global g_client_socket
        global g_filePath
        global g_fileName
        
        print('4')
        print('isRun = ',self.isRun)
        if self.isRun:
            g_connected =True
            print('g_connected = ', g_connected)
            while g_connected:
                try:
                    f = open(g_filePath + g_fileName, 'rb')
                    print(f)
                    data = f.read(1024)
                    while data:
                        if g_client_socket.sendto(data, (HOST, PORT)):
                            data = f.read(1024)
                            time.sleep(1)
                    
                    g_client_socket.close()
                    f.close()


                except Exception as ex:
                    print('error', ex)
                    sys.exit()
                    

            #self.threadEvent.emit(self.n)

                           

    # 파일 보내기
    # def send(self):
    #     global g_filePath
    #     global g_fileName
    #     global g_client_socket
    #     print('send ->', g_filePath+g_fileName)
    #     #with open("C:/test/tiger.jpg", 'rb') as img_file:
        
    #     if os.path.isfile(g_filePath):
    #         #with open(g_filePath + g_fileName, 'rb') as img_file:
    #         with open('C:test/tiger1.jpg', 'rb') as img_file:
            
    #             try:
    #                 while True:
    #                     data = img_file.read(1024)
                        
    #                     if data:
    #                         g_client_socket.send(data)
    #                         print('clientsocket', g_client_socket.send(data))
    #                     else:
    #                         print('파일이 없습니다.')
    #                 # ------------------------------------ #
    #                 # 소켓 닫기
    #                     g_client_socket.shutdown(socket.SHUT_WR)
    #                 # ------------------------------------ #
    #             except Exception as e:
    #                 print(e)

    # # 답신
    # def receive():
    #     message = mainGUI.connectedSvr.client_socket.recv(1024)
    #     print(message.decode())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = mainGUI()

    
    # transferImg.send()
    # transferImg.receive()

    app.exec_()