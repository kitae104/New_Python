# coding:utf-8

import sys
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

# UI 경로
CalUI = '../ui_files/calculator.ui'

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(CalUI, self)         # UI 로딩하기

        ## 숫자
        self.num_pushButton_1.clicked.connect(lambda state, button=self.num_pushButton_1: self.numClicked(state, button))      # 숫자 버튼 연결하기
        self.num_pushButton_2.clicked.connect(lambda state, button=self.num_pushButton_2: self.numClicked(state, button))      # 숫자 버튼 연결하기
        self.num_pushButton_3.clicked.connect(lambda state, button=self.num_pushButton_3: self.numClicked(state, button))      # 숫자 버튼 연결하기
        self.num_pushButton_4.clicked.connect(lambda state, button=self.num_pushButton_4: self.numClicked(state, button))      # 숫자 버튼 연결하기
        self.num_pushButton_5.clicked.connect(lambda state, button=self.num_pushButton_5: self.numClicked(state, button))      # 숫자 버튼 연결하기
        self.num_pushButton_6.clicked.connect(lambda state, button=self.num_pushButton_6: self.numClicked(state, button))      # 숫자 버튼 연결하기
        self.num_pushButton_7.clicked.connect(lambda state, button=self.num_pushButton_7: self.numClicked(state, button))      # 숫자 버튼 연결하기
        self.num_pushButton_8.clicked.connect(lambda state, button=self.num_pushButton_8: self.numClicked(state, button))      # 숫자 버튼 연결하기
        self.num_pushButton_9.clicked.connect(lambda state, button=self.num_pushButton_9: self.numClicked(state, button))      # 숫자 버튼 연결하기
        self.num_pushButton_0.clicked.connect(lambda state, button=self.num_pushButton_0: self.numClicked(state, button))      # 숫자 버튼 연결하기

        ## 연산
        self.sign_pushButton_1.clicked.connect(lambda state, button=self.sign_pushButton_1: self.numClicked(state, button))    # 연산 버튼 연결하기
        self.sign_pushButton_2.clicked.connect(lambda state, button=self.sign_pushButton_2: self.numClicked(state, button))    # 연산 버튼 연결하기
        self.sign_pushButton_3.clicked.connect(lambda state, button=self.sign_pushButton_3: self.numClicked(state, button))    # 연산 버튼 연결하기
        self.sign_pushButton_4.clicked.connect(lambda state, button=self.sign_pushButton_4: self.numClicked(state, button))    # 연산 버튼 연결하기

        self.p_open_pushButton.clicked.connect(lambda state, button=self.p_open_pushButton: self.numClicked(state, button))    # 연산 버튼 연결하기
        self.p_close_pushButton.clicked.connect(lambda state, button=self.p_close_pushButton: self.numClicked(state, button))    # 연산 버튼 연결하기
        self.dot_pushButton.clicked.connect(lambda state, button=self.dot_pushButton: self.numClicked(state, button))    # 연산 버튼 연결하기
        self.per_pushButton.clicked.connect(lambda state, button=self.per_pushButton: self.numClicked(state, button))    # 연산 버튼 연결하기

        ## 그 외
        self.result_pushButton.clicked.connect(self.makeResult)
        self.reset_pushButton.clicked.connect(self.reset)
        self.del_pushButton.clicked.connect(self.delete)

        # 버튼에 스타일 적용
        #self.del_pushButton.setStyleSheet('image:url(../image/delete.png); border:0px;')

        # hover 스타일 적용
        self.del_pushButton.setStyleSheet(
            '''
            QPushButton{image:url(../image/delete.png); border:0px;}
            QPushButton:hover{image:url(../image/delete_red.png); border:0px;}
            ''')

    def numClicked(self, state, button):
        if button == self.per_pushButton:
            now_num_text = '*0.01'
        else:
            now_num_text = button.text()

        exist_line_text = self.q_lineEdit.text()        # 에디터의 글자 가져오기
        self.q_lineEdit.setText(exist_line_text + now_num_text)   # 에디터에 글자 출력하기

    def makeResult(self):
        try:
            result = eval(self.q_lineEdit.text())
            self.a_lineEdit.setText(str(result))
        except Exception as e:
            print(e)
            self.a_lineEdit.setText('Error')

    def reset(self):
        self.q_lineEdit.clear()
        self.a_lineEdit.setText("0")

    def delete(self):
        exist_line_text = self.q_lineEdit.text()
        #한문자 잘라내기
        exist_line_text =  exist_line_text[:-1]
        self.q_lineEdit.setText(exist_line_text)

app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
app.exec_()         # 이벤트 루프 사용