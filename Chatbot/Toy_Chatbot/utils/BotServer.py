# 챗봇 서버
import socket

class BotServer:
    # 생성자(서버 포트, 수락할 클라이언트 수)
    def __init__(self, srv_port, listen_num):
        self.port = srv_port
        self.listen = listen_num
        self.mySock = None

    # sock 생성
    def create_sock(self):
        self.mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mySock.bind(("0.0.0.0", int(self.port)))
        self.mySock.listen(int(self.listen))
        return self.mySock

    # client 대기
    def read_for_client(self):
        return self.mySock.accept()     # 소캣 객체 반환 (conn, address 반환)

    # sock 반환
    def get_sock(self):
        return self.mySock

