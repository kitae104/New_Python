# ========================================================
#  RPA_화면분할
# ========================================================
import sys

from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QDesktopWidget, QTextEdit, \
    QTreeView, QAbstractItemView, QMessageBox, QInputDialog, QAction, qApp, QToolBar, QMainWindow, \
    QPushButton, QDockWidget
from PyQt5.QtWidgets import QSplitter, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QDateTime

from selenium import webdriver
import time

# 테이블 데이터
kospi_top5 = {
    'code': [],
    'name': [],
    'cprice': ['']
}

# 컬럼 인덱스 관리
column_idx_lookup = {'code': 0, 'name': 1, 'cprice': 2}

# 트리 데이터
data = [
    {"type": "Web", "objects": ["Open Browser", "Set Text", "Click Item"]},
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

class Form(QMainWindow):

    #========================================================
    #  생성자에서 필요한 것들을 다를 위젯들을 선언
    #========================================================
    def __init__(self):
        super().__init__()
        self.date = QDateTime.currentDateTime()  # 현재 날짜 시간 정보
        self.initUI()  # 기본 UI 초기화

    def make_tree_table(self):
        self.view = QTreeView(self)
        self.model = Model()
        self.view.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 수정 불가
        self.view.doubleClicked.connect(self.treeMedia_doubleClicked)
        self.table = QTableWidget(self)
        self.table.setRowCount(0)
        self.table.setColumnCount(3)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 수정 불가
        self.setTableData()
        self.split = QSplitter()

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
    def initUI(self):

        # 메뉴 바 생성
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        # 메뉴 생성
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(self.exitActionFunc())

        # 툴바 생성
        self.toolBar = self.addToolBar('Run')
        self.toolBar.addAction(self.runActionFunc())

        self.toolBar = self.addToolBar('Exit')
        self.toolBar.addAction(self.exitActionFunc())

        # 상태바 추가 - 현재 날짜 추가
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        self.make_tree_table()

        # QTreeView 생성 및 설정
        #self.view.setEditTriggers(QAbstractItemView.DoubleClicked)

        self.view.setModel(self.model)

        dockWidget1 = QDockWidget('Activity', self)
        dockWidget1.setWidget(self.view)
        dockWidget1.setFloating(False)
        dockWidget2 = QDockWidget('스크립트', self)
        dockWidget2.setWidget(self.table)
        dockWidget2.setFloating(False)
        # self.setCentralWidget(self.table)
        self.addDockWidget(Qt.LeftDockWidgetArea, dockWidget1)
        self.addDockWidget(Qt.RightDockWidgetArea, dockWidget2)

        # 시작 크기 지정하기
        self.resizeDocks({dockWidget1, dockWidget2}, {180, 630}, Qt.Horizontal)


        self.setWindowTitle("파이썬_RPA")
        self.setWindowIcon(QIcon('../../Utils/Images/menu_icon/web.png'))  # 아이콘 추가
        self.resize(800, 550)  # 크기와 위치 설정
        self.center()  # 화면 가운데 위치시키기

    # ========================================================
    # run 엑션 설정
    # ========================================================
    def runActionFunc(self):
        runAction = QAction(QIcon('../../Utils/Images/menu_icon/run.png'), 'Run', self)
        runAction.setShortcut('Ctrl+R')
        runAction.setStatusTip('Run RPA Application')  # 상태바에 출력할 정보
        runAction.triggered.connect(self.scrip_run)  # 생성된 시그널을 위젯의 quit 메소드에 연결
        return runAction


    # ========================================================
    #  exit 엑션 설정
    # ========================================================
    def exitActionFunc(self):
        exitAction = QAction(QIcon('../images/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')  # 상태바에 출력할 정보
        exitAction.triggered.connect(qApp.quit)  # 생성된 시그널을 위젯의 quit 메소드에 연결
        return exitAction

    # ========================================================
    #  선택 내용에 따라 수행하기
    # ========================================================
    def treeMedia_doubleClicked(self,index):
        item = self.view.selectedIndexes()[0]
        activity = item.model().itemFromIndex(index).text()

        if activity == 'Open Browser':
            self.open_browser()

        elif activity == 'Set Text':
            self.set_text()

        elif activity == 'Click Item':
            self.click_item()

    def open_browser(self):
        url, ok = QInputDialog.getText(self, 'Open Browser', '이동할 URL :')
        # self.add_table_row()
        row_cnt = self.table.rowCount()
        self.table.setRowCount(row_cnt + 1)
        self.table.setItem(row_cnt, 0, QTableWidgetItem("Open_Browser"))
        self.table.setItem(row_cnt, 1, QTableWidgetItem(url))
        self.table.setItem(row_cnt, 2, QTableWidgetItem(""))

    def set_text(self):
        selector, ok = QInputDialog.getText(self, 'Set Text', '셀렉터 선택 :')
        msg, ok = QInputDialog.getText(self, 'Set Text', 'Text 입력 :')
        
        row_cnt = self.table.rowCount()
        self.table.setRowCount(row_cnt + 1)
        self.table.setItem(row_cnt, 0, QTableWidgetItem("Set_Text"))
        self.table.setItem(row_cnt, 1, QTableWidgetItem(selector))
        self.table.setItem(row_cnt, 2, QTableWidgetItem(msg))

    def click_item(self):
        selector, ok = QInputDialog.getText(self, 'Set Text', '셀렉터 선택 :')

        row_cnt = self.table.rowCount()
        self.table.setRowCount(row_cnt + 1)
        self.table.setItem(row_cnt, 0, QTableWidgetItem("Click_Item"))
        self.table.setItem(row_cnt, 1, QTableWidgetItem(selector))
        self.table.setItem(row_cnt, 2, QTableWidgetItem(""))

    # ========================================================
    #  선택 내용에 따라 수행하기
    # ========================================================
    def add_table_row(self):
        row_cnt = self.table.rowCount()
        self.table.setRowCount(row_cnt + 1)

    # ========================================================
    #  실제 스크립트를 수행하는 부분
    # ========================================================
    def scrip_run(self):
        rowCnt = self.table.model().rowCount()
        for i in range(rowCnt):
            kind = self.table.item(i,0).text()
            if kind == "Open_Browser":
                self.openBrowser(self.table.item(i,1).text())
            elif kind == "Set_Text":
                self.setText(self.table.item(i,1).text(), self.table.item(i,2).text())
            elif kind == "Click_Item":
                self.clickItem(self.table.item(i,1).text())

    # ========================================================
    #  기능 구현 부분
    # ========================================================
    def openBrowser(self, input_url):
        self.driver = webdriver.Chrome()  # 크롬 드라이버 초기화
        url = str(input_url)
        self.driver.get(url)

    def setText(self, selector, msg):
        self.driver.find_element_by_css_selector(str(selector)).click()
        self.driver.find_element_by_css_selector(str(selector)).send_keys(str(msg))

    def clickItem(self, selector):
        self.driver.find_element_by_css_selector(str(selector)).click()


# ============================================
# 메인 프로그램 시작하는 부분
# ============================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec())