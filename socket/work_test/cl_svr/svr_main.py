import socket
from _thread import *

client_sockets = [] # 서버에 접속한 클라이언트 목록

# 쓰레드에서 실행되는 코드입니다.
# 접속한 클라이언트마다 새로운 쓰레드가 생성되어 통신을 하게 됩니다.
def threaded(client_socket, addr):
    # addr[0] : ip Address, addr[1] : client ID
    print('>> Connected by :', addr[0], ':', addr[1])
    
    # 클라이언트가 접속을 끊을 때 까지 반복합니다.
    while True:

        try:

            # 데이터가 수신되면 클라이언트에 다시 전송합니다.(에코)
            # 클라이언트가 보낸 메시지를 수신하기 위해 대기합니다. 
            data = client_socket.recv(4096)

            if not data:
                print('>> Disconnected by ' + addr[0], ':', addr[1])
                break

            print('>> Received from ' + addr[0], ':', addr[1], data.decode())

            # 서버에 접속한 클라이언트들에게 채팅 보내기
            # 메세지를 보낸 본인을 제외한 서버에 접속한 클라이언트에게 메세지 보내기
            for client in client_sockets :
                if client != client_socket :
                    client.send(data)

        except ConnectionResetError as e:
            print('>> Disconnected by ' + addr[0], ':', addr[1])
            break

    if client_socket in client_sockets :
        client_sockets.remove(client_socket)
        print('remove client list : ',len(client_sockets))

    client_socket.close()


# 서버 IP 및 열어줄 포트
HOST = '172.16.53.123'
PORT = 9080

# 서버 소켓 생성
print('>> Server Start')
# 소켓 객체를 생성합니다. 
# 주소 체계(address family)로 IPv4, 소켓 타입으로 TCP 사용합니다. 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 포트 사용중이라 연결할 수 없다는 
# WinError 10048 에러 해결를 위해 필요합니다. 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind 함수는 소켓을 특정 네트워크 인터페이스와 포트 번호에 연결하는데 사용됩니다.
server_socket.bind((HOST, PORT))
# 서버가 클라이언트의 접속을 허용하도록 합니다.
server_socket.listen()

# 클라이언트가 접속하면 accept 함수에서 새로운 소켓을 리턴합니다.

# 새로운 쓰레드에서 해당 소켓을 사용하여 통신을 하게 됩니다.

try:
    while True:
        print('>> Wait')
        # accept 함수에서 대기하다가 클라이언트가 접속하면 새로운 소켓을 리턴합니다. 
        client_socket, addr = server_socket.accept()
        client_sockets.append(client_socket)
        start_new_thread(threaded, (client_socket, addr))
        print("Connected Users : ", len(client_sockets))
except Exception as e :
    print ('err : ',e)

finally:
    server_socket.close()

