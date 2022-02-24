import socket
import signal
import sys
import threading
import time


# Ctrl+C 로 프로그램을 종료한다.
def signal_handler(signal, frame):
    print( 'signal_handler called' )
    sys.exit(0)

# echo 서버의 클라이언트 연동 쓰레드 함수
def ClientFunc(conn):
    while True:
        data = conn.recv( 8192 )
        if( len(data) == 0 ):
            print( 'client is closed' )
            break
        print( data )
        conn.sendall( data )

# TCP accept 쓰레드
def ServerFunc(server):
    while True:
        conn, addr = server.accept()
    
        print( addr, 'client is connected' )
    
        p = threading.Thread( target=ClientFunc, args=(conn,))
        p.daemon = True
        p.start()

# Ctrl+C 이벤트 핸들러를 등록한다.

signal.signal( signal.SIGINT, signal_handler )


# TCP 서버를 시작한다.

server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
server.bind( ('localhost', 8000) )
server.listen(5)


# TCP accept 쓰레드를 시작한다.

p = threading.Thread( target=ServerFunc, args=(server,))
p.daemon = True
p.start()

while True:
    time.sleep(10)
    server.close() 
                                                                                                               

# import socket

# client = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
# client.connect( ('localhost', 8000) )

# client.sendall( b'1234' )
# data = client.recv( 8192 )

# print( data )

# client.close()



