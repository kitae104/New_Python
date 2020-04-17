#=======================================================
# 기본 위젯 2
#=======================================================
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QVBoxLayout
from PyQt5.QtWidgets import QComboBox, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QProgressBar, QSlider, QDial
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QBasicTimer

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

        # 슬라이더
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.move(350, 50)
        self.slider.setRange(0, 50)
        self.slider.setSingleStep(2)

        # 다이얼
        self.dial = QDial(self)
        self.dial.move(350, 80)
        self.dial.setRange(0, 50)

        btnDefault = QPushButton('Default', self)
        btnDefault.move(355, 190)

        self.lblVal = QLabel(self)
        self.lblVal.move(450, 195)

        self.slider.valueChanged.connect(self.dial.setValue)
        self.slider.valueChanged.connect(self.showValue)
        self.dial.valueChanged.connect(self.slider.setValue)
        btnDefault.clicked.connect(self.button_clicked)

        # 프로그래스 바
        self.progbar = QProgressBar(self)
        self.progbar.setGeometry(50, 150, 300, 25)

        # 푸시 버튼
        self.btn = QPushButton('Start', self)
        self.btn.move(150, 190)
        self.btn.clicked.connect(self.doAction)

        # 타이머 설정
        self.timer = QBasicTimer()
        self.step = 0

        # 라벨, 에디트
        self.lblStr = QLabel(self)
        self.lblStr.move(160, 40)

        lineEdit = QLineEdit(self)
        lineEdit.move(160, 100)
        lineEdit.textChanged[str].connect(self.onChanged)   # 텍스트가 바뀌면 onChanged 호출


        # 라벨, 콤보
        self.lbl = QLabel("선택 내용", self)
        self.lbl.move(50, 100)

        comb = QComboBox(self)
        comb.addItem("선택1")
        comb.addItem("선택2")
        comb.addItem("선택3")
        comb.addItem("선택4")
        comb.move(50, 40)

        # 선택했을 때 함수 호출
        comb.activated[str].connect(self.onActivated)

        self.setWindowTitle("내 어플리케이션")           # 타이틀
        self.setWindowIcon(QIcon('../images/web.png'))  # 아이콘 추가
        self.resize(600, 250)                             # 크기 설정
        self.center()
        self.show()                                       # 보이기

    # 콤보박스에서 선택 시
    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()       # 라벨의 크기 조절

    # 라인에디터에서 글자를 수정할 때
    def onChanged(self, text):
        self.lblStr.setText(text)
        self.lblStr.adjustSize()

    # 프로그래시브 바 버튼 눌렀을 때 동작
    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')

    # QObject와 그 자손들은 timerEvent() 이벤트 핸들러를 갖는다
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            self.step = 0
            return

        self.step = self.step + 1
        self.progbar.setValue(self.step)

    # 버튼이 눌렸을 때 수행할 동작 수행
    def button_clicked(self):
        self.slider.setValue(0)
        self.dial.setValue(0)

    # 슬라이더의 값을 라벨에 출력
    def showValue(self):
        self.lblVal.setText(str(self.slider.value()))
        self.lblVal.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())