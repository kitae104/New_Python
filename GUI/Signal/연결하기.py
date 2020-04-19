#=======================================================
# 시그널과 슬롯 연결하기
# PyQt에서 이벤트(시그널) 처리를 할 때 사용되는 함수를 이벤트 핸들러 (슬롯)라고 한다.
#=======================================================
import sys

from PyQt5.QtCore import Qt, QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QVBoxLayout, QLCDNumber, QDial, QPushButton, \
    QHBoxLayout, QLabel
from PyQt5.QtGui import QIcon


class Communicate(QObject):
    closeApp = pyqtSignal()

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

        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        # 마우스 위치 확인 라벨
        x = 0
        y = 0

        self.text = '마우스의 위치 : x = {0}, y = {1}'.format(x, y)
        self.lbl = QLabel(self.text, self)

        # 마우스 위치 추적
        self.setMouseTracking(True)

        # LCD 패널과 다이얼
        lcd = QLCDNumber(self)
        dial = QDial(self)

        # valueChaged 시그널(이벤트) 발생 --> display 슬롯에 연결
        dial.valueChanged.connect(lcd.display)

        btn1 = QPushButton('Big', self)
        btn2 = QPushButton('Small', self)

        # 버튼 클릭 시 이를 처리하는 슬롯(이벤트 핸들러 함수) 호출
        btn1.clicked.connect(self.resizeBig)
        btn2.clicked.connect(self.resizeSmall)

        # 레이아웃 설정
        hBox = QHBoxLayout()
        hBox.addWidget(btn1)
        hBox.addWidget(btn2)

        vBox = QVBoxLayout()
        vBox.addWidget(self.lbl)     # 일반 위젯은 addWidget으로 추가
        vBox.addWidget(lcd)
        vBox.addWidget(dial)
        vBox.addLayout(hBox)    # 레이아웃은 addLayout으로 추가

        self.setLayout(vBox)

        self.setWindowTitle("시그널 연결하기")           # 타이틀
        self.setWindowIcon(QIcon('../../Utils/images/web.png'))  # 아이콘 추가
        self.resize(200, 250)                             # 크기 설정
        self.center()
        self.show()                                       # 보이기

    def resizeBig(self):
        self.resize(400, 500)

    def resizeSmall(self):
        self.resize(200, 250)

    # 기존에 존재하는 이벤트 핸들러 수정해서 사용하기
    # keyPressEvent 이벤트 핸들러는 키보드의 이벤트를 입력으로 사용
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_B:
            self.resizeBig()
        elif event.key() == Qt.Key_S:
            self.resizeSmall()

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()

        self.text = '마우스의 위치 : x = {0}, y = {1}'.format(x, y)
        self.lbl.setText(self.text)
        self.lbl.adjustSize()

    def mousePressEvent(self, e):
        self.c.closeApp.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())