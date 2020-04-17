import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QDesktopWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()           # 기본 UI 초기화

    # =================================
    # 윈도우를 화면 가운데 위치 시키기
    # =================================
    def center(self):
        qr = self.frameGeometry()  # 창의 위치와 크기 정보를 가져
        cp = QDesktopWidget().availableGeometry().center()  # 사용하는 모니터 화면의 가운데 위치를 파악
        qr.moveCenter(cp)  # 창의 직사각형 위치를 화면의 중심의 위치로 이동합니다.
        self.move(qr.topLeft())

    def initUI(self):

        label1 = QLabel('Label1', self)
        label1.move(20, 20)                             # 절대적인 위치에 배치
        label2 = QLabel('Label2', self)
        label2.move(20, 60)                             # 절대적인 위치에 배치

        btn1 = QPushButton('Button1', self)
        btn1.move(80, 13)
        btn2 = QPushButton('Button2', self)
        btn2.move(80, 53)

        self.setWindowTitle("내 어플리케이션")           # 타이틀
        self.setWindowIcon(QIcon('../images/web.png'))  # 아이콘 추가
        self.resize(500, 350)                             # 크기 설정
        self.center()
        self.show()                                       # 보이기

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())