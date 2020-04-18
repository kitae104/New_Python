#=======================================================
# 픽스 맵 위젯
#=======================================================
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QVBoxLayout, QTabWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap


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

        # 픽스 맵
        pixmap = QPixmap('../../Utils/Images/korea_mask.jpg')

        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap)
        lbl_size = QLabel('Width: ' + str(pixmap.width()) + ", Height: " + str(pixmap.height()))
        lbl_size.setAlignment(Qt.AlignCenter)

        # 레이아웃 설정
        vBox = QVBoxLayout()
        vBox.addWidget(lbl_img)
        vBox.addWidget(lbl_size)

        self.setLayout(vBox)

        self.setWindowTitle("픽스 맵 위젯")           # 타이틀
        self.setWindowIcon(QIcon('../../Utils/Images/web.png'))  # 아이콘 추가
        self.resize(500, 350)                             # 크기 설정
        self.center()
        self.show()                                       # 보이기

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())