import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QDesktopWidget, QHBoxLayout, QVBoxLayout
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

        okBtn = QPushButton('OK')
        cancelBtn = QPushButton('Cancel')

        hbox = QHBoxLayout()                            # 수평 레이아웃
        hbox.addStretch(1)                              # stretch factor : 1
        hbox.addWidget(okBtn)
        hbox.addWidget(cancelBtn)
        hbox.addStretch(1)                              # 1

        vbox = QVBoxLayout()                            # 수직 레이아웃
        vbox.addStretch(3)                              # 3 : 1 비율 유지
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle("내 어플리케이션")           # 타이틀
        self.setWindowIcon(QIcon('../images/web.png'))  # 아이콘 추가
        self.resize(500, 350)                             # 크기 설정
        self.center()
        self.show()                                       # 보이기

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())