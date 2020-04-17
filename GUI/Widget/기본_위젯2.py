#=======================================================
# 기본 위젯 2
#=======================================================
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QVBoxLayout
from PyQt5.QtWidgets import QComboBox, QLabel, QLineEdit
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
        self.resize(500, 350)                             # 크기 설정
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())