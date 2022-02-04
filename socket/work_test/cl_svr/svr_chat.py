from asyncio import transports
from twisted.internet import protocol, reactor
import names

COLORS = [
    '\033[31m', # RED
    '\033[32m', # GREEN
    '\033[33m', # YELLOW
    '\033[34m', # BLUE
    '\033[35m', # MAGENTA
    '\033[36m', # CYAN
    '\033[37m', # WHITE
    '\033[4m', # UNDERLINE
]


transports = set()
users = set()

class Chat(protocol.Protocol):
    def connectionMade(self):
        print('Client Connnected !')
        
        name = names.get_first_name()
        color = COLORS[len(users) % len(COLORS)]
        users.add(name)
        transports.add(self.transport)
        

        self.transport.write(f'{color}{name}\033[0m'.encode())
        # \003[0m 은 컬러를 리셋하는 코드 

    def dataReceived(self, data): # 사용자가 서버에 메시지를 보내면 실행
        # 모든 클라이언트를 하나씩 돌면서(for 루프) :
        # 만약 내가 보낸 메세지가 아니라면 :
        # 메세지를 전달한다.
        for t in transports:
            if self.transport is not t:
                t.write(data)
                
        print(data.decode('utf-8'))


class ChatFactory(protocol.Factory): # 통신 프로토콜 정의
    def buildProtocol(self, addr):
        return Chat()

print('Server Started !')

reactor.listenTCP(8000, ChatFactory())
reactor.run()