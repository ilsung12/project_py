from datetime import datetime
from fileinput import filename
from genericpath import isfile
from datetime import datetime
import socket
import os
from time import sleep


HOST = "172.16.53.123"

#HOST = "127.0.0.1"
PORT = 8081

# 수신 : 파일명에 실시간을 적음으로서 같은 파일이 아니게 됨
#       혹여나 같은 시간에 동작했다면 copy라는 이름을 가짐. 아? sleep을 줄까?
def receive(receive_socket):    
        # 받은 파일
    now = datetime.now()    
    cur_time = now.strftime("%Y%m%d_%H%M%S")
    filePath = 'D:/testrecv/'
    fileName = 'tiger' + str(cur_time)

    # if os.path.exists("D:/testrecv/"+ fileName + ".jpg") :
    #     with open("D:/testrecv/"+ fileName + "_copy.jpg", 'wb') as f1:
    #         try:
    #             while True:
    #                 data = receive_socket.recv(1024)
    #                 if data:
    #                     f1.write(data)
    #                     print(cur_time)
    #                     print('11111')
    #                 else:
    #                     break
    #         except Exception as e:
    #             print(e)
    #         finally:
    #             f1.close()
    # else:
    with open(filePath + fileName + ".jpg", 'wb') as f:
        try:
            while True:
                data = receive_socket.recv(1024)
                if data:
                    f.write(data)
                    print('22222')
                else:
                    break
        except Exception as e:
            print(e)
        finally:
            f.close()
            sleep(1)

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)

    while True:
        client_socket, addr = server_socket.accept()
        receive(client_socket)

        client_socket.send("수신 완료".encode())

        