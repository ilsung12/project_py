from select import select
import socket
import select
import sys
import msvcrt

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8000))

name = None

while True:
    # No Win Version
    # read, write, fail = select.select((s,sys.stdin),(),())
    # ... for desc in read: ...

    # Win Error resolved
    read, write, fail = select.select((s,),(),(), 1)

    if msvcrt.kbhit(): read.append(sys.stdin)

    for desc in read:
        if desc == s: # 서버에서 온 메세지라면 메세지 출력
            data = s.recv(4096)
            print(data.decode())

            if name is None:
                name = data.decode()
                s.send(f'{name} is connected!'.encode())

        else: # 만약 사용자가 입력한거라면 사용자가 입력한 문자열을 읽어서 서버에 전송
            msg = desc.readline()
            msg = msg.replace('\n', '')
            s.send(f'{name}: {msg}'.encode())
