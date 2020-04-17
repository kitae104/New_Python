import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.vbox = QVBoxLayout()   # 레이아웃 설정(수직 배치)
        self.initUI()               # 기본 UI 초기화

    #=================================
    # 윈도우를 화면 가운데 위치 시키기
    # =================================
    def center(self):
        qr = self.frameGeometry()  # 창의 위치와 크기 정보를 가져
        cp = QDesktopWidget().availableGeometry().center()  # 사용하는 모니터 화면의 가운데 위치를 파악
        qr.moveCenter(cp)  # 창의 직사각형 위치를 화면의 중심의 위치로 이동합니다.
        self.move(qr.topLeft())

    def test(self):
        lbl_red = QLabel('Red')
        lbl_red.setStyleSheet("color: red;"
                              "border-style: solid;"
                              "border-width: 2px;"
                              "border-color: #FA8072;"
                              "border-radius: 3px")

        lbl_green = QLabel('Green')
        lbl_green.setStyleSheet("color: green;"
                                "background-color: #7FFFD4")
        lbl_blue = QLabel('Blue')
        lbl_blue.setStyleSheet("color: blue;"
                               "background-color: #87CEFA;"
                               "border-style: dashed;"
                               "border-width: 3px;"
                               "border-color: #1E90FF")

        self.vbox.addWidget(lbl_red)
        self.vbox.addWidget(lbl_green)
        self.vbox.addWidget(lbl_blue)

    def initUI(self):

        self.test();
        self.setLayout(self.vbox)

        self.setWindowTitle("스타일 꾸미기")           # 타이틀
        self.setWindowIcon(QIcon('../images/web.png'))  # 아이콘 추가
        self.resize(500, 350)  # 크기와 위치 설정
        self.center()
        self.show()                                       # 보이기



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())