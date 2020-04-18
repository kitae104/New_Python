#=======================================================
# 그룹박스 위젯
#=======================================================
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QGridLayout, QRadioButton, QCheckBox, QPushButton, \
    QMenu
from PyQt5.QtWidgets import QVBoxLayout, QGroupBox
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

        grid = QGridLayout()
        grid.addWidget(self.createFirstGroup(), 0, 0)
        grid.addWidget(self.createSecondGroup(), 1, 0)
        grid.addWidget(self.createNonGroup(), 0, 1)
        grid.addWidget(self.createPushButtonGroup(), 1, 1)

        # 최상위에 레이아웃 설정
        self.setLayout(grid)
        self.setWindowTitle("그룹박스 위젯")           # 타이틀
        self.setWindowIcon(QIcon('../images/web.png'))  # 아이콘 추가
        self.resize(500, 350)                             # 크기 설정
        self.center()
        self.show()                                       # 보이기

    def createFirstGroup(self):
        groupBox = QGroupBox("라디오 버튼 그룹")

        radio1 = QRadioButton('Radio1')
        radio2 = QRadioButton('Radio2')
        radio3 = QRadioButton('Radio3')
        radio1.setChecked(True)

        vBox = QVBoxLayout()
        vBox.addWidget(radio1)
        vBox.addWidget(radio2)
        vBox.addWidget(radio3)
        groupBox.setLayout(vBox)

        return groupBox

    def createSecondGroup(self):
        groupBox = QGroupBox("라디오 버튼 그룹2")
        groupBox.setCheckable(True)
        groupBox.setChecked(False)

        radio1 = QRadioButton('Radio1')
        radio2 = QRadioButton('Radio2')
        radio3 = QRadioButton('Radio3')
        radio1.setChecked(True)
        checkBox = QCheckBox('독립적인 체크박스')
        checkBox.setChecked(True)

        vBox = QVBoxLayout()
        vBox.addWidget(radio1)
        vBox.addWidget(radio2)
        vBox.addWidget(radio3)
        vBox.addWidget(checkBox)
        vBox.addStretch(1)              # 공간 확보
        groupBox.setLayout(vBox)

        return groupBox

    def createNonGroup(self):
        groupBox = QGroupBox('체크박스 그룹')
        groupBox.setFlat(True)

        checkbox1 = QCheckBox('Checkbox1')
        checkbox2 = QCheckBox('Checkbox2')
        checkbox2.setChecked(True)
        checkbox3 = QCheckBox('Tri-State Button')
        checkbox3.setTristate(True)

        vBox = QVBoxLayout()
        vBox.addWidget(checkbox1)
        vBox.addWidget(checkbox2)
        vBox.addWidget(checkbox3)
        vBox.addStretch(1)

        groupBox.setLayout(vBox)

        return groupBox

    def createPushButtonGroup(self):
        groupBox = QGroupBox('Push Buttons')
        groupBox.setCheckable(True)
        groupBox.setChecked(True)

        btn1 = QPushButton('Normal Button')
        btn2 = QPushButton('Toggle Button')
        btn2.setCheckable(True)
        btn2.setChecked(True)
        btn3 = QPushButton('Flat Button')
        btn3.setFlat(True)
        btn4 = QPushButton('Popup Button')

        menu = QMenu(self)
        menu.addAction('First Item')
        menu.addAction('Second Item')
        menu.addAction('Third Item')
        menu.addAction('Fourth Item')

        btn4.setMenu(menu)

        vBox = QVBoxLayout()
        vBox.addWidget(btn1)
        vBox.addWidget(btn2)
        vBox.addWidget(btn3)
        vBox.addWidget(btn4)
        vBox.addStretch(1)

        groupBox.setLayout(vBox)

        return groupBox

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())