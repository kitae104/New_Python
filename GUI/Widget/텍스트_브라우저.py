#=======================================================
# 텍스트 브라우저 위젯
# QTextBrowser 클래스는 하이퍼텍스트 내비게이션을 포함하는 리치 텍스트 (서식있는 텍스트) 브라우저를 제공
# 읽기 전용이며, QTextEdit의 확장형으로서 하이퍼텍스트 문서의 링크들을 사용할 수 있습니다.
#=======================================================
import sys

from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QVBoxLayout, QLineEdit, QTextBrowser, QPushButton, \
    QLabel
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

        # 라인 에디트
        self.lineEdit = QLineEdit()
        # Enter키를 누르면 append_text 메서드가 호출
        self.lineEdit.returnPressed.connect(self.appendText)

        # 라벨
        self.lbl = QLabel('전체 단어 수 : 0')
        self.lbl.setAlignment(Qt.AlignCenter)

        # 텍스트 브라우저
        self.textBrowser = QTextBrowser()
        self.textBrowser.setAcceptRichText(True)
        # setOpenExternalLinks()를 True로 설정해주면, 외부 링크로의 연결이 가능
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.textChanged.connect(self.textBrowserChanged)

        self.clearBtn = QPushButton('Clear')
        self.clearBtn.pressed.connect(self.clearText)

        # 레이아웃 설정
        vBox = QVBoxLayout()
        vBox.addWidget(self.lineEdit, 0)
        vBox.addWidget(self.lbl)
        vBox.addWidget(self.textBrowser, 2)
        vBox.addWidget(self.clearBtn, 3)

        self.setLayout(vBox)

        self.setWindowTitle("텍스트 브라우저")           # 타이틀
        self.setWindowIcon(QIcon('../../Utils/Images/web.png'))  # 아이콘 추가
        self.resize(500, 350)                             # 크기 설정
        self.center()
        self.show()                                       # 보이기

    def appendText(self):
        text = self.lineEdit.text()
        self.textBrowser.append(text)
        self.lineEdit.clear()

    def clearText(self):
        self.textBrowser.clear()

    def textBrowserChanged(self):
        text = self.textBrowser.toPlainText()
        self.lbl.setText('전체 단어 수 : ' + str(len(text.split())))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())