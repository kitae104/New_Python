# ========================================================
#  RPA_화면분할
# ========================================================
import sys

from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QDesktopWidget, QTextEdit, QTreeView, QAbstractItemView, \
    QMessageBox, QInputDialog
from PyQt5.QtWidgets import QSplitter, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

# 테이블 데이터
kospi_top5 = {
    'code': ['005930', '015760', '005380', '090430', '012330'],
    'name': ['삼성전자', '한국전력', '현대차', '아모레퍼시픽', '현대모비스'],
    'cprice': ['1,269,000', '60,100', '132,000', '414,500', '243,500']
}

# 컬럼 인덱스 관리
column_idx_lookup = {'code': 0, 'name': 1, 'cprice': 2}

# 트리 데이터
data = [
    {"type": "Web", "objects": ["Open Browser", "Win_Item2"]},
    {"type": "DeskTop", "objects": ["Web_Item1", "Web_Item2"]},
    {"type": "Test", "objects": ["TEst_Item1", "Test_Item2"]}
]

class Model(QStandardItemModel):
    def __init__(self):
        QStandardItemModel.__init__(self)

        # for 문을 이용해서 작성했을 경우
        for j, _type in enumerate(data):
            item = QStandardItem(_type["type"])
            for obj in _type["objects"]:
                child = QStandardItem(obj)
                item.appendRow(child)
            self.setItem(j, 0, item)
        self.setHorizontalHeaderLabels(['Activity'])

class Form(QWidget):

    #========================================================
    #  생성자에서 필요한 것들을 다를 위젯들을 선언
    #========================================================
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)

        self.view = QTreeView(self)
        self.model = Model()
        self.view.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 수정 불가
        self.view.doubleClicked.connect(self.treeMedia_doubleClicked)

        self.table = QTableWidget(self)
        self.table.setRowCount(0)
        self.table.setColumnCount(3)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)    # 수정 불가
        self.setTableData()

        self.split = QSplitter()
        self.vbox = QVBoxLayout()

        self.init_widget()

    # =================================
    # 테이블에 데이터 입력하기 
    # =================================
    def setTableData(self):
        column_headers = ['    엑티비티    ', '               동작              ', '       속성       ']
        self.table.setHorizontalHeaderLabels(column_headers)
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(1, 100)
        self.table.setColumnWidth(2, 50)

        for k, v in kospi_top5.items():
            col = column_idx_lookup[k]

            for row, val in enumerate(v):
                item = QTableWidgetItem(val)
                if col == 2:
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignRight)

                self.table.setItem(row, col, item)

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

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
        #self.view.setEditTriggers(QAbstractItemView.DoubleClicked)

        self.view.setModel(self.model)
        self.split.addWidget(self.view)
        self.split.addWidget(self.table)
        self.split.setSizes([20, 180])      # 분할 크기 정하기

        self.vbox.addWidget(self.split)
        self.setLayout(self.vbox)

        self.setWindowTitle("RPA")
        self.setWindowIcon(QIcon('../../Utils/Images/menu_icon/web.png'))  # 아이콘 추가
        self.resize(500, 350)  # 크기와 위치 설정
        self.center()  # 화면 가운데 위치시키기

    # ========================================================
    #  선택 내용에 따라 수행하기
    # ========================================================
    def treeMedia_doubleClicked(self,index):
        item = self.view.selectedIndexes()[0]
        activity = item.model().itemFromIndex(index).text()

        if activity == 'Open Browser':
            self.open_browser()

        elif activity == 'Win_Item2':
            QMessageBox.information(self, "메뉴2", "Win_Item2  ");
            self.add_table_row()

    def open_browser(self):
        url, ok = QInputDialog.getText(self, 'Open Browser', '이동할 URL :')
        # self.add_table_row()
        row_cnt = self.table.rowCount()
        self.table.setRowCount(row_cnt + 1)
        self.table.setItem(row_cnt, 0, QTableWidgetItem("AAA"))
        self.table.setItem(row_cnt, 1, QTableWidgetItem(url))
        self.table.setItem(row_cnt, 2, QTableWidgetItem("CCC"))

    # ========================================================
    #  선택 내용에 따라 수행하기
    # ========================================================
    def add_table_row(self):
        row_cnt = self.table.rowCount()
        self.table.setRowCount(row_cnt + 1)


# ============================================
# 메인 프로그램 시작하는 부분
# ============================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec())