# ========================================================
#  RPA_화면분할
# ========================================================
import sys

from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QDesktopWidget, QTextEdit, QTreeView, QAbstractItemView
from PyQt5.QtWidgets import QSplitter
from PyQt5.QtCore import Qt

class Model(QStandardItemModel):
    def __init__(self, data):
        QStandardItemModel.__init__(self)

        # for 문을 이용해서 작성했을 경우
        for j, _type in enumerate(data):
            item = QStandardItem(_type["type"])
            for obj in _type["objects"]:
                child = QStandardItem(obj)
                item.appendRow(child)
            self.setItem(j, 0, item)


class Form(QWidget):

    #========================================================
    #  생성자에서 필요한 것들을 다를 위젯들을 선언
    #========================================================
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)

        # 데이터
        data = [
            {"type": "Window", "objects": ["Win_Item1", "Win_Item2"]},
            {"type": "Web", "objects": ["Web_Item1", "Web_Item2"]},
            {"type": "Test", "objects": ["TEst_Item1", "Test_Item2"]}
        ]

        self.view = QTreeView(self)
        self.model = Model(data)
        self.te_2 = QTextEdit()

        self.split = QSplitter()
        self.vbox = QVBoxLayout()

        self.init_widget()

    #=================================
    # 윈도우를 화면 가운데 위치 시키기
    #=================================
    def center(self):
        qr = self.frameGeometry()  # 창의 위치와 크기 정보를 가져
        cp = QDesktopWidget().availableGeometry().center()  # 사용하는 모니터 화면의 가운데 위치를 파악
        qr.moveCenter(cp)  # 창의 직사각형 위치를 화면의 중심의 위치로 이동합니다.
        self.move(qr.topLeft())  # 현재 창을, 화면의 중심으로 이동했던 직사각형(qr)의 위치로 이동시킵니다.

    # ========================================================
    #  현재 위젯의 모양들을 초기화
    # ========================================================
    def init_widget(self):

        # QTreeView 생성 및 설정
        self.view.setEditTriggers(QAbstractItemView.DoubleClicked)

        self.view.setModel(self.model)
        self.split.addWidget(self.view)
        self.split.addWidget(self.te_2)
        self.split.setSizes([20, 180])      # 분할 크기 정하기

        self.vbox.addWidget(self.split)
        self.setLayout(self.vbox)

        self.setWindowTitle("RPA")
        self.setWindowIcon(QIcon('../../Utils/Images/menu_icon/web.png'))  # 아이콘 추가
        self.resize(500, 350)  # 크기와 위치 설정
        self.center()  # 화면 가운데 위치시키기

# ============================================
# 메인 프로그램 시작하는 부분
# ============================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec())