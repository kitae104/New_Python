import socket
import RPi.GPIO as GPIO
import time


class ServerSocket:

    def init(self):
        self.host = '192.168.0.18'
        self.port = 9999

    def gethost(self):
        host = self.host

        return host

    def getport(self):
        port = self.port

        return port

    def makehex(self, num1, num2):
        value1 = str(format(num1, '02x'))
        value2 = str(format(num2, '02x'))
        hex_value = value1 + value2

        return hex_value

serv = ServerSocket()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 소켓객체생성
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # WinError 10048 에러 해결

server_socket.bind((serv.gethost(), serv.getport()))
server_socket.listen()

client_socket, addr = server_socket.accept()
print('Connected by', addr)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

while True:
    data = client_socket.recv(2048)

    funccode = data[7]
    reg_addr = serv.makehex(data[8], data[9])
    reg_value = serv.makehex(data[10], data[11])

    print('Received from', data)
    print('funccode', funccode)
    print('reg_addr', reg_addr)
    print('reg_value', reg_value)

    if funccode == 1:
        pass

    elif funccode == 2:
        pass

    elif funccode == 3:
        pass

    elif funccode == 4:
        pass

    elif funccode == 6:
        if reg_addr == '0001':  #led
            if reg_value == '0001':  #on
                GPIO.output(17, True)
                continue

            elif reg_value == '0000':  #off
                GPIO.output(17, False)
                continue

GPIO.cleanup()