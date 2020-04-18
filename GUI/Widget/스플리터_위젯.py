#=======================================================
# 스플리터 위젯
#=======================================================
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
from PyQt5.QtWidgets import QHBoxLayout, QFrame, QSplitter
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MyApp(QWidget):

    #================================
    # 초기화 동작 수행
    #================================
    def __init__(self):
        super().__init__()
        self.initUI()           # 기본 UI 초기화

    #=================================
    # 윈도우를 화면 가운데 위치 시키기
    #=================================
    def center(self):
        qr = self.frameGeometry()  # 창의 위치와 크기 정보를 가져
        cp = QDesktopWidget().availableGeometry().center()  # 사용하는 모니터 화면의 가운데 위치를 파악
        qr.moveCenter(cp)  # 창의 직사각형 위치를 화면의 중심의 위치로 이동합니다.
        self.move(qr.topLeft())

    # ================================
    # 화면 기본 설정
    # ================================
    def initUI(self):
        # 프레임 추가
        top = QFrame()
        top.setFrameShape(QFrame.Box)   # 프레임 형태

        midLeft = QFrame()
        midLeft.setFrameShape(QFrame.StyledPanel)

        midRight = QFrame()
        midRight.setFrameShape(QFrame.Panel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.WinPanel)
        bottom.setFrameShadow(QFrame.Raised)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(midLeft)
        splitter1.addWidget(midRight)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(top)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        # 레이아웃 설정
        hBox = QHBoxLayout()
        hBox.addWidget(splitter2)

        # 최상위에 레이아웃 설정
        self.setLayout(hBox)
        self.setWindowTitle("스플리터 위젯")           # 타이틀
        self.setWindowIcon(QIcon('../images/web.png'))  # 아이콘 추가
        self.resize(500, 350)                             # 크기 설정
        self.center()
        self.show()                                       # 보이기

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())