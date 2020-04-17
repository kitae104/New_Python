import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit,QTextEdit, QDesktopWidget, QGridLayout
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

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('Title:'), 0, 0)
        grid.addWidget(QLineEdit(), 0, 1)

        grid.addWidget(QLabel('Author:'), 1, 0)
        grid.addWidget(QLineEdit(), 1, 1)

        grid.addWidget(QLabel('Review:'), 2, 0)
        grid.addWidget(QTextEdit(), 2, 1)

        self.setWindowTitle("그리드 레이아웃")           # 타이틀
        self.setWindowIcon(QIcon('../images/web.png'))  # 아이콘 추가
        self.resize(300, 200)                             # 크기 설정
        self.center()
        self.show()                                       # 보이기

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())