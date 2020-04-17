#=======================================================
# 기본 위젯
#=======================================================
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton, QLabel, QCheckBox, QRadioButton
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

        # 라벨 추가
        label1 = QLabel("라벨 1", self)           # self 위치는 부모 위젯
        label1.setAlignment(Qt.AlignCenter)

        label2 = QLabel('라벨 2', self)
        label2.setAlignment(Qt.AlignCenter)

        label3 = QLabel(self)
        label3.setText("라벨 3")
        label3.setAlignment(Qt.AlignRight)

        font1 = label1.font()
        font1.setPointSize(15)

        font2 = label2.font()
        font2.setFamily('Times New Roman')
        font2.setBold(True)

        label1.setFont(font1)
        label2.setFont(font2)

        # 토글 버튼 추가
        btn1 = QPushButton('&Button1', self)
        btn1.setCheckable(True)
        btn1.toggle()

        btn2 = QPushButton(self)
        btn2.setText("Button&2")

        btn3 = QPushButton('Button3', self)
        btn3.setEnabled(False)

        # 체크 박스
        cb = QCheckBox('Show title', self)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        # 라디오 버튼
        rbtn1 = QRadioButton("남자", self)
        rbtn1.setChecked(True)

        rbtn2 = QRadioButton("여자", self)

        hBox1 = QHBoxLayout()
        hBox1.addWidget(btn1)
        hBox1.addWidget(label1)

        hBox2 = QHBoxLayout()
        hBox2.addWidget(label2)
        hBox2.addWidget(btn2)

        hBox3 = QHBoxLayout()
        hBox3.addWidget(btn3)
        hBox3.addWidget(label3)

        hBox4 = QHBoxLayout()
        hBox4.addStretch(1)
        hBox4.addWidget(cb)
        hBox4.addStretch(1)

        hBox5 = QHBoxLayout()
        hBox5.addStretch(1)
        hBox5.addWidget(rbtn1)
        hBox5.addWidget(rbtn2)
        hBox5.addStretch(1)

        # 레이아웃 설정
        vBox = QVBoxLayout()
        vBox.addLayout(hBox1)
        vBox.addLayout(hBox2)
        vBox.addLayout(hBox3)
        vBox.addLayout(hBox4)
        vBox.addLayout(hBox5)

        self.setLayout(vBox)
        self.setWindowTitle("기본 위젯 다루기")           # 타이틀
        self.setWindowIcon(QIcon('../images/web.png'))  # 아이콘 추가
        self.resize(300, 300)                             # 크기 설정
        self.center()
        self.show()                                       # 보이기

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())