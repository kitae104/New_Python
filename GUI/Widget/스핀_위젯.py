#=======================================================
# 스핀 위젯
#=======================================================
import sys

from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QVBoxLayout, QLabel, QSpinBox, QDoubleSpinBox
from PyQt5.QtGui import QIcon


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

        # 스핀 박스
        self.lbl1 = QLabel('QSpinBox')
        self.spinbox = QSpinBox()
        self.spinbox.setMinimum(-10)
        self.spinbox.setMaximum(30)
        # self.spinbox.setRange(-10, 30)
        self.spinbox.setSingleStep(2)
        self.lbl2 = QLabel('0')

        self.spinbox.valueChanged.connect(self.valueUpDown)

        # 더블 스핀 박스
        self.lblDS1 = QLabel('QDoubleSpinBox')
        self.dspinbox = QDoubleSpinBox()
        self.dspinbox.setRange(0, 100)
        self.dspinbox.setSingleStep(2.5)
        self.dspinbox.setPrefix('$ ')
        self.dspinbox.setDecimals(1)
        self.lblDS2 = QLabel('0.0')

        self.dspinbox.valueChanged.connect(self.dValueUpDown)

        # 레이아웃 설정
        vBox = QVBoxLayout()
        vBox.addWidget(self.lbl1)
        vBox.addWidget(self.spinbox)
        vBox.addWidget(self.lbl2)
        vBox.addStretch(1)
        vBox.addWidget(self.lblDS1)
        vBox.addWidget(self.dspinbox)
        vBox.addWidget(self.lblDS2)
        vBox.addStretch(2)

        self.setLayout(vBox)

        self.setWindowTitle("스핀 위젯")           # 타이틀
        self.setWindowIcon(QIcon('../../Utils/Images/web.png'))  # 아이콘 추가
        self.resize(500, 350)                             # 크기 설정
        self.center()
        self.show()                                       # 보이기

    def valueUpDown(self):
        self.lbl2.setText(str(self.spinbox.value()))

    def dValueUpDown(self):
        self.lblDS2.setText(str(self.dspinbox.value()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())