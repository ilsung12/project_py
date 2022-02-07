import socket

HOST = "127.0.0.1"
PORT = 8081

def receive(receive_socket):
    with open("D:/testrecv/tiger.jpg", 'wb') as f:
        try:
            while True:
                data = receive_socket.recv(1024)
                if data:
                    f.write(data)
                else:
                    break
        except Exception as e:
            print(e)
        finally:
            f.close()


if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)

    while True:
        client_socket, addr = server_socket.accept()
        receive(client_socket)
        
        # socket.send("수신 완료".encode()) 
        client_socket.send("수신 완료".encode())