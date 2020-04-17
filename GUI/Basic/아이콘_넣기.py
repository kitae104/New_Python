import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()           # 기본 UI 초기화

    def initUI(self):
        self.setWindowTitle("아이콘 추가 연습")        # 타이틀
        self.setWindowIcon(QIcon('../images/web.png'))  # 아이콘 추가
        self.setGeometry(300, 300, 300, 200)
        self.show()                                     # 보이기 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())