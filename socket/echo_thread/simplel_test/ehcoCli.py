import socket
def run_client(host='127.0.0.1', port=7788):
    with socket.socket() as sock:
        sock.connect((host, port))
        for _ in range(10):
            data = input(">>")
            sock.sendall(data.encode())
            if data == 'bye':
                sock.close()
                break
            res = sock.recv(1024)
            print(res.decode())
if __name__ == '__main__':
    run_client()

# 클라이언트 : 바인드나 리스닝의 과정이 필요없다는 것
# 필요 목록 : ip, host, buf_size
# 1. 소켓 열기
# 2. 소켓 연결(connect) : 
# 3. 데이터 보내기 : sock.sendall()
# 4. 데이터 받기 : sock.recv()
# 5. close