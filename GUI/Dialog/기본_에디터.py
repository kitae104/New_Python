# ========================================================
# 기본 에디터
# ========================================================
import sys
from PyQt5.QtWidgets import QApplication, QInputDialog, QTextEdit, \
    QColorDialog, QFontDialog, QFileDialog, QMessageBox  # 어플리케이션
from PyQt5.QtWidgets import QMainWindow  # 메일 윈도우
from PyQt5.QtWidgets import QToolTip  # 툴팁
from PyQt5.QtWidgets import QAction  # 이벤트 처리
from PyQt5.QtWidgets import qApp  # 어플
from PyQt5.QtWidgets import QDesktopWidget  # 데스크탑 위젯

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont

from PyQt5.QtCore import QDateTime
from PyQt5.QtCore import Qt


# ========================================================
# 클래스 생성시에 QMainWindow와 QWidget을 구분해야 함
# QMainWindow 클래스를 이용해서 메인 어플리케이션 창 생성
# ========================================================
class MyApp(QMainWindow):

    # ================================
    # 초기화 동작 수행
    # ================================
    def __init__(self):
        super().__init__()
        self.date = QDateTime.currentDateTime()  # 현재 날짜 시간 정보
        self.initUI()  # 기본 UI 초기화

    # =================================
    # 윈도우를 화면 가운데 위치 시키기
    # =================================
    def center(self):
        qr = self.frameGeometry()  # 창의 위치와 크기 정보를 가져
        cp = QDesktopWidget().availableGeometry().center()  # 사용하는 모니터 화면의 가운데 위치를 파악
        qr.moveCenter(cp)  # 창의 직사각형 위치를 화면의 중심의 위치로 이동합니다.
        self.move(qr.topLeft())  # 현재 창을, 화면의 중심으로 이동했던 직사각형(qr)의 위치로 이동시킵니다.

    # ================================
    # 화면 기본 설정
    # ================================
    def initUI(self):

        # 메뉴 바 생성
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        # 메뉴 생성
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(self.openAction())
        fileMenu.addAction(self.exitAction())

        dialogMenu = menubar.addMenu('&Dialog')
        dialogMenu.addAction(self.inputDialogAction())
        dialogMenu.addAction(self.colorDialogAction())
        dialogMenu.addAction(self.fontDialogAction())

        # 툴바 생성
        self.toolBar = self.addToolBar('Open')
        self.toolBar.addAction(self.openAction())

        self.toolBar = self.addToolBar('Exit')
        self.toolBar.addAction(self.exitAction())

        # 상태바 추가 - 현재 날짜 추가
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        # 툴팁 추가
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('다이얼로그 연습중 입니다.')  # 전체 윈도우에 툴 팁

        # 텍스트 브라우저 추가 QTextBrowser 사용도 가능
        self.textEdit = QTextEdit(self)
        self.textEdit.setAcceptRichText(True)
        # self.textEdit.setOpenExternalLinks(True)
        # 화면 중앙에 위치하게 함.
        self.setCentralWidget(self.textEdit)

        self.setWindowTitle("내 어플리케이션")  # 타이틀
        self.setWindowIcon(QIcon('../../Utils/Images/menu_icon/web.png'))  # 아이콘 추가
        self.resize(500, 350)  # 크기와 위치 설정
        self.center()  # 화면 가운데 위치시키기
        self.show()  # 보이기

    #============================================
    # 종료 기능 - 확인 후 종료 수행
    #============================================
    def closeEvent(self, event):
        # 두번째 매개변수는 타이틀바에 나타날 문자열 ('Message'),
        # 세번째 매개변수는 대화창에 나타날 문자열 ('Are you sure to quit?')을 입력
        # 네 번째에는 대화창에 보여질 버튼의 종류를 입력하고
        # 마지막으로 디폴트로 선택될 버튼을 설정해줍니다.
        replay = QMessageBox.question(self, '종료 확인', '정말 종료 할까요?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if replay == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    #============================================
    # 파일 열기 기능
    #============================================
    def openAction(self):
        action = QAction(QIcon('../../Utils/Images/menu_icon/open.png'), 'Open', self)
        action.setShortcut('Ctrl+O')
        action.setStatusTip('Open New File')  # 상태바에 출력할 정보
        action.triggered.connect(self.showOpenDialog)  # 생성된 시그널을 위젯의 quit 메소드에 연결
        return action

    #============================================
    # show dialog 처리
    #============================================
    def showOpenDialog(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open file', './')

        if fileName[0]:
            # 주의 : 파일 읽을 때 인코딩이 없으면 오류 발생하는 경우가 종종 있음
            f = open(fileName[0], 'r', encoding="utf8")
            with f:
                data = f.read()
                self.textEdit.setText(data)
                f.close()

    #============================================
    # 나가기 기능 구현
    #============================================
    def exitAction(self):
        action = QAction(QIcon('../../Utils/Images/menu_icon/exit.png'), 'Exit', self)
        action.setShortcut('Ctrl+Q')
        action.setStatusTip('Exit Application')  # 상태바에 출력할 정보
        action.triggered.connect(self.closeEvent)  # 종료 이벤트를 호출
        return action

    #============================================
    # input dialog 메뉴 선택한 경우
    #============================================
    def inputDialogAction(self):
        action = QAction(QIcon('../../Utils/Images/menu_icon/input.png'), 'Input Dialog', self)
        action.setStatusTip('Input Dialog')  # 상태바에 출력할 정보
        action.triggered.connect(self.showInputDialog)  # 생성된 시그널을 위젯의 quit 메소드에 연결
        return action

    #============================================
    # show dialog 처리
    #============================================
    def showInputDialog(self):
        # 두 번째 매개변수는 대화창의 타이틀, 세 번째 매개변수는 대화창 안에 보여질 메세지를 의미합니다.
        # 입력 대화창은 입력한 텍스트와 불 (Boolean) 값을 반환합니다.
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

        if ok:
            self.textEdit.append(str(text))

    #============================================
    # color dialog 메뉴 선택한 경우
    #============================================
    def colorDialogAction(self):
        action = QAction(QIcon('../../Utils/Images/menu_icon/color.png'), 'Color Dialog', self)
        action.setStatusTip('Color Dialog')  # 상태바에 출력할 정보
        action.triggered.connect(self.showColorDialog)  # 생성된 시그널을 위젯의 quit 메소드에 연결
        return action

    #============================================
    # show color dialog 처리
    #============================================
    def showColorDialog(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.textEdit.setTextColor(color)

    #============================================
    # color dialog 메뉴 선택한 경우
    #============================================
    def fontDialogAction(self):
        action = QAction(QIcon('../../Utils/Images/menu_icon/font.png'), 'Font Dialog', self)
        action.setStatusTip('Font Dialog')  # 상태바에 출력할 정보
        action.triggered.connect(self.showFontDialog)  # 생성된 시그널을 위젯의 quit 메소드에 연결
        return action

    #============================================
    # show color dialog 처리
    #============================================
    def showFontDialog(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.textEdit.setFont(font)

#============================================
# 메인 프로그램 시작하는 부분
#============================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
