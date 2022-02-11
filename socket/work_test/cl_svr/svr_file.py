import socket
import select

# HOST = "127.0.0.1"
# PORT = 8081

# def receive(receive_socket):
#     for i in range(1, 8):
            

#         #with open("D:/testrecv/tiger"+ str(i) +".jpg", 'wb') as f:
#         with open("D:/testrecv/tiger1.jpg", 'wb') as f:
#             try:
#                 while True:
#                     data = receive_socket.recv(1024)
#                     if data:
#                         f.write(data)
#                     else:
#                         break
#             except Exception as e:
#                 print(e)
#             finally:
#                 f.close()


# if __name__ == '__main__':
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind((HOST, PORT))
#     server_socket.listen(10)

#     while True:
#         client_socket, addr = server_socket.accept()
#         receive(client_socket)
        
#         # socket.send("수신 완료".encode()) 
#         client_socket.send("수신 완료".encode())

# UDP_IP = "127.0.0.1"
# IN_PORT = 8081
# timeout = 3


# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.bind((UDP_IP, IN_PORT)) #서버

# while True:
#     data, addr = sock.recvfrom(1024)
#     if data:
#         print("File name:", data)
#         data=data.decode('utf-8')
#         #file_name = data.strip() + 'a'
#         file_name = 'D:/testrecv/n.jpg'

#     f = open(file_name, 'wb')

#     while True:
#         print('.')
#         ready = select.select([sock], [], [], timeout)
#         if ready[0]:
#             data, addr = sock.recvfrom(1024)
#             f.write(data)
#         else:
#             print("%s Finish!" % file_name)
#             f.close()
#             break
#     sock.close()

from socket import *
from os.path import exists
import sys

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('127.0.0.1', 8081))
serverSock.listen(1)

connectionSock, addr = serverSock.accept()

print(str(addr),'에서 접속했습니다')

filename = connectionSock.recv(1024) #클라이언트한테 파일이름(이진 바이트 스트림 형태)을 전달 받는다
print('받은 데이터 : ', filename.decode('utf-8')) #파일 이름을 일반 문자열로 변환한다
data_transferred = 0

if not exists(filename):
    print("no file")
    sys.exit()

print("파일 %s 전송 시작" %filename)
with open(filename, 'wb') as f:
    try:
        data = f.read(1024) #1024바이트 읽는다
        while data: #데이터가 없을 때까지
            data_transferred += connectionSock.send(data) #1024바이트 보내고 크기 저장
            data = f.read(1024) #1024바이트 읽음
    except Exception as ex:
        print(ex)
print("전송완료 %s, 전송량 %d" %(filename, data_transferred))