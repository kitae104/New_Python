import sys
from PyQt5.QtWidgets import QApplication    # 어플리케이션
from PyQt5.QtWidgets import QMainWindow     # 메일 윈도우
from PyQt5.QtWidgets import QWidget         # 위젯
from PyQt5.QtWidgets import QPushButton     # 푸시 버튼
from PyQt5.QtWidgets import QToolTip        # 툴팁
from PyQt5.QtWidgets import QAction         # 이벤트 처리
from PyQt5.QtWidgets import qApp            # 어플
from PyQt5.QtWidgets import QDesktopWidget  # 데스크탑 위젯

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QDate, QDateTime
from PyQt5.QtCore import Qt

#========================================================
# 클래스 생성시에 QMainWindow와 QWidget을 구분해야 함
# QMainWindow 클래스를 이용해서 메인 어플리케이션 창 생성
#========================================================
class MyApp(QMainWindow):

    #================================
    # 초기화 동작 수행
    #================================
    def __init__(self):
        super().__init__()
        self.date = QDateTime.currentDateTime() # 현재 날짜 시간 정보
        self.initUI()                           # 기본 UI 초기화

    #=================================
    # 윈도우를 화면 가운데 위치 시키기
    #=================================
    def center(self):
        qr = self.frameGeometry()                           # 창의 위치와 크기 정보를 가져
        cp = QDesktopWidget().availableGeometry().center()  # 사용하는 모니터 화면의 가운데 위치를 파악
        qr.moveCenter(cp)                                   # 창의 직사각형 위치를 화면의 중심의 위치로 이동합니다.
        self.move(qr.topLeft())                             # 현재 창을, 화면의 중심으로 이동했던 직사각형(qr)의 위치로 이동시킵니다.

    #================================
    # 화면 기본 설정
    #================================
    def initUI(self):

        # 메뉴에서 사용할 엑션 추가
        exitAction = QAction(QIcon('../images/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')     # 상태바에 출력할 정보
        exitAction.triggered.connect(qApp.quit)           # 생성된 시그널을 위젯의 quit 메소드에 연결

        # 메뉴 바 생성
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        # 메뉴 생성
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        # 툴바 생성
        self.toolBar = self.addToolBar('Exit')
        self.toolBar.addAction(exitAction)

        # 상태바 추가 - 현재 날짜 추가
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        # 툴팁 추가
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')  # 전체 윈도우에 툴 팁

        # 버튼 추가
        btn = QPushButton('Quit', self)                         # 버튼 추가, self는 버튼이 위치할 부모 위젯
        btn.move(50, 80)
        btn.setToolTip('This is a <b>QPushButton</b> widget')   # 버튼에 툴 팁
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle("내 어플리케이션")           # 타이틀
        self.setWindowIcon(QIcon('../images/web.png'))  # 아이콘 추가
        self.resize(500, 350)                             # 크기와 위치 설정
        self.center()                                     # 화면 가운데 위치시키기
        self.show()                                       # 보이기

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())