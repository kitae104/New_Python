import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QDropEvent 
from PyQt5 import QtGui
from selenium import webdriver
from PyQt5.QtGui import QIcon

from collections import Counter
import json
from PyQt5.QtGui import QKeyEvent
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime
from openpyxl import load_workbook

import pytesseract
from PIL import Image
import cv2
import numpy as np
import pandas as pd
from pandas import DataFrame
import csv
import urllib.request
from bs4 import BeautifulSoup

import os
from urllib.request import urlopen

import konlpy.tag
from collections import Counter

import wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from os import path
import pyautogui



class MyWindow(QWidget):

    
    

    def __init__(self,):

        super().__init__()

        # 메인리스트 기준이 되는 리스트
        self.ObLs = []

        
        # driver를 전역변수로 설정해서 다양한 함수에서 driver를 사용할 수 있도록 설정
        self.driver = ""

        
        
        
        ############################################################################
        ###################### 기능들에대한 딕셔너리 설정###########################
        ###########################################################################

        self.DicOpenBrowser  = {
        
                'DicOpenBrowser': {
                    'DicOpenBrowserName': [("OpenBrowser")] ,
                    'DicOpenBrowserUrl': [("Default")]
                    }
                }

        
        self.DicMakeFolder  = {
        
                'DicMakeFolder': {
                    'DicMakeFolderName': [("MakeFolder")] ,
                    'DicMakeFolderValue': [("Default")]
                    }
                }


        self.DicPageDown  = {
        
                'DicPageDown': {
                    'DicPageDownName': [("PageDown")] ,
                    'DicPageDownTag': [("Default")] ,
                    'DicPageDownCount': [("Default")]
                    }
                }
        

        self.DicEnter  = {
        
                'DicEnter': {
                    'DicEnterName': [("Enter")] ,
                    'DicEnterValue': [("Default")] 
                    }
                }

        self.DicBrowserClose  = {
        
                'DicBrowserClose': {
                    'DicBrowserCloseName': [("BrowserClose")] ,
                    'DicBrowserCloseValue': [("Default")]
                    }
                }
        
        
        self.DicAssign  = {
        
                'DicAssign': {
                    'DicAssignName': [("Assign")] ,
                    'DicAssignValueName': [("Default")] ,
                    'DicAssignValueVariable': [("Default")] ,
                    }
                }


        self.DicSetText  = {
        
                'DicSetText': {
                    'DicSetTextName': [("SetText")] ,
                    'DicSetTextValues1': [("Default")] ,
                    'DicSetTextValues2': [("Default")]
                    }
                }


        self.DicClick  = {
        
                'DicClick': {
                    'DicClickName': [("Click")] ,
                    'DicClickValue': [("Default")]
                    }
                }

        self.DicMousePosition  = {
        
                'DicMousePosition': {
                    'DicMousePositionName': [("MousePosition")] ,
                    'DicMousePositionValue': [("Default")]
                    }
                }
        
        self.DicMoveToPosition  = {
        
                'DicMoveToPosition': {
                    'DicMoveToPositionName': [("MoveToPosition")] ,
                    'DicMoveToPositionValues1': [("Default")] ,
                    'DicMoveToPositionValues2': [("Default")]
                    }
                }
        
        self.DicMoveToPositionClick  = {
        
                'DicMoveToPositionClick': {
                    'DicMoveToPositionClickName': [("MoveToPositionClick")] ,
                    'DicMoveToPositionClickValues1': [("Default")] ,
                    'DicMoveToPositionClickValues2': [("Default")]
                    }
                }
        
        self.DicMoveToPositionDoubleClick  = {
        
                'DicMoveToPositionDoubleClick': {
                    'DicMoveToPositionDoubleClickName': [("MoveToPositionDoubleClick")] ,
                    'DicMoveToPositionDoubleClickValues1': [("Default")] ,
                    'DicMoveToPositionDoubleClickValues2': [("Default")]
                    }
                }
        
        self.DicTypeWrite  = {
        
                'DicTypeWrite': {
                    'DicTypeWriteName': [("TypeWrite")] ,
                    'DicTypeWriteValue': [("Default")]
                    }
                }
        
        

        self.DicTextCrawling  = {

                'DicTextCrawling': {
                    'DicTextCrawlingName': [("TextCrawling")] ,
                    'DicTextCrawlingValues1': [("Default")] ,
                    'DicTextCrawlingValues2': [("Default")] ,
                    'DicTextCrawlingValues3': [("Default")] ,
                    'DicTextCrawlingValues4': [("Default")] ,
                    'DicTextCrawlingValues5': [("Default")] ,
                    'DicTextCrawlingValues6': [("Default")] 
                    }
                }

        self.DicImageCrawling  = {

                'DicImageCrawling': {
                    'DicImageCrawlingName': [("ImageCrawling")] ,
                    'DicImageCrawlingValues1': [("Default")] ,
                    'DicImageCrawlingValues2': [("Default")] ,
                    'DicImageCrawlingValues3': [("Default")] ,
                    'DicImageCrawlingValues4': [("Default")]
                    }
                }
        
        self.DicInstaImageCrawling  = {

                'DicInstaImageCrawling': {
                    'DicInstaImageCrawlingName': [("InstaImageCrawling")] ,
                    'DicInstaImageCrawlingValues1': [("Default")] ,
                    'DicInstaImageCrawlingValues2': [("Default")]
                    }
                }


        self.DicExcelWrite  = {

                'DicExcelWrite': {
                    'DicExcelWriteName': [("ExcelWrite")] ,
                    'DicExcelWriteValues1': [("Default")] ,
                    'DicExcelWriteValues2': [("Default")] ,
                    'DicExcelWriteValues3': [("Default")] 
                    }
                }


        self.DicExcelRead  = {

                'DicExcelRead': {
                    'DicExcelReadName': [("ExcelRead")] ,
                    'DicExcelReadValues1': [("Default")] ,
                    'DicExcelReadValues2': [("Default")] 
                    }
                }

        self.DicRowDropNa  = {

                'DicRowDropNa': {
                    'DicRowDropNaName': [("RowDropNa")] ,
                    'DicRowDropNaValue': [("Default")] ,
                    }
                }
        
        self.DicColumnDropNa  = {

                'DicColumnDropNa': {
                    'DicColumnDropNaName': [("ColumnDropNa")] ,
                    'DicColumnDropNaValue': [("Default")] ,
                    }
                }

        self.DicCsvWrite  = {

                'DicCsvWrite': {
                    'DicCsvWriteName': [("CsvWrite")] ,
                    'DicCsvWriteValues1': [("Default")] ,
                    'DicCsvWriteValues2': [("Default")] ,
                    'DicCsvWriteValues3': [("Default")] 
                    }
                }

        self.DicCsvRead  = {

                'DicCsvRead': {
                    'DicCsvReadName': [("CsvRead")] ,
                    'DicCsvReadValues1': [("Default")] ,
                    'DicCsvReadValues2': [("Default")] 
                    }
                }

        
        self.DicFor  = {

                'DicFor': {
                    'DicForName': [("For")] ,
                    'DicForValues1': [("Default")] ,
                    'DicForValues2': [("Default")] ,
                    'DicForValues3': [("Default")] 
                    }
                }


        self.DicMaxWin  = {
        
                'DicMaxWin': {
                    'DicMaxWinName': [("MaxWin")] ,
                    'DicMaxWinValue': [("Default")]
                    }
                }

        self.DicSwitchWin  = {
        
                'DicSwitchWin': {
                    'DicSwitchWinName': [("SwitchWin")] ,
                    'DicSwitchWinValue': [("Default")]
                    }
                }

        self.DicTimeSleep  = {
        
                'DicTimeSleep': {
                    'DicTimeSleepName': [("TimeSleep")] ,
                    'DicTimeSleepValue': [("Default")]
                    }
                }
        
        self.DicFillNa  = {
        
                'DicFillNa': {
                    'DicFillNaName': [("FillNa")] ,
                    'DicFillNaValues1': [("Default")] ,
                    'DicFillNaValues2': [("Default")]
                    }
                }

                

        self.DicMakeClipBoard  = {
        
                'DicMakeClipBoard': {
                    'DicMakeClipBoardName': [("MakeClipBoard")] ,
                    'DicMakeClipBoardValues1': [("Default1")],
                    'DicMakeClipBoardValues2': [("Default2")],
                    'DicMakeClipBoardValues3': [("Default3")],
                    }
                }


        self.DicResize  = {
        
                'DicResize': {
                    'DicResizeName': [("Resize")] ,
                    'DicResizeValues1': [("Default1")],
                    'DicResizeValues2': [("Default2")],
                    'DicResizeValues3': [("Default3")],
                    'DicResizeValues4': [("Default4")]
                    }
                }


        self.DicConvertGray  = {
        
                'DicConvertGray': {
                    'DicConvertGrayName': [("ConvertGray")] ,
                    'DicConvertGrayValues1': [("Default1")],
                    'DicConvertGrayValues2': [("Default2")]
                    }
                }


        self.DicImgSquare  = {
        
                'DicImgSquare': {
                    'DicImgSquareName': [("ImgSquare")] ,
                    'DicImgSquareValues1': [("Default1")],
                    'DicImgSquareValues2': [("Default2")]
                    }
                }

        self.DicThresHolding  = {
        
                'DicThresHolding': {
                    'DicThresHoldingName': [("ThresHolding")] ,
                    'DicThresHoldingValues1': [("Default1")],
                    'DicThresHoldingValues2': [("Default2")]
                    }
                }
                
        self.DicEqualizeHist  = {
        
                'DicEqualizeHist': {
                    'DicEqualizeHistName': [("EqualizeHist")] ,
                    'DicEqualizeHistValues1': [("Default1")],
                    'DicEqualizeHistValues2': [("Default2")]
                    }
                }

        
        self.DicColorEqualizeHist  = {
        
                'DicColorEqualizeHist': {
                    'DicColorEqualizeHistName': [("ColorEqualizeHist")] ,
                    'DicColorEqualizeHistValues1': [("Default1")],
                    'DicColorEqualizeHistValues2': [("Default2")]
                    }
                }

        self.DicBlur  = {
        
                'DicBlur': {
                    'DicBlurName': [("Blur")] ,
                    'DicBlurValues1': [("Default1")] ,
                    'DicBlurValues2': [("Default2")] ,
                    'DicBlurValues3': [("Default3")] ,
                    'DicBlurValues4': [("Default4")] ,
                    }
                }

        self.Dic2DBlur  = {
        
                'Dic2DBlur': {
                    'Dic2DBlurName': [("Blur_2D")] ,
                    'Dic2DBlurValues1': [("Default1")] ,
                    'Dic2DBlurValues2': [("Default2")] ,
                    'Dic2DBlurValues3': [("Default3")] 
                    }
                }

        self.DicGausianBlur  = {
        
                'DicGausianBlur': {
                    'DicGausianBlurName': [("GausianBlur")] ,
                    'DicGausianBlurValues1': [("Default1")] ,
                    'DicGausianBlurValues2': [("Default2")] ,
                    'DicGausianBlurValues3': [("Default3")] ,
                    'DicGausianBlurValues4': [("Default4")] ,
                    'DicGausianBlurValues5': [("Default5")]  
                    }
                }

        self.DicMedianBlur  = {
        
                'DicMedianBlur': {
                    'DicMedianBlurName': [("MedianBlur")] ,
                    'DicMedianBlurValues1': [("Default1")] ,
                    'DicMedianBlurValues2': [("Default2")] ,
                    'DicMedianBlurValues3': [("Default3")] 
                    }
                }

        self.DicBilateralBlur  = {
        
                'DicBilateralBlur': {
                    'DicBilateralBlurName': [("BilateralBlur")] ,
                    'DicBilateralBlurValues1': [("Default1")] ,
                    'DicBilateralBlurValues2': [("Default2")] ,
                    'DicBilateralBlurValues3': [("Default3")] ,
                    'DicBilateralBlurValues4': [("Default4")] ,
                    'DicBilateralBlurValues5': [("Default5")] 
                    }
                }

        self.DicFilter_Content  = {
        
                'DicFilter_Content': {
                    'DicFilter_ContentName': [("Filter_Content")] ,
                    'DicFilter_ContentValues1': [("Default1")] ,
                    'DicFilter_ContentValues2': [("Default2")]
                    }
                }

        self.DicMorphs  = {
        
                'DicMorphs': {
                    'DicMorphsName': [("Morphs")] ,
                    'DicMorphsValues1': [("Default1")] ,
                    'DicMorphsValues2': [("Default2")]
                    }
                }

        self.DicExtract_Word  = {
        
                'DicExtract_Word': {
                    'DicExtract_WordName': [("Extract_Word")] ,
                    'DicExtract_WordValues1': [("Default1")] ,
                    'DicExtract_WordValues2': [("Default2")]
                    }
                }
        
        self.DicCounter_Word  = {
        
                'DicCounter_Word': {
                    'DicCounter_WordName': [("Counter_Word")] ,
                    'DicCounter_WordValues1': [("Default1")] ,
                    'DicCounter_WordValues2': [("Default2")]
                    }
                }
        
        self.DicWordCloud  = {
        
                'DicWordCloud': {
                    'DicWordCloudName': [("WordCloud")] ,
                    'DicWordCloudValues1': [("Default1")]
                    }
                }

        self.DicOcr_Eng  = {
        
                'DicOcr_Eng': {
                    'DicOcr_EngName': [("Ocr_Eng")] ,
                    'DicOcr_EngValue': [("Default")]
                    }
                }

        self.DicOcr_Kor  = {
        
                'DicOcr_Kor': {
                    'DicOcr_KorName': [("Ocr_Kor")] ,
                    'DicOcr_KorValue1': [("Default")] ,
                    'DicOcr_KorValue2': [("Default")] 
                    }
                }


        self.DicAddScript  = {
        
                'DicAddScript': {
                    'DicAddScriptName': [("Script")] ,
                    'DicAddScriptValue': [("Default")]
                    }
                }

        
        ############################################################################
        ###################### 기능들에대한 딕셔너리 설정###########################
        ###########################################################################

        
        
        self.setupUI()

    
    def setupUI(self,flags=Qt.Widget):
        
        
        # 전체 화면 groupbox로 나누기 #

        # 전체화면 중앙배치 #

        ##################################
        self.resize(1300, 900)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.setWindowTitle('Term Project')
        ##################################

        # 전체화면 중앙배치 #

        self.groupBox1 = QGroupBox("기능선택")
        self.groupBox2 = QGroupBox("메인화면")
        self.groupBox3 = QGroupBox("속성창")
        self.groupBox4 = QGroupBox("스크립트창")
        self.groupBox5 = QGroupBox("콘솔창")
        self.groupBox6 = QGroupBox("선택창")
        self.groupBox7 = QGroupBox("검색창")

        # 전체 화면 groupbox로 나누기 #


           
    
        
#===============================================================기능 트리==========================================================#
        
        # 트리위젯 선언
        self.tw = QTreeWidget(self)
        # 트리위젯 기능 연결
        self.tw.itemDoubleClicked.connect(self.AddList)
        # 트리위젯 열 설정
        self.tw.setColumnCount(1)
        self.tw.setHeaderLabels(["Type"])
        # 두개 뭔지 모르겟다 #
        self.root = self.tw.invisibleRootItem()
        self.root.setChildIndicatorPolicy(True)
        # 두개 뭔지 모르겟다 #
        
        # 트리위젯에 붙일 기능들 선언 #
        self.item = QTreeWidgetItem()
        # 트리위젯에 붙일 기능들 선언 #

        # 부모 item
        self.item.setText(0, "VALUE")

        ##############################
        # 자식 item
        self.sub_item = QTreeWidgetItem()
        self.sub_item.setText(0, "Assign")
        self.item.addChild(self.sub_item)
        # 자식 item
        ##############################

        # 트리위젯에 부모 자식 둘다 붙임
        self.root.addChild(self.item)

        # 트리위젯에 붙일 기능들 선언 #
        self.item = QTreeWidgetItem()

        # 부모 item
        self.item.setText(0, "EXCEL")
        ##############################
        # 자식 item

        self.sub_item = QTreeWidgetItem()
        self.sub_item.setText(0, "ExcelRead")
        self.item.addChild(self.sub_item)
        self.sub_item = QTreeWidgetItem()
        self.sub_item.setText(0, "ExcelWrite")
        self.item.addChild(self.sub_item)

        # 자식 item
        ##############################

        # 트리위젯에 부모 자식 둘다 붙임
        self.root.addChild(self.item)


        # 트리위젯에 붙일 기능들 선언 #
        self.item = QTreeWidgetItem()
        # 트리위젯에 붙일 기능들 선언 #

        # 부모 item
        self.item.setText(0, "CSV")
        ##############################
        # 자식 item #

        self.sub_item = QTreeWidgetItem()
        self.sub_item.setText(0, "CsvRead")
        self.item.addChild(self.sub_item)
        self.sub_item = QTreeWidgetItem()
        self.sub_item.setText(0, "CsvWrite")
        self.item.addChild(self.sub_item)

        # 자식 item #
        ##############################

        # 트리위젯에 부모자식 둘다 붙임
        self.root.addChild(self.item)
        # 트리위젯에 부모자식 둘다 붙임


        # 트리위젯에 붙일 기능들 선언 #
        self.item = QTreeWidgetItem()

        ##############################
        # 자식 item

        # 부모 item
        self.item.setText(0, "MOUSE")

        self.sub_item = QTreeWidgetItem()
        self.sub_item.setText(0, "Click")
        self.item.addChild(self.sub_item)

        self.sub_item = QTreeWidgetItem()
        self.sub_item.setText(0, "MousePosition")
        self.item.addChild(self.sub_item)

        self.sub_item = QTreeWidgetItem()
        self.sub_item.setText(0, "MoveToPosition")
        self.item.addChild(self.sub_item)

        self.sub_item = QTreeWidgetItem()
        self.sub_item.setText(0, "MoveToPositionClick")
        self.item.addChild(self.sub_item)

        self.sub_item = QTreeWidgetItem()
        self.sub_item.setText(0, "MoveToPositionDoubleClick")
        self.item.addChild(self.sub_item)
        

        
        # 자식 item
        ##############################

        # 트리위젯에 부모 자식 둘다 붙임
        self.root.addChild(self.item)

        # 트리위젯에 붙일 기능들 선언 #
        self.item = QTreeWidgetItem()

        # 부모 item
        self.item.setText(0, "FOR AND WHILE")

        
        ##############################
        # 자식 item

        self.sub_item = QTreeWidgetItem()
        self.sub_item.setText(0, "For")
        self.item.addChild(self.sub_item)

        # 자식 item
        ##############################

        # 트리위젯에 부모 자식 둘다 붙임
        self.root.addChild(self.item)

        # 트리위젯에 붙일 기능들 선언 #
        self.item = QTreeWidgetItem()

        # 부모 item
        self.item.setText(0, "BROWSER")

        ##############################
        # 자식 item

        self.sub_item = QTreeWidgetItem()
        self.sub_item.setText(0, "OpenBrowser")
        self.item.addChild(self.sub_item)

        self.sub_item = QTreeWidgetItem()
        self.sub_item.setText(0, "BrowserClose")
        self.item.addChild(self.sub_item)

        self.sub_item = QTreeWidgetItem()
        self.sub_item.setText(0, "MaxWin")
        self.item.addChild(self.sub_item)

        self.sub_item = QTreeWidgetItem()
        self.sub_item.setText(0, "SwitchWin")
        self.item.addChild(self.sub_item)

        self.sub_item = QTreeWidgetItem()
        self.sub_item.setText(0, "TimeSleep")
        self.item.addChild(self.sub_item)

        self.sub_item = QTreeWidgetItem()
        self.sub_item.setText(0, "TextCrawling")
        self.item.addChild(self.sub_item)

        self.sub_item = QTreeWidgetItem()
        self.sub_item.setText(0, "ImageCrawling")
        self.item.addChild(self.sub_item)

        self.sub_item = QTreeWidgetItem()
        self.sub_item.setText(0, "InstaImageCrawling")
        self.item.addChild(self.sub_item)

        # 자식 item
        ##############################
        

        # 트리위젯에 부모 자식 둘다 붙임
        self.root.addChild(self.item)

        # 트리위젯에 붙일 기능들 선언 #
        self.item = QTreeWidgetItem()

        # 부모 item
        self.item.setText(0, "FILE")

        # 자식 item
        ##############################
        self.sub_item = QTreeWidgetItem()
        self.sub_item.setText(0, "MakeClipBoard")
        self.item.addChild(self.sub_item)
        self.root.addChild(self.item)

        self.sub_item = QTreeWidgetItem()
        self.sub_item.setText(0, "MakeFolder")
        self.item.addChild(self.sub_item)
        
        # 자식 item
        ##############################

        # 트리위젯에 부모 자식 둘다 붙임
        self.root.addChild(self.item)
        
        # 트리위젯에 붙일 기능들 선언 #
        self.item = QTreeWidgetItem()

        # 부모 item
        self.item.setText(0, "TEXT")

        # 자식 item
        ##############################

        self.sub_item = QTreeWidgetItem()
        self.sub_item.setText(0, "SetText")
        self.item.addChild(self.sub_item)

        self.sub_item = QTreeWidgetItem()
        self.sub_item.setText(0, "TypeWrite")
        self.item.addChild(self.sub_item)
        
        # 자식 item
        ##############################
        
        # 트리위젯에 부모 자식 둘다 붙임
        self.root.addChild(self.item)

        # 트리위젯에 붙일 기능들 선언 #
        self.item = QTreeWidgetItem()

        # 부모 item
        self.item.setText(0, "KEYBOARD")

        # 자식 item
        ##############################

        self.sub_item = QTreeWidgetItem()
        self.sub_item.setText(0, "PageDown")
        self.item.addChild(self.sub_item)

        self.sub_item = QTreeWidgetItem()
        self.sub_item.setText(0, "Enter")
        self.item.addChild(self.sub_item)

        # 자식 item
        ##############################
        
        # 트리위젯에 부모 자식 둘다 붙임
        self.root.addChild(self.item)
        
        # 트리위젯에 붙일 기능들 선언 #
        self.item = QTreeWidgetItem()

        # 부모 item
        self.item.setText(0, "AI")

        # 자식 item
        ##############################

        self.sub_item = QTreeWidgetItem()
        self.sub_item.setText(0, "Ocr_Eng")
        self.item.addChild(self.sub_item)

        self.sub_item = QTreeWidgetItem()
        self.sub_item.setText(0, "Ocr_Kor")
        self.item.addChild(self.sub_item)

        # 자식 item
        ##############################

        # 트리위젯에 부모 자식 둘다 붙임
        self.root.addChild(self.item)

        # 트리위젯에 붙일 기능들 선언 #
        self.item_main = QTreeWidgetItem()
        self.item_1 = QTreeWidgetItem()
        self.item_2 = QTreeWidgetItem()
        
        # 부모 item
        self.item_main.setText(0, "PROCESSING")
        self.item_1.setText(0, "TEXT_PROCESSING")
        self.item_2.setText(0, "IMG_PROCESSING")

        # 자식 item_1
        ##############################

        self.sub_item_1 = QTreeWidgetItem()
        self.sub_item_1.setText(0, "Filter_Content")
        self.item_1.addChild(self.sub_item_1)

        self.sub_item_1 = QTreeWidgetItem()
        self.sub_item_1.setText(0, "Morphs")
        self.item_1.addChild(self.sub_item_1)

        self.sub_item_1 = QTreeWidgetItem()
        self.sub_item_1.setText(0, "Extract_Word")
        self.item_1.addChild(self.sub_item_1)

        self.sub_item_1 = QTreeWidgetItem()
        self.sub_item_1.setText(0, "Counter_Word")
        self.item_1.addChild(self.sub_item_1)

        self.sub_item_1 = QTreeWidgetItem()
        self.sub_item_1.setText(0, "WordCloud")
        self.item_1.addChild(self.sub_item_1)

        self.sub_item_1 = QTreeWidgetItem()
        self.sub_item_1.setText(0, "RowDropNa")
        self.item_1.addChild(self.sub_item_1)

        self.sub_item_1 = QTreeWidgetItem()
        self.sub_item_1.setText(0, "ColumnDropNa")
        self.item_1.addChild(self.sub_item_1)

        self.sub_item_1 = QTreeWidgetItem()
        self.sub_item_1.setText(0, "FillNa")
        self.item_1.addChild(self.sub_item_1)

        
        # 자식 item_1
        ##############################



        # 자식 item_2
        ##############################

        self.sub_item_2 = QTreeWidgetItem()
        self.sub_item_2.setText(0, "Resize")
        self.item_2.addChild(self.sub_item_2)

        self.sub_item_2 = QTreeWidgetItem()
        self.sub_item_2.setText(0, "ConvertGray")
        self.item_2.addChild(self.sub_item_2)

        self.sub_item_2 = QTreeWidgetItem()
        self.sub_item_2.setText(0, "ImgSquare")
        self.item_2.addChild(self.sub_item_2)

        self.sub_item_2 = QTreeWidgetItem()
        self.sub_item_2.setText(0, "ThresHolding")
        self.item_2.addChild(self.sub_item_2)

        self.sub_item_2 = QTreeWidgetItem()
        self.sub_item_2.setText(0, "EqualizeHist")
        self.item_2.addChild(self.sub_item_2)

        self.sub_item_2 = QTreeWidgetItem()
        self.sub_item_2.setText(0, "ColorEqualizeHist")
        self.item_2.addChild(self.sub_item_2)

        self.sub_item_2 = QTreeWidgetItem()
        self.sub_item_2.setText(0, "Blur")
        self.item_2.addChild(self.sub_item_2)

        self.sub_item_2 = QTreeWidgetItem()
        self.sub_item_2.setText(0, "Blur_2D")
        self.item_2.addChild(self.sub_item_2)

        self.sub_item_2 = QTreeWidgetItem()
        self.sub_item_2.setText(0, "GausianBlur")
        self.item_2.addChild(self.sub_item_2)

        self.sub_item_2 = QTreeWidgetItem()
        self.sub_item_2.setText(0, "MedianBlur")
        self.item_2.addChild(self.sub_item_2)

        self.sub_item_2 = QTreeWidgetItem()
        self.sub_item_2.setText(0, "BilateralBlur")
        self.item_2.addChild(self.sub_item_2)

        # 자식 item_2
        ##############################
        self.item_main.addChild(self.item_1)
        self.item_main.addChild(self.item_2)
        self.root.addChild(self.item_main)
        # 트리위젯에 부모 자식 둘다 붙임

        



        

        

        

        
       

        

    
        
        

#===============================================================기능 트리==========================================================#



#===============================================================레이아웃==========================================================#
        
        # 위젯을 붙이기 위한 레이아웃 만들기
        self.vb1 = QVBoxLayout()
        self.vb7 = QHBoxLayout()
        
        # 검색창 설정
        self.tslb = QLineEdit("검색 키워드를 입력해 주세요 !")
        # 검색결과 창 설정
        self.tmplist = QListWidget()
        self.tmplist.setFixedSize(410,65)
        # 사이즈 설정
        self.groupBox7.setFixedHeight(56)
        # 검색창 붙이기
        self.vb7.addWidget(self.tslb)
        # 검색결과 붙이기
        self.vb1.addWidget(self.tmplist)
        # 트리구조 붙이기
        self.vb1.addWidget(self.tw)
        # 검색창 레이아웃 설정
        self.groupBox7.setLayout(self.vb7)
        # 트리구조 레이아웃 설정
        self.groupBox1.setLayout(self.vb1)
        # 메인리스트 설정
        self.te_1 = QListWidget(self)
        # 메인리스트 움직일수 있게 설정
        self.te_1.setDragDropMode(QListWidget.InternalMove)
        
        # 스플릿트 삭제할 예정
        self.split_1 = QSplitter()
        self.te_1.setAlternatingRowColors(True)
        # 스플릿트에 메인리스트 붙이기
        self.split_1.addWidget(self.te_1)
        # 메인리스트 수직구조 설정
        self.split_1.setOrientation(Qt.Vertical)
        # 위젯을 붙이기 위한 레이아웃 만들기
        self.vb2 = QVBoxLayout()
        # 레이아웃에 메인리스트 붙이기
        self.vb2.addWidget(self.split_1)
        # 메인리스트 레이아웃 설정
        self.groupBox2.setLayout(self.vb2)
        
        # 위젯을 붙이기 위한 레이아웃 만들기
        self.vb3 = QVBoxLayout()
        # 속성창 만들기
        self.table=QTableWidget()
        # 속성창 열 지정
        self.table.setColumnCount(1)
        # 속성창 행 지정
        self.table.setRowCount(7)
        # 속성창 스크롤바 설정
        self.table.setHorizontalScrollMode(True)
        # 속성창 헤더 부분설정
        self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
        self.table.setVerticalHeaderLabels(['NAME','VALUES 1','VALUES 2','VALUES 3','VALUES 4','VALUES 5','VALUES 6'])

        # 행 사이즈 설정
        self.table.setRowHeight(0,53)
        self.table.setRowHeight(1,53)
        self.table.setRowHeight(2,53)
        self.table.setRowHeight(3,53)
        self.table.setRowHeight(4,53)
        self.table.setRowHeight(5,53)
        self.table.setRowHeight(6,53)

        # 열 사이즈 설정
        self.table.setColumnWidth(0,322.5)
        self.table.setColumnWidth(1,322.5)
        self.table.setColumnWidth(2,322.5)
        self.table.setColumnWidth(3,322.5)
        self.table.setColumnWidth(4,322.5)
        self.table.setColumnWidth(5,322.5)
        self.table.setColumnWidth(6,322.5)

        # 속성창 테이블 레이아웃에 붙이기
        self.vb3.addWidget(self.table)
        
        # 속성 창 사이즈 조절
        self.groupBox3.setLayout(self.vb3)
        self.groupBox3.setFixedSize(440,430.5)

        
        
        
        
        #===========================================================================================================#
        # 스크립트 및 터미널 탭 레이아웃 설정 #    

        # 스크립트 창 tab 만들기
        self.tabs1 = QTabWidget()
        # 스크립트 창 tab에 붙일 tab 만들기
        self.tab1 = QWidget()
        # 레이아웃 만들기
        vb8 = QVBoxLayout()
        # 탭에 붙일 텍스트 창 만들기
        self.Py_Text = QTextEdit()
        # 레이아웃에 텍스트 창 붙이기
        vb8.addWidget(self.Py_Text)
        # 레이아웃 만들기
        vb9 = QVBoxLayout()
        # 레이아웃에 텍스트 창 붙이기
        vb9.addWidget(QTextEdit())
        # 스크립트 창 레이아웃 설정
        self.tab1.setLayout(vb8)
        # 스크립트 창 붙이기
        self.tabs1.addTab(self.tab1, "Python Code")

        # 레이아웃 설정
        self.vb4 = QVBoxLayout()
        # 레이아웃에 위젯 붙이기
        self.vb4.addWidget(self.tabs1)
        # groupbox 레이아웃 전체 설정
        self.groupBox4.setLayout(self.vb4)

        
        
        # 터미널 및 problem창 탭 만들기
        self.tabs2 = QTabWidget()
        # 붙일 탭 위젯 만들기
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        # 탭 붙이기
        self.tabs2.addTab(self.tab2, "Terminal")
        self.tabs2.addTab(self.tab1, "Problem")
        
        # 레이아웃 설정
        vb10 = QVBoxLayout()
        # problem textedit창 만들기
        self.P_text = QTextEdit()
        # 레이아웃에 Textedit창 붙이기
        vb10.addWidget(self.P_text)
        # 탭 레이아웃 설정
        self.tab1.setLayout(vb10)
        # 레이아웃 만들기
        vb11 = QVBoxLayout()
        # 터미널 텍스트 창 만들기
        self.T_text = QTextEdit()
        # 텍스트 창 레이아웃에 붙이기
        vb11.addWidget(self.T_text)
        # 탭 레이아웃 설정
        self.tab2.setLayout(vb11)

        # 디버깅 부분 삭제할 예정
        vb12 = QVBoxLayout()
        self.D_Text = QTextEdit()
        vb12.addWidget(self.D_Text)
        # 디버깅 부분 삭제할 예정
        
        # 터미널 및 problem 창 레이아웃에 붙이기
        self.vb5 = QVBoxLayout()
        self.vb5.addWidget(self.tabs2)
        self.groupBox5.setLayout(self.vb5)


        # 스크립트 및 터미널 탭 레이아웃 설정 #
        #===========================================================================================================#

        #===========================================================================================================#

        # 기능선택 아이콘 및 레이아웃 설정 #
        self.vb6 = QGridLayout()
        
        self.btn1 = QPushButton("up",self) # up
        self.btn2 = QPushButton("start",self) # start
        self.btn3 = QPushButton("down",self) # down
        self.btn4 = QPushButton("save",self) # save
        self.btn5 = QPushButton("attedit",self)  # attedit
        self.btn6 = QPushButton("loading",self) # loading
        self.btn7 = QPushButton("remove",self) # remove
        self.btn8 = QPushButton("addscript",self) # addscript
        self.btn9 = QPushButton("removeall",self)  # removeall

        # 아이콘 넣기
        self.btn1.setIcon(QIcon(r'C:\Users\PC\Desktop\Capstion\툴 이미지\up\KakaoTalk_20200624_233308566.png')) # 수정요망
        self.btn2.setIcon(QIcon(r'C:\Users\PC\Desktop\Capstion\툴 이미지\start\start-png-44878.png'))
        self.btn3.setIcon(QIcon(r'C:\Users\PC\Desktop\Capstion\툴 이미지\down\KakaoTalk_20200624_233309755.png')) # 수정요망
        self.btn4.setIcon(QIcon(r'C:\Users\PC\Desktop\Capstion\툴 이미지\save\save-icon-36514.png'))
        self.btn5.setIcon(QIcon(r'C:\Users\PC\Desktop\Capstion\툴 이미지\attedit\gear-icon-png-2242.png'))
        self.btn6.setIcon(QIcon(r'C:\Users\PC\Desktop\Capstion\툴 이미지\load\load.png'))
        self.btn7.setIcon(QIcon(r'C:\Users\PC\Desktop\Capstion\툴 이미지\remove\kisspng-computer-icons-rubbish-bins-waste-paper-baskets-trash-can-5ad2a84d45eed1.7397870915237550852865.png'))
        self.btn8.setIcon(QIcon(r'C:\Users\PC\Desktop\Capstion\툴 이미지\addscript\script.png'))
        self.btn9.setIcon(QIcon(r'C:\Users\PC\Desktop\Capstion\툴 이미지\removeall\red-bin-png-1.png'))
        

        # 버튼 레이아웃에 붙이기
        self.vb6.addWidget(self.btn1,0,0)
        self.vb6.addWidget(self.btn2,0,1)
        self.vb6.addWidget(self.btn3,0,2)
        self.vb6.addWidget(self.btn4,1,0)
        self.vb6.addWidget(self.btn5,1,1)
        self.vb6.addWidget(self.btn6,1,2)
        self.vb6.addWidget(self.btn7,2,0)
        self.vb6.addWidget(self.btn8,2,1)
        self.vb6.addWidget(self.btn9,2,2)  
        
        # 선택창 레이아웃 설정
        self.groupBox6.setLayout(self.vb6)

        # 버튼 기능 연결
        self.btn1.clicked.connect(self.Up)
        self.btn2.clicked.connect(self.Start)
        self.btn3.clicked.connect(self.Down) 
        self.btn4.clicked.connect(self.FileSave)
        self.btn5.clicked.connect(self.AttEdit)
        self.btn6.clicked.connect(self.FileLoad)
        self.btn7.clicked.connect(self.RemoveList)
        self.btn8.clicked.connect(self.AddScript)
        self.btn9.clicked.connect(self.RemoveListAll)

        # 검색 , 속성값 보기 기능 연결
        self.tslb.textChanged.connect(self.Search)
        self.tmplist.doubleClicked.connect(self.add_search)
        self.te_1.clicked.connect(self.AttView)

        # 기능선택 아이콘 및 레이아웃 설정 #
        
       #===========================================================================================================#
    


       ##########################################
       ############전체 레이아웃 설정#############
       ###########################################

        self.layout = QVBoxLayout()

        # 왼쪽 레이아웃
        self.leftLayOut = QVBoxLayout()
        self.leftLayOut.addWidget(self.groupBox7)
        self.leftLayOut.addWidget(self.groupBox1)
        
        
        # 중앙 레이아웃
        self.middleLayOut = QVBoxLayout()
        self.middleLayOut.addWidget(self.groupBox2)
        self.middleLayOut.addWidget(self.groupBox6)
        self.middleLayOut.addWidget(self.groupBox5)
        
        # 오른쪽 레이아웃
        self.rightLayOut = QVBoxLayout()
        self.rightLayOut.addWidget(self.groupBox3)
        self.rightLayOut.addWidget(self.groupBox4)

        # 전체 레이아웃
        layout = QHBoxLayout()
        layout.addLayout(self.leftLayOut)
        layout.addLayout(self.middleLayOut)
        layout.addLayout(self.rightLayOut)
        
        self.setLayout(layout)

        ##########################################
       ############전체 레이아웃 설정#############
       ###########################################

#===============================================================레이아웃==========================================================#

#=============================================================def 함수 정의==========================================================#
    
    ##########################################################
    ########### 트리구조에서 더블클릭시 발생하는 함수 #########
    # 위에 선언한 기본 딕셔너리의 기본값이 self.obls에 들어감 #
    ##########################################################

    @pyqtSlot(QTreeWidgetItem, int)

    def AddList(self,it, col):
        
        a = it.text(col)
        self.te_1.addItem(a)
        
        if a == 'OpenBrowser' :

            test1 = self.DicOpenBrowser['DicOpenBrowser']['DicOpenBrowserName'][0]
            test2 = self.DicOpenBrowser['DicOpenBrowser']['DicOpenBrowserUrl'][0]
            
            
            self.ObLs.append([test1,test2])

        elif a == 'ImageCrawling' :
            
            test1 = self.DicImageCrawling['DicImageCrawling']['DicImageCrawlingName'][0]
            test2 = self.DicImageCrawling['DicImageCrawling']['DicImageCrawlingValues1'][0]
            test3 = self.DicImageCrawling['DicImageCrawling']['DicImageCrawlingValues2'][0]
            test4 = self.DicImageCrawling['DicImageCrawling']['DicImageCrawlingValues3'][0]
            test5 = self.DicImageCrawling['DicImageCrawling']['DicImageCrawlingValues4'][0]
            
            self.ObLs.append([test1,test2,test3,test4,test5])
        
        elif a == 'InstaImageCrawling' :
            
            test1 = self.DicInstaImageCrawling['DicInstaImageCrawling']['DicInstaImageCrawlingName'][0]
            test2 = self.DicInstaImageCrawling['DicInstaImageCrawling']['DicInstaImageCrawlingValues1'][0]
            test3 = self.DicInstaImageCrawling['DicInstaImageCrawling']['DicInstaImageCrawlingValues2'][0]
            
            self.ObLs.append([test1,test2,test3])


        elif a == 'MakeFolder' :

            test1 = self.DicMakeFolder['DicMakeFolder']['DicMakeFolderName'][0]
            test2 = self.DicMakeFolder['DicMakeFolder']['DicMakeFolderValue'][0]
            
            
            self.ObLs.append([test1,test2])
    

        elif a == 'PageDown' :

            test1 = self.DicPageDown['DicPageDown']['DicPageDownName'][0]
            test2 = self.DicPageDown['DicPageDown']['DicPageDownTag'][0]
            test3 = self.DicPageDown['DicPageDown']['DicPageDownCount'][0]
            
            self.ObLs.append([test1,test2,test3])
        
        elif a == 'Enter' :

            test1 = self.DicEnter['DicEnter']['DicEnterName'][0]
            test2 = self.DicEnter['DicEnter']['DicEnterValue'][0]
            
            self.ObLs.append([test1,test2])
        

        elif a == 'ImgSquare' :

            test1 = self.DicImgSquare['DicImgSquare']['DicImgSquareName'][0]
            test2 = self.DicImgSquare['DicImgSquare']['DicImgSquareValues1'][0]
            test3 = self.DicImgSquare['DicImgSquare']['DicImgSquareValues2'][0]
            
            
            self.ObLs.append([test1,test2,test3])

            
        elif a == 'BrowserClose' :

            test1 = self.DicBrowserClose['DicBrowserClose']['DicBrowserCloseName'][0]
            test2 = self.DicBrowserClose['DicBrowserClose']['DicBrowserCloseValue'][0]
            
            
            self.ObLs.append([test1,test2])


        
        elif a == 'Assign' :

            test1 = self.DicAssign['DicAssign']['DicAssignName'][0]
            test2 = self.DicAssign['DicAssign']['DicAssignValueName'][0]
            test3 = self.DicAssign['DicAssign']['DicAssignValueVariable'][0]
            
            
            self.ObLs.append([test1,test2,test3])

            

        
        elif a == 'SetText' :

            test1 = self.DicSetText['DicSetText']['DicSetTextName'][0]
            test2 = self.DicSetText['DicSetText']['DicSetTextValues1'][0]
            test3 = self.DicSetText['DicSetText']['DicSetTextValues2'][0]
            
            
            self.ObLs.append([test1,test2,test3])
        
        elif a == 'TypeWrite' :

            test1 = self.DicTypeWrite['DicTypeWrite']['DicTypeWriteName'][0]
            test2 = self.DicTypeWrite['DicTypeWrite']['DicTypeWriteValue'][0]
          
            
            self.ObLs.append([test1,test2])


        elif a == 'For' :

            test1 = self.DicFor['DicFor']['DicForName'][0]
            test2 = self.DicFor['DicFor']['DicForValues1'][0]
            test3 = self.DicFor['DicFor']['DicForValues2'][0]
            test4 = self.DicFor['DicFor']['DicForValues3'][0]
            
            
            self.ObLs.append([test1,test2,test3,test4])



        elif a == 'TextCrawling' :

            test1 = self.DicTextCrawling['DicTextCrawling']['DicTextCrawlingName'][0]
            test2 = self.DicTextCrawling['DicTextCrawling']['DicTextCrawlingValues1'][0]
            test3 = self.DicTextCrawling['DicTextCrawling']['DicTextCrawlingValues2'][0]
            test4 = self.DicTextCrawling['DicTextCrawling']['DicTextCrawlingValues3'][0]
            test5 = self.DicTextCrawling['DicTextCrawling']['DicTextCrawlingValues4'][0]
            test6 = self.DicTextCrawling['DicTextCrawling']['DicTextCrawlingValues5'][0]
            test7 = self.DicTextCrawling['DicTextCrawling']['DicTextCrawlingValues6'][0]
            
            
            self.ObLs.append([test1,test2,test3,test4,test5,test6,test7])

            print(self.ObLs)


        
        elif a == 'ExcelRead' :

            test1 = self.DicExcelRead['DicExcelRead']['DicExcelReadName'][0]
            test2 = self.DicExcelRead['DicExcelRead']['DicExcelReadValues1'][0]
            test3 = self.DicExcelRead['DicExcelRead']['DicExcelReadValues2'][0]
            
            self.ObLs.append([test1,test2,test3])
        
        elif a == 'ExcelWrite' :

            test1 = self.DicExcelWrite['DicExcelWrite']['DicExcelWriteName'][0]
            test2 = self.DicExcelWrite['DicExcelWrite']['DicExcelWriteValues1'][0]
            test3 = self.DicExcelWrite['DicExcelWrite']['DicExcelWriteValues2'][0]
            test4 = self.DicExcelWrite['DicExcelWrite']['DicExcelWriteValues3'][0]
           
            
            self.ObLs.append([test1,test2,test3,test4])
        
        elif a == 'RowDropNa' :

            test1 = self.DicRowDropNa['DicRowDropNa']['DicRowDropNaName'][0]
            test2 = self.DicRowDropNa['DicRowDropNa']['DicRowDropNaValue'][0]
            
            self.ObLs.append([test1,test2])
        
        elif a == 'ColumnDropNa' :

            test1 = self.DicColumnDropNa['DicColumnDropNa']['DicColumnDropNaName'][0]
            test2 = self.DicColumnDropNa['DicColumnDropNa']['DicColumnDropNaValue'][0]
            
            self.ObLs.append([test1,test2])
        
        elif a == 'FillNa' :

            test1 = self.DicFillNa['DicFillNa']['DicFillNaName'][0]
            test2 = self.DicFillNa['DicFillNa']['DicFillNaValues1'][0]
            test3 = self.DicFillNa['DicFillNa']['DicFillNaValues2'][0]
            
            self.ObLs.append([test1,test2,test3])
        

        elif a == 'CsvRead' :

            test1 = self.DicCsvRead['DicCsvRead']['DicCsvReadName'][0]
            test2 = self.DicCsvRead['DicCsvRead']['DicCsvReadValues1'][0]
            test3 = self.DicCsvRead['DicCsvRead']['DicCsvReadValues2'][0]
            
            self.ObLs.append([test1,test2,test3])

        
        elif a == 'CsvWrite' :

            test1 = self.DicCsvWrite['DicCsvWrite']['DicCsvWriteName'][0]
            test2 = self.DicCsvWrite['DicCsvWrite']['DicCsvWriteValues1'][0]
            test3 = self.DicCsvWrite['DicCsvWrite']['DicCsvWriteValues2'][0]
            test4 = self.DicCsvWrite['DicCsvWrite']['DicCsvWriteValues3'][0]
           
            
            
            self.ObLs.append([test1,test2,test3,test4])    


        elif a == 'MaxWin' :

            test1 = self.DicMaxWin['DicMaxWin']['DicMaxWinName'][0]
            test2 = self.DicMaxWin['DicMaxWin']['DicMaxWinValue'][0]
           
            
            self.ObLs.append([test1,test2])

        elif a == 'SwitchWin' :

            test1 = self.DicSwitchWin['DicSwitchWin']['DicSwitchWinName'][0]
            test2 = self.DicSwitchWin['DicSwitchWin']['DicSwitchWinValue'][0]
           
            
            self.ObLs.append([test1,test2])


        
        elif a == 'TimeSleep' :

            test1 = self.DicTimeSleep['DicTimeSleep']['DicTimeSleepName'][0]
            test2 = self.DicTimeSleep['DicTimeSleep']['DicTimeSleepValue'][0]
           
            
            self.ObLs.append([test1,test2])




        elif a == 'Click' :

            test1 = self.DicClick['DicClick']['DicClickName'][0]
            test2 = self.DicClick['DicClick']['DicClickValue'][0]
            
            
            self.ObLs.append([test1,test2])

        elif a == 'MousePosition' :

            test1 = self.DicMousePosition['DicMousePosition']['DicMousePositionName'][0]
            test2 = self.DicMousePosition['DicMousePosition']['DicMousePositionValue'][0]
            
            
            self.ObLs.append([test1,test2])

        elif a == 'MoveToPosition' :

            test1 = self.DicMoveToPosition['DicMoveToPosition']['DicMoveToPositionName'][0]
            test2 = self.DicMoveToPosition['DicMoveToPosition']['DicMoveToPositionValues1'][0]
            test3 = self.DicMoveToPosition['DicMoveToPosition']['DicMoveToPositionValues2'][0]
            
            
            self.ObLs.append([test1,test2,test3])
        
        elif a == 'MoveToPositionClick' :

            test1 = self.DicMoveToPositionClick['DicMoveToPositionClick']['DicMoveToPositionClickName'][0]
            test2 = self.DicMoveToPositionClick['DicMoveToPositionClick']['DicMoveToPositionClickValues1'][0]
            test3 = self.DicMoveToPositionClick['DicMoveToPositionClick']['DicMoveToPositionClickValues2'][0]
            
            
            self.ObLs.append([test1,test2,test3])
        

        elif a == 'MoveToPositionDoubleClick' :

            test1 = self.DicMoveToPositionDoubleClick['DicMoveToPositionDoubleClick']['DicMoveToPositionDoubleClickName'][0]
            test2 = self.DicMoveToPositionDoubleClick['DicMoveToPositionDoubleClick']['DicMoveToPositionDoubleClickValues1'][0]
            test3 = self.DicMoveToPositionDoubleClick['DicMoveToPositionDoubleClick']['DicMoveToPositionDoubleClickValues2'][0]
            
            
            self.ObLs.append([test1,test2,test3])
            


        elif a == 'MakeClipBoard':

            test1 = self.DicMakeClipBoard['DicMakeClipBoard']['DicMakeClipBoardName'][0]
            test2 = self.DicMakeClipBoard['DicMakeClipBoard']['DicMakeClipBoardValues1'][0]
            test3 = self.DicMakeClipBoard['DicMakeClipBoard']['DicMakeClipBoardValues2'][0]
            test4 = self.DicMakeClipBoard['DicMakeClipBoard']['DicMakeClipBoardValues3'][0]

           
            self.ObLs.append([test1,test2,test3,test4])



        elif a == 'Resize':

            test1 = self.DicResize['DicResize']['DicResizeName'][0]
            test2 = self.DicResize['DicResize']['DicResizeValues1'][0]
            test3 = self.DicResize['DicResize']['DicResizeValues2'][0]
            test4 = self.DicResize['DicResize']['DicResizeValues3'][0]
            test5 = self.DicResize['DicResize']['DicResizeValues4'][0]

            self.ObLs.append([test1,test2,test3,test4,test5])


        elif a == 'ConvertGray':

            test1 = self.DicConvertGray['DicConvertGray']['DicConvertGrayName'][0]
            test2 = self.DicConvertGray['DicConvertGray']['DicConvertGrayValues1'][0]
            test3 = self.DicConvertGray['DicConvertGray']['DicConvertGrayValues1'][0]

            self.ObLs.append([test1,test2,test3])


        
        elif a == 'ThresHolding':

            test1 = self.DicThresHolding['DicThresHolding']['DicThresHoldingName'][0]
            test2 = self.DicThresHolding['DicThresHolding']['DicThresHoldingValues1'][0]
            test3 = self.DicThresHolding['DicThresHolding']['DicThresHoldingValues2'][0]

            self.ObLs.append([test1,test2,test3])

        
        elif a == 'EqualizeHist':

            test1 = self.DicEqualizeHist['DicEqualizeHist']['DicEqualizeHistName'][0]
            test2 = self.DicEqualizeHist['DicEqualizeHist']['DicEqualizeHistValues1'][0]
            test3 = self.DicEqualizeHist['DicEqualizeHist']['DicEqualizeHistValues2'][0]

            self.ObLs.append([test1,test2,test3])

        
        elif a == 'ColorEqualizeHist':

            test1 = self.DicColorEqualizeHist['DicColorEqualizeHist']['DicColorEqualizeHistName'][0]
            test2 = self.DicColorEqualizeHist['DicColorEqualizeHist']['DicColorEqualizeHistValues1'][0]
            test3 = self.DicColorEqualizeHist['DicColorEqualizeHist']['DicColorEqualizeHistValues2'][0]

            self.ObLs.append([test1,test2,test3])

        
        elif a == 'Blur':

            test1 = self.DicBlur['DicBlur']['DicBlurName'][0]
            test2 = self.DicBlur['DicBlur']['DicBlurValues1'][0]
            test3 = self.DicBlur['DicBlur']['DicBlurValues2'][0]
            test4 = self.DicBlur['DicBlur']['DicBlurValues3'][0]
            test5 = self.DicBlur['DicBlur']['DicBlurValues4'][0]

            self.ObLs.append([test1,test2,test3,test4,test5])

        elif a == 'Blur_2D':

            test1 = self.Dic2DBlur['Dic2DBlur']['Dic2DBlurName'][0]
            test2 = self.Dic2DBlur['Dic2DBlur']['Dic2DBlurValues1'][0]
            test3 = self.Dic2DBlur['Dic2DBlur']['Dic2DBlurValues2'][0]
            test4 = self.Dic2DBlur['Dic2DBlur']['Dic2DBlurValues3'][0]
            

            self.ObLs.append([test1,test2,test3,test4])

        elif a == 'GausianBlur':

            test1 = self.DicGausianBlur['DicGausianBlur']['DicGausianBlurName'][0]
            test2 = self.DicGausianBlur['DicGausianBlur']['DicGausianBlurValues1'][0]
            test3 = self.DicGausianBlur['DicGausianBlur']['DicGausianBlurValues2'][0]
            test4 = self.DicGausianBlur['DicGausianBlur']['DicGausianBlurValues3'][0]
            test5 = self.DicGausianBlur['DicGausianBlur']['DicGausianBlurValues4'][0]
            test6 = self.DicGausianBlur['DicGausianBlur']['DicGausianBlurValues5'][0]
            

            self.ObLs.append([test1,test2,test3,test4,test5,test6])

        elif a == 'MedianBlur':

            test1 = self.DicMedianBlur['DicMedianBlur']['DicMedianBlurName'][0]
            test2 = self.DicMedianBlur['DicMedianBlur']['DicMedianBlurValues1'][0]
            test3 = self.DicMedianBlur['DicMedianBlur']['DicMedianBlurValues2'][0]
            test4 = self.DicMedianBlur['DicMedianBlur']['DicMedianBlurValues3'][0]
           

            self.ObLs.append([test1,test2,test3,test4])

        elif a == 'BilateralBlur':

            test1 = self.DicBilateralBlur['DicBilateralBlur']['DicBilateralBlurName'][0]
            test2 = self.DicBilateralBlur['DicBilateralBlur']['DicBilateralBlurValues1'][0]
            test3 = self.DicBilateralBlur['DicBilateralBlur']['DicBilateralBlurValues2'][0]
            test4 = self.DicBilateralBlur['DicBilateralBlur']['DicBilateralBlurValues3'][0]
            test5 = self.DicBilateralBlur['DicBilateralBlur']['DicBilateralBlurValues4'][0]
            test6 = self.DicBilateralBlur['DicBilateralBlur']['DicBilateralBlurValues5'][0]
           
            self.ObLs.append([test1,test2,test3,test4,test5,test6])

        elif a == 'Filter_Content':

            test1 = self.DicFilter_Content['DicFilter_Content']['DicFilter_ContentName'][0]
            test2 = self.DicFilter_Content['DicFilter_Content']['DicFilter_ContentValues1'][0]
            test3 = self.DicFilter_Content['DicFilter_Content']['DicFilter_ContentValues2'][0]
            
            self.ObLs.append([test1,test2,test3])

        elif a == 'Morphs':

            test1 = self.DicMorphs['DicMorphs']['DicMorphsName'][0]
            test2 = self.DicMorphs['DicMorphs']['DicMorphsValues1'][0]
            test3 = self.DicMorphs['DicMorphs']['DicMorphsValues2'][0]
            
            self.ObLs.append([test1,test2,test3])

        elif a == 'Extract_Word':

            test1 = self.DicExtract_Word['DicExtract_Word']['DicExtract_WordName'][0]
            test2 = self.DicExtract_Word['DicExtract_Word']['DicExtract_WordValues1'][0]
            test3 = self.DicExtract_Word['DicExtract_Word']['DicExtract_WordValues2'][0]
            
            self.ObLs.append([test1,test2,test3])

        elif a == 'Counter_Word':

            test1 = self.DicCounter_Word['DicCounter_Word']['DicCounter_WordName'][0]
            test2 = self.DicCounter_Word['DicCounter_Word']['DicCounter_WordValues1'][0]
            test3 = self.DicCounter_Word['DicCounter_Word']['DicCounter_WordValues2'][0]
            
            self.ObLs.append([test1,test2,test3])
        
        elif a == 'WordCloud':

            test1 = self.DicWordCloud['DicWordCloud']['DicWordCloudName'][0]
            test2 = self.DicWordCloud['DicWordCloud']['DicWordCloudValues1'][0]
            
            
            self.ObLs.append([test1,test2])
    
  
        elif a == 'Ocr_Eng':

            test1 = self.DicOcr_Eng['DicOcr_Eng']['DicOcr_EngName'][0]
            test2 = self.DicOcr_Eng['DicOcr_Eng']['DicOcr_EngValue'][0]

            self.ObLs.append([test1,test2])


        elif a == 'Ocr_Kor':

            test1 = self.DicOcr_Kor['DicOcr_Kor']['DicOcr_KorName'][0]
            test2 = self.DicOcr_Kor['DicOcr_Kor']['DicOcr_KorValue1'][0]
            test3 = self.DicOcr_Kor['DicOcr_Kor']['DicOcr_KorValue2'][0]

            self.ObLs.append([test1,test2,test3])


        
    ##########################################################################
    # 메인리스트 항목 클리시 오른쪽 속성창에 현제 들어가 있는 인자값들을 보여줌#
    ##########################################################################

    def AttView(self) :


        i = self.te_1.currentRow()
        print(i)

   

        if self.ObLs[i][0] == 'OpenBrowser' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','URL','','','','',''])


            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])

            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)


        elif self.ObLs[i][0] == 'MakeFolder' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','PATH','','','','',''])


            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])

            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)



        elif self.ObLs[i][0] == 'PageDown' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','TAG','COUNT','','','',''])


            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])

            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)

        
        elif self.ObLs[i][0] == 'Enter' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','DeFault','','','','',''])


            test1 = QTableWidgetItem(self.ObLs[i][0])

            test1.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(0, 0,test1)
            

        
        





        elif self.ObLs[i][0] == 'BrowserClose' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','NOT VALUE','','','','',''])


            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])

            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)


        elif self.ObLs[i][0] == 'SwitchWin' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','VALUE','','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])

            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)


        elif self.ObLs[i][0] == 'Assign' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','ValueName','ValueVariable','','','',''])


            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])

            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)

            try :

                if type(self.ObLs[i][2]) == list :
                    
                    test4 = QTableWidgetItem(' list 형식의 값입니다. ')
                    test4.setTextAlignment(Qt.AlignCenter)

                    self.table.setItem(0,2,test4)

                else:

                    test3 = QTableWidgetItem(self.ObLs[i][2])
                    test3.setTextAlignment(Qt.AlignCenter)
                    print(type(test3))

                    self.table.setItem(0, 2,test3)
            
            except:

                print('예외 처리 부분입니다.')
           

            

        elif self.ObLs[i][0] == 'TextCrawling' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','HTML1','HTML2','HTML3','HTML4','HTML5','RESULT'])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])
            test4 = QTableWidgetItem(self.ObLs[i][3])
            test5 = QTableWidgetItem(self.ObLs[i][4])
            test6 = QTableWidgetItem(self.ObLs[i][5])
            test7 = QTableWidgetItem(self.ObLs[i][6])

            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)
            test4.setTextAlignment(Qt.AlignCenter)
            test5.setTextAlignment(Qt.AlignCenter)
            test6.setTextAlignment(Qt.AlignCenter)
            test7.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)
            self.table.setItem(0, 3,test4)
            self.table.setItem(0, 4,test5)
            self.table.setItem(0, 5,test6)
            self.table.setItem(0, 6,test7)

        
        elif self.ObLs[i][0] == 'ImageCrawling' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','HTML1','HTML2','LOCATION','TYPE','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])
            test4 = QTableWidgetItem(self.ObLs[i][3])
            test5 = QTableWidgetItem(self.ObLs[i][4])
           

            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)
            test4.setTextAlignment(Qt.AlignCenter)
            test5.setTextAlignment(Qt.AlignCenter)
            

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)
            self.table.setItem(0, 3,test4)
            self.table.setItem(0, 4,test5)

        elif self.ObLs[i][0] == 'InstaImageCrawling' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','LOCATION','TYPE','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])
           
            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)
          
            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)


        elif self.ObLs[i][0] == 'ExcelWrite' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','RESULT','COLUMN','LOCATION','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])
            test4 = QTableWidgetItem(self.ObLs[i][3])
            
            

            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)
            test4.setTextAlignment(Qt.AlignCenter)
            
            

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)
            self.table.setItem(0, 3,test4)


        elif self.ObLs[i][0] == 'ExcelRead' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','LOCATION','RESULT','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])
           
            
            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)
            

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)
        
        elif self.ObLs[i][0] == 'RowDropNa' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','Default','','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
           
           
            
            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            
            

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
        
        elif self.ObLs[i][0] == 'ColumnDropNa' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','Default','','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
           
           
            
            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            
            

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
        

        elif self.ObLs[i][0] == 'FillNa' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','File','Replace_Value','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])
           
 
            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)
            
            

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)
          


        elif self.ObLs[i][0] == 'CsvWrite' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','RESULT','COLUMN','LOCATION','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])
            test4 = QTableWidgetItem(self.ObLs[i][3])
            
            

            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)
            test4.setTextAlignment(Qt.AlignCenter)
            
            

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)
            self.table.setItem(0, 3,test4)


        elif self.ObLs[i][0] == 'CsvRead' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','LOCATION','RESULT','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])
           
            
            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)
            
            
            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)


            
        elif self.ObLs[i][0] == 'SetText' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','XPATH','TEXT','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])
            

            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)
            

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)
        
        elif self.ObLs[i][0] == 'TypeWrite' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','TEXT','','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            

            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)            

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)



        elif self.ObLs[i][0] == 'Resize' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','X','Y','O_PATH','P_PATH','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])
            test4 = QTableWidgetItem(self.ObLs[i][3])
            test5 = QTableWidgetItem(self.ObLs[i][4])
            

            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)
            test4.setTextAlignment(Qt.AlignCenter)
            test5.setTextAlignment(Qt.AlignCenter)
            

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)
            self.table.setItem(0, 3,test4)
            self.table.setItem(0, 4,test5)

        
        elif self.ObLs[i][0] == 'ConvertGray' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','O_PATH','P_PATH','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])
           
            
            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)
            
            
            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)


        elif self.ObLs[i][0] == 'ImgSquare' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','O_PATH','P_PATH','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])
            
            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)


        elif self.ObLs[i][0] == 'ThresHolding' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','O_PATH','P_PATH','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])
           
            
            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)
            
            
            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)


        elif self.ObLs[i][0] == 'EqualizeHist' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','O_PATH','P_PATH','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])
           
            
            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)
            
            
            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)

        
        elif self.ObLs[i][0] == 'ColorEqualizeHist' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','O_PATH','P_PATH','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])
           
            
            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)
            
            
            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)


        elif self.ObLs[i][0] == 'Blur' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','Blur_X','Blur_Y','O_PATH','P_PATH','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])
            test4 = QTableWidgetItem(self.ObLs[i][3])
            test5 = QTableWidgetItem(self.ObLs[i][4])
           
            
            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)
            test4.setTextAlignment(Qt.AlignCenter)
            test5.setTextAlignment(Qt.AlignCenter)
            
            
            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)
            self.table.setItem(0, 3,test4)
            self.table.setItem(0, 4,test5)

        elif self.ObLs[i][0] == 'Blur_2D' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','Blur_2D_Value','O_PATH','P_PATH','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])
            test4 = QTableWidgetItem(self.ObLs[i][3])
           
            
            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)
            test4.setTextAlignment(Qt.AlignCenter)
            
            
            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)
            self.table.setItem(0, 3,test4)

        elif self.ObLs[i][0] == 'GausianBlur' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','O_PATH','P_PATH','Kernel_W','Kernel_H','Sigma',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])
            test4 = QTableWidgetItem(self.ObLs[i][3])
            test5 = QTableWidgetItem(self.ObLs[i][4])
            test6 = QTableWidgetItem(self.ObLs[i][5])
           
            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)
            test4.setTextAlignment(Qt.AlignCenter)
            test5.setTextAlignment(Qt.AlignCenter)
            test6.setTextAlignment(Qt.AlignCenter)
             
            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)
            self.table.setItem(0, 3,test4)
            self.table.setItem(0, 4,test5)
            self.table.setItem(0, 5,test6)

        elif self.ObLs[i][0] == 'MedianBlur' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','O_PATH','P_PATH','Kernel_size','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])
            test4 = QTableWidgetItem(self.ObLs[i][3])
          
           
            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)
            test4.setTextAlignment(Qt.AlignCenter)
          
             
            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)
            self.table.setItem(0, 3,test4)


        elif self.ObLs[i][0] == 'BilateralBlur' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','O_PATH','P_PATH','Pixel','Color_Space','Sigma',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])
            test4 = QTableWidgetItem(self.ObLs[i][3])
            test5 = QTableWidgetItem(self.ObLs[i][4])
            test6 = QTableWidgetItem(self.ObLs[i][5])
          
           
            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)
            test4.setTextAlignment(Qt.AlignCenter)
            test5.setTextAlignment(Qt.AlignCenter)
            test6.setTextAlignment(Qt.AlignCenter)
          
             
            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)
            self.table.setItem(0, 3,test4)
            self.table.setItem(0, 4,test5)
            self.table.setItem(0, 5,test6)


        

        

           
        elif self.ObLs[i][0] == 'MaxWin' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','NOT VALUE','','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])

            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)


        elif self.ObLs[i][0] == 'For' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','START','END','COUNT','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])
            test4 = QTableWidgetItem(self.ObLs[i][3])

            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)
            test4.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)
            self.table.setItem(0, 3,test4)



        elif self.ObLs[i][0] == 'TimeSleep' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','SECONDS','','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])

            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)



        elif self.ObLs[i][0] == 'Click' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','XPATH','','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])

            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)


        elif self.ObLs[i][0] == 'MousePosition' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','Default','','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])

            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
        
        elif self.ObLs[i][0] == 'MoveToPosition' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','X_Position','Y_Position','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])

            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)
        
        elif self.ObLs[i][0] == 'MoveToPositionClick' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','X_Position','Y_Position','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])

            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)
        
        elif self.ObLs[i][0] == 'MoveToPositionDoubleClick' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','X_Position','Y_Position','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])

            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)




        
        elif self.ObLs[i][0] == 'MakeClipBoard' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','FILE NAME','MODE','ENCODING','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])
            test4 = QTableWidgetItem(self.ObLs[i][3])
            

            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)
            test4.setTextAlignment(Qt.AlignCenter)
            

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)
            self.table.setItem(0, 3,test4)

        
        elif self.ObLs[i][0] == 'Filter_Content' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','CONTENT','RESULT','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])
            
            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)
        
        elif self.ObLs[i][0] == 'Morphs' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','CONTENT','RESULT','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])
            
            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)

        elif self.ObLs[i][0] == 'Extract_Word' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','CONTENT','RESULT','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])
            
            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)

        elif self.ObLs[i][0] == 'Counter_Word' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','CONTENT','RESULT','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])
            
            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)

        elif self.ObLs[i][0] == 'WordCloud' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','CONTENT','','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            
            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
        
            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)


        elif self.ObLs[i][0] == 'Ocr_Eng' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','ADRESS','','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])

            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)


        elif self.ObLs[i][0] == 'Ocr_Kor' :

            self.table.clear()

            self.table.setHorizontalHeaderLabels(['정확한 값을 입력해 주세요 ! '])
            self.table.setVerticalHeaderLabels(['NAME','ADRESS','RESULT','','','',''])

            test1 = QTableWidgetItem(self.ObLs[i][0])
            test2 = QTableWidgetItem(self.ObLs[i][1])
            test3 = QTableWidgetItem(self.ObLs[i][2])

            test1.setTextAlignment(Qt.AlignCenter)
            test2.setTextAlignment(Qt.AlignCenter)
            test3.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(0, 0,test1)
            self.table.setItem(0, 1,test2)
            self.table.setItem(0, 2,test3)
            
            

        elif self.ObLs[i][0] == 'Script' :

            test = self.ObLs[i][1] 
            self.Py_Text.setText(test)
            

            
    #####################################################
    # Edit 버튼 클릭시 속성창 안에 해당되는 값들이 저장됨#
    ####################################################

    def AttEdit(self) :
        
        
        i = self.te_1.currentRow()

        

        if self.ObLs[i][0] == 'OpenBrowser' :

            f1 = self.table.item(1,0).text()
            
            self.ObLs[i][1] = f1


        elif self.ObLs[i][0] == 'MakeFolder' :

            mf1 = self.table.item(1,0).text()
            
            self.ObLs[i][1] = mf1


        
        elif self.ObLs[i][0] == 'PageDown' :

            pd1 = self.table.item(1,0).text()
            pd2 = self.table.item(2,0).text()
            
            self.ObLs[i][1] = pd1
            self.ObLs[i][2] = pd2

        elif self.ObLs[i][0] == 'Enter' :

            pd1 = self.table.item(1,0).text()
            
            self.ObLs[i][1] = pd1
            

        elif self.ObLs[i][0] == 'ImgSquare' :

            is1 = self.table.item(1,0).text()
            is2 = self.table.item(2,0).text()
            
            self.ObLs[i][1] = is1
            self.ObLs[i][2] = is2
        
        elif self.ObLs[i][0] == 'Filter_Content' :

            fc1 = self.table.item(1,0).text()
            fc2 = self.table.item(2,0).text()
            
            self.ObLs[i][1] = fc1
            self.ObLs[i][2] = fc2

        elif self.ObLs[i][0] == 'Morphs' :

            mp1 = self.table.item(1,0).text()
            mp2 = self.table.item(2,0).text()
            
            self.ObLs[i][1] = mp1
            self.ObLs[i][2] = mp2

        elif self.ObLs[i][0] == 'Extract_Word' :

            ew1 = self.table.item(1,0).text()
            ew2 = self.table.item(2,0).text()
            
            self.ObLs[i][1] = ew1
            self.ObLs[i][2] = ew2

        elif self.ObLs[i][0] == 'Counter_Word' :

            cw1 = self.table.item(1,0).text()
            cw2 = self.table.item(2,0).text()
            
            self.ObLs[i][1] = cw1
            self.ObLs[i][2] = cw2

        
        elif self.ObLs[i][0] == 'WordCloud' :

            wc1 = self.table.item(1,0).text()
           
            self.ObLs[i][1] = wc1


        elif self.ObLs[i][0] == 'BrowserClose' :

            f1 = self.table.item(1,0).text()
            
            self.ObLs[i][1] = f1
        
        
        elif self.ObLs[i][0] == 'SwitchWin' :

            sw1 = self.table.item(1,0).text()
            
            self.ObLs[i][1] = sw1



        elif self.ObLs[i][0] == 'Assign' :

            as1 = self.table.item(1,0).text()
            as2 = self.table.item(2,0).text()
            
            self.ObLs[i][1] = as1
            self.ObLs[i][2] = as2



        elif self.ObLs[i][0] == 'TextCrawling' :

            f1 = self.table.item(1,0).text()
            f2 = self.table.item(2,0).text()
            f3 = self.table.item(3,0).text()
            f4 = self.table.item(4,0).text()
            f5 = self.table.item(5,0).text()
            f6 = self.table.item(6,0).text()
        
            self.ObLs[i][1] = f1
            self.ObLs[i][2] = f2
            self.ObLs[i][3] = f3
            self.ObLs[i][4] = f4
            self.ObLs[i][5] = f5
            self.ObLs[i][6] = f6


        elif self.ObLs[i][0] == 'ImageCrawling' :

            f1 = self.table.item(1,0).text()
            f2 = self.table.item(2,0).text()
            f3 = self.table.item(3,0).text()
            f4 = self.table.item(4,0).text()
            
        
            self.ObLs[i][1] = f1
            self.ObLs[i][2] = f2
            self.ObLs[i][3] = f3
            self.ObLs[i][4] = f4

        elif self.ObLs[i][0] == 'InstaImageCrawling' :

            ic1 = self.table.item(1,0).text()
            ic2 = self.table.item(2,0).text()
            
            self.ObLs[i][1] = ic1
            self.ObLs[i][2] = ic2


        elif self.ObLs[i][0] == 'Resize' :

            rs1 = self.table.item(1,0).text()
            rs2 = self.table.item(2,0).text()
            rs3 = self.table.item(3,0).text()
            rs4 = self.table.item(4,0).text()
            
        
            self.ObLs[i][1] = rs1
            self.ObLs[i][2] = rs2
            self.ObLs[i][3] = rs3
            self.ObLs[i][4] = rs4

        elif self.ObLs[i][0] == 'ConvertGray' :

            cg1 = self.table.item(1,0).text()
            cg2 = self.table.item(2,0).text()
          
            
            self.ObLs[i][1] = cg1
            self.ObLs[i][2] = cg2

        elif self.ObLs[i][0] == 'ThresHolding' :

            th1 = self.table.item(1,0).text()
            th2 = self.table.item(2,0).text()
          
            
            self.ObLs[i][1] = th1
            self.ObLs[i][2] = th2

        
        elif self.ObLs[i][0] == 'EqualizeHist' :

            eh1 = self.table.item(1,0).text()
            eh2 = self.table.item(2,0).text()
          
            
            self.ObLs[i][1] = eh1
            self.ObLs[i][2] = eh2


        elif self.ObLs[i][0] == 'ColorEqualizeHist' :

            ceh1 = self.table.item(1,0).text()
            ceh2 = self.table.item(2,0).text()
          
            
            self.ObLs[i][1] = ceh1
            self.ObLs[i][2] = ceh2

        
        elif self.ObLs[i][0] == 'Blur' :

            bl1 = self.table.item(1,0).text()
            bl2 = self.table.item(2,0).text()
            bl3 = self.table.item(3,0).text()
            bl4 = self.table.item(4,0).text()
          
            
            self.ObLs[i][1] = bl1
            self.ObLs[i][2] = bl2
            self.ObLs[i][3] = bl3
            self.ObLs[i][4] = bl4


        elif self.ObLs[i][0] == 'Blur_2D' :

            dbl1 = self.table.item(1,0).text()
            dbl2 = self.table.item(2,0).text()
            dbl3 = self.table.item(3,0).text()
            
            self.ObLs[i][1] = dbl1
            self.ObLs[i][2] = dbl2
            self.ObLs[i][3] = dbl3

        elif self.ObLs[i][0] == 'GausianBlur' :

            gb1 = self.table.item(1,0).text()
            gb2 = self.table.item(2,0).text()
            gb3 = self.table.item(3,0).text()
            gb4 = self.table.item(4,0).text()
            gb5 = self.table.item(5,0).text()
            
            self.ObLs[i][1] = gb1
            self.ObLs[i][2] = gb2
            self.ObLs[i][3] = gb3
            self.ObLs[i][4] = gb4
            self.ObLs[i][5] = gb5

        
        elif self.ObLs[i][0] == 'MedianBlur' :

            mb1 = self.table.item(1,0).text()
            mb2 = self.table.item(2,0).text()
            mb3 = self.table.item(3,0).text()
             
            self.ObLs[i][1] = mb1
            self.ObLs[i][2] = mb2
            self.ObLs[i][3] = mb3

        elif self.ObLs[i][0] == 'BilateralBlur' :

            bb1 = self.table.item(1,0).text()
            bb2 = self.table.item(2,0).text()
            bb3 = self.table.item(3,0).text()
            bb4 = self.table.item(4,0).text()
            bb5 = self.table.item(5,0).text()
             
            self.ObLs[i][1] = bb1
            self.ObLs[i][2] = bb2
            self.ObLs[i][3] = bb3
            self.ObLs[i][4] = bb4
            self.ObLs[i][5] = bb5
           
        
        elif self.ObLs[i][0] == 'ExcelWrite' :

            f1 = self.table.item(1,0).text()
            f2 = self.table.item(2,0).text()
            f3 = self.table.item(3,0).text()
            
            self.ObLs[i][1] = f1
            self.ObLs[i][2] = f2
            self.ObLs[i][3] = f3


        elif self.ObLs[i][0] == 'ExcelRead' :

            er1 = self.table.item(1,0).text()
            er2 = self.table.item(2,0).text()
            
            
            self.ObLs[i][1] = er1
            self.ObLs[i][2] = er2
        
        elif self.ObLs[i][0] == 'RowDropNa' :

            er1 = self.table.item(1,0).text()
            
            self.ObLs[i][1] = er1
        
        elif self.ObLs[i][0] == 'ColumnDropNa' :

            er1 = self.table.item(1,0).text()
            
            self.ObLs[i][1] = er1

        elif self.ObLs[i][0] == 'FillNa' :

            er1 = self.table.item(1,0).text()
            er2 = self.table.item(2,0).text()
            
            self.ObLs[i][1] = er1
            self.ObLs[i][2] = er2

            

        
        elif self.ObLs[i][0] == 'CsvWrite' :

            f1 = self.table.item(1,0).text()
            f2 = self.table.item(2,0).text()
            f3 = self.table.item(3,0).text()
            
            
            self.ObLs[i][1] = f1
            self.ObLs[i][2] = f2
            self.ObLs[i][3] = f3


        elif self.ObLs[i][0] == 'CsvRead' :

            cr1 = self.table.item(1,0).text()
            cr2 = self.table.item(2,0).text()
            
            
            self.ObLs[i][1] = cr1
            self.ObLs[i][2] = cr2


        
        elif self.ObLs[i][0] == 'For' :

            f1 = self.table.item(1,0).text()
            f2 = self.table.item(2,0).text()
            f3 = self.table.item(3,0).text()
            
            
            self.ObLs[i][1] = f1
            self.ObLs[i][2] = f2
            self.ObLs[i][3] = f3
            


        elif self.ObLs[i][0] == 'SetText' :

            f1 = self.table.item(1,0).text()
            f2 = self.table.item(2,0).text()
         

            self.ObLs[i][1] = f1
            self.ObLs[i][2] = f2

        
        elif self.ObLs[i][0] == 'TypeWrite' :

            f1 = self.table.item(1,0).text()
         
            self.ObLs[i][1] = f1
            

        
        elif self.ObLs[i][0] == 'MaxWin' :

            f1 = self.table.item(1,0).text()
            
            self.ObLs[i][1] = f1
           


        elif self.ObLs[i][0] == 'TimeSleep' :

            f1 = self.table.item(1,0).text()
            
            self.ObLs[i][1] = f1
           


        elif self.ObLs[i][0] == 'Click' :

            f1 = self.table.item(1,0).text()
          
            self.ObLs[i][1] = f1

        
        elif self.ObLs[i][0] == 'MousePosition' :

            f1 = self.table.item(1,0).text()
          
            self.ObLs[i][1] = f1
        
        elif self.ObLs[i][0] == 'MoveToPosition' :

            f1 = self.table.item(1,0).text()
            f2 = self.table.item(2,0).text()
          
            self.ObLs[i][1] = f1
            self.ObLs[i][2] = f2
        
        elif self.ObLs[i][0] == 'MoveToPositionClick' :

            f1 = self.table.item(1,0).text()
            f2 = self.table.item(2,0).text()
          
            self.ObLs[i][1] = f1
            self.ObLs[i][2] = f2
        
        elif self.ObLs[i][0] == 'MoveToPositionDoubleClick' :

            f1 = self.table.item(1,0).text()
            f2 = self.table.item(2,0).text()
          
            self.ObLs[i][1] = f1
            self.ObLs[i][2] = f2


        elif self.ObLs[i][0] == 'MakeClipBoard' :

            f1 = self.table.item(1,0).text()
            f2 = self.table.item(2,0).text()
            f3 = self.table.item(3,0).text()
            
            self.ObLs[i][1] = f1
            self.ObLs[i][2] = f2
            self.ObLs[i][3] = f3


        elif self.ObLs[i][0] == 'Ocr_Eng' :

            f1 = self.table.item(1,0).text()

            self.ObLs[i][1] = f1


        elif self.ObLs[i][0] == 'Ocr_Kor' :

            f1 = self.table.item(1,0).text()
            f2 = self.table.item(2,0).text()

            self.ObLs[i][1] = f1
            self.ObLs[i][2] = f2

            


        else: 

            print("Script 입니다.")

         
        print("수정이 완료되었습니다 .")
       

    ###################################################################
    # start 버튼 클릭시 메인리스트에 해당되는 항목들이 순차적으로 실행 #
    ###################################################################

    def Start(self):
        
        # 0619 try catch로 화면을 꺼지는 것을 방지 !

        Count_Zero = self.te_1.count()
        

        if Count_Zero == 0 :
            
            self.Tab_Problem()

        else : 
            
          
            for i in range(self.te_1.count()):


                if self.ObLs[i][0] == ("OpenBrowser") :
                    
                    try :

                        ob = self.ObLs[i][1]

                        self.OpenBrowser(ob)

                        name = self.ObLs[i][0]

                        self.Tab_Terminal(name)
                    
                    except:

                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)
                        self.driver.close()


                elif self.ObLs[i][0] == ("MakeFolder") :

                    try :

                        mk = self.ObLs[i][1]

                        self.MakeFolder(mk)

                        name = self.ObLs[i][0]

                        self.Tab_Terminal(name)
                    
                    except:

                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)


                elif self.ObLs[i][0] == ("PageDown") :

                    try :

                        pd1 = self.ObLs[i][1]
                        pd2 = self.ObLs[i][2]

                        self.PageDown(pd1,pd2)

                        name = self.ObLs[i][0]

                        self.Tab_Terminal(name)
                    
                    except:

                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)
                
                elif self.ObLs[i][0] == ("Enter") :

                    try :

                        pd1 = self.ObLs[i][1]
                    

                        self.Enter()

                        name = self.ObLs[i][0]

                        self.Tab_Terminal(name)
                    
                    except:

                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)


                elif self.ObLs[i][0] == ("BrowserClose") :

                    try:

                        bc = self.ObLs[i][1]

                        self.BrowserClose()

                        name = self.ObLs[i][0]

                        self.Tab_Terminal(name)
                    
                    except:

                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

                elif self.ObLs[i][0] == ("SwitchWin") :
                    

                    try:

                        sw = self.ObLs[i][1]

                        self.SwitchWin(sw)

                        name = self.ObLs[i][0]

                        self.Tab_Terminal(name)
                    
                    except:

                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)



                elif self.ObLs[i][0] == ("Assign") :

                    try:

                        as1 = self.ObLs[i][1]
                        as2 = self.ObLs[i][2]
                    
                        self.Assign(as1,as2)

                        name = self.ObLs[i][0]

                        self.Tab_Terminal(name)
                    
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

            
                elif self.ObLs[i][0] == ("SetText") :

                    try:

                        tx1 = self.ObLs[i][1]
                        tx2 = self.ObLs[i][2]

                        self.SetText(tx1,tx2)

                        name = self.ObLs[i][0]

                        self.Tab_Terminal(name)

                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

                
                elif self.ObLs[i][0] == ("TypeWrite") :

                    
                    try:

                        tw1 = self.ObLs[i][1]
                        
                        self.TypeWrite(tw1)

                        name = self.ObLs[i][0]

                        self.Tab_Terminal(name)

                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)


                elif self.ObLs[i][0] == ("For") :

                    
                    try :

                        fr1 = self.ObLs[i][1]
                        fr2 = self.ObLs[i][2]
                        fr3 = self.ObLs[i][3]

                        self.EachFor(fr1,fr2,fr3)

                        name = self.ObLs[i][0]

                        self.Tab_Terminal(name)
                    
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)


                elif self.ObLs[i][0] == ("TextCrawling") :

                    try:

                        cr1 = self.ObLs[i][1]
                        cr2 = self.ObLs[i][2]
                        cr3 = self.ObLs[i][3]
                        cr4 = self.ObLs[i][4]
                        cr5 = self.ObLs[i][5]
                        cr6 = self.ObLs[i][6]

                        self.TextCrawling(cr1,cr2,cr3,cr4,cr5,cr6)
                    
                        name = self.ObLs[i][0]
                        self.Tab_Terminal(name)
                    
                        
                    
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

                
                elif self.ObLs[i][0] == ("ImageCrawling") :

                  
                    try:

                        icr1 = self.ObLs[i][1]
                        icr2 = self.ObLs[i][2]
                        icr3 = self.ObLs[i][3]
                        icr4 = self.ObLs[i][4]
                    
                        self.ImageCrawling(icr1,icr2,icr3,icr4)

                        name = self.ObLs[i][0]
                        self.Tab_Terminal(name)
                    
                    except:
                  
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

                elif self.ObLs[i][0] == ("InstaImageCrawling") :

                  
                    try:

                        ic1 = self.ObLs[i][1]
                        ic2 = self.ObLs[i][2]
                    
                        self.InstaImageCrawling(ic1,ic2)

                        name = self.ObLs[i][0]
                        self.Tab_Terminal(name)
                    
                    except:
                  
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)



                elif self.ObLs[i][0] == ("Resize") :

                    try:

                        rs1 = self.ObLs[i][1]
                        rs2 = self.ObLs[i][2]
                        rs3 = self.ObLs[i][3]
                        rs4 = self.ObLs[i][4]
                    
                        self.Resize(rs1,rs2,rs3,rs4)

                        name = self.ObLs[i][0]
                        self.Tab_Terminal(name)
                    
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

                elif self.ObLs[i][0] == ("ConvertGray") :

                    
                    try:
                        cg1 = self.ObLs[i][1]
                        cg2 = self.ObLs[i][2]

                        self.ConvertGray(cg1,cg2)
                    
                        name = self.ObLs[i][0]
                        self.Tab_Terminal(name)
                    
                      
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)


                elif self.ObLs[i][0] == ("ImgSquare") :

                    try:

                        is1 = self.ObLs[i][1]
                        is2 = self.ObLs[i][2]

                        self.ImgSquare(is1,is2)
                    
                        name = self.ObLs[i][0]
                        self.Tab_Terminal(name)
                    
                    
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)


                elif self.ObLs[i][0] == ("ThresHolding") :

                    try:

                        th1 = self.ObLs[i][1]
                        th2 = self.ObLs[i][2]

                        self.ThresHolding(th1,th2)
                    
                        name = self.ObLs[i][0]
                        self.Tab_Terminal(name)
                    
                   
                    
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

                
                elif self.ObLs[i][0] == ("EqualizeHist") :

                    try:

                        eh1 = self.ObLs[i][1]
                        eh2 = self.ObLs[i][2]

                        self.EqualizeHist(eh1,eh2)
                    
                        name = self.ObLs[i][0]
                        self.Tab_Terminal(name)
                    
                   
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

                
                elif self.ObLs[i][0] == ("ColorEqualizeHist") :

                   
                    try:
                        ceh1 = self.ObLs[i][1]
                        ceh2 = self.ObLs[i][2]

                        self.ColorEqualizeHist(ceh1,ceh2)
                    
                        name = self.ObLs[i][0]
                        self.Tab_Terminal(name)
                    
                   
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

                
                elif self.ObLs[i][0] == ("Blur") :

                   
                    try:

                        bl1 = self.ObLs[i][1]
                        bl2 = self.ObLs[i][2]
                        bl3 = self.ObLs[i][3]
                        bl4 = self.ObLs[i][4]

                        self.Blur(bl1,bl2,bl3,bl4)
                    
                        name = self.ObLs[i][0]
                        self.Tab_Terminal(name)
                    
                   
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

                
                elif self.ObLs[i][0] == ("Blur_2D") :

                   
                   
                    try:
                        dbl1 = self.ObLs[i][1]
                        dbl2 = self.ObLs[i][2]
                        dbl3 = self.ObLs[i][3] 

                        self.Blur_2D(dbl1,dbl2,dbl3)
                    
                        name = self.ObLs[i][0]
                        self.Tab_Terminal(name)
                    
                   
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

                
                elif self.ObLs[i][0] == ("GausianBlur") :

                   
                   
                    try:

                        gb1 = self.ObLs[i][1]
                        gb2 = self.ObLs[i][2]
                        gb3 = self.ObLs[i][3]
                        gb4 = self.ObLs[i][4]
                        gb5 = self.ObLs[i][5] 

                        self.GausianBlur(gb1,gb2,gb3,gb4,gb5)
                    
                        name = self.ObLs[i][0]
                        self.Tab_Terminal(name)
                    
                   
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)
                
                elif self.ObLs[i][0] == ("MedianBlur") :

                   
                    try:

                        mb1 = self.ObLs[i][1]
                        mb2 = self.ObLs[i][2]
                        mb3 = self.ObLs[i][3]

                        self.MedianBlur(mb1,mb2,mb3)
                    
                        name = self.ObLs[i][0]
                        self.Tab_Terminal(name)
                    
                   
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

                
                elif self.ObLs[i][0] == ("BilateralBlur") :

                   
                    try:

                        bb1 = self.ObLs[i][1]
                        bb2 = self.ObLs[i][2]
                        bb3 = self.ObLs[i][3]
                        bb4 = self.ObLs[i][4]
                        bb5 = self.ObLs[i][5]

                        self.BilateralBlur(bb1,bb2,bb3,bb4,bb5)
                    
                        name = self.ObLs[i][0]
                        self.Tab_Terminal(name)
                    
                   
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

                
                elif self.ObLs[i][0] == ("Filter_Content") :

                   
                    try:

                        fc1 = self.ObLs[i][1]
                        fc2 = self.ObLs[i][2]

                        self.Filter_Content(fc1,fc2)
                    
                        name = self.ObLs[i][0]
                        self.Tab_Terminal(name)
                    
                   
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

                elif self.ObLs[i][0] == ("Morphs") :

                   
                    try:

                        mp1 = self.ObLs[i][1]
                        mp2 = self.ObLs[i][2]

                        self.Morphs(mp1,mp2)
                    
                        name = self.ObLs[i][0]
                        self.Tab_Terminal(name)
                    
                   
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

                elif self.ObLs[i][0] == ("Extract_Word") :

                   
                    try:

                        ew1 = self.ObLs[i][1]
                        ew2 = self.ObLs[i][2]

                        self.Extract_Word(ew1,ew2)
                    
                        name = self.ObLs[i][0]
                        self.Tab_Terminal(name)
                    
                   
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)
                
                elif self.ObLs[i][0] == ("Counter_Word") :

                   
                    try:

                        cw1 = self.ObLs[i][1]
                        cw2 = self.ObLs[i][2]

                        self.Counter_Word(cw1,cw2)
                    
                        name = self.ObLs[i][0]
                        self.Tab_Terminal(name)
                    
                   
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

                elif self.ObLs[i][0] == ("WordCloud") :

                   
                    try:

                        wc1 = self.ObLs[i][1]
                        

                        self.WordCloud(wc1)
                    
                        name = self.ObLs[i][0]
                        self.Tab_Terminal(name)
                    
                   
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)
                                


                elif self.ObLs[i][0] == ("ExcelWrite") :

                    try:

                        ex1 = self.ObLs[i][1]
                        ex2 = self.ObLs[i][2]
                        ex3 = self.ObLs[i][3]
                    
                        self.ExcelWrite(ex1,ex2,ex3)

                        name = self.ObLs[i][0]
                        self.Tab_Terminal(name)
                    
                        
                    
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

                
                elif self.ObLs[i][0] == ("ExcelRead") :


                    try:

                        er1 = self.ObLs[i][1]
                        er2 = self.ObLs[i][2]
                        
                        self.ExcelRead(er1,er2)

                        name = self.ObLs[i][0]
                        self.Tab_Terminal(name)
                    
                        
                    
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)
                
                elif self.ObLs[i][0] == ("RowDropNa") :


                    try:

                        er1 = self.ObLs[i][1]
                        
                        self.RowDropNa(er1)

                        name = self.ObLs[i][0]
                        self.Tab_Terminal(name)
                    
                        
                    
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)
                
                elif self.ObLs[i][0] == ("ColumnDropNa") :


                    try:

                        er1 = self.ObLs[i][1]
                        
                        self.ColumnDropNa(er1)

                        name = self.ObLs[i][0]
                        self.Tab_Terminal(name)
                    
                        
                    
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)
                
                elif self.ObLs[i][0] == ("FillNa") :


                    try:

                        er1 = self.ObLs[i][1]
                        er2 = self.ObLs[i][2]
                        
                        self.FillNa(er1,er2)

                        name = self.ObLs[i][0]
                        self.Tab_Terminal(name)
                    
                        
                    
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

                
                elif self.ObLs[i][0] == ("CsvWrite") :

                    try:

                        csv1 = self.ObLs[i][1]
                        csv2 = self.ObLs[i][2]
                        csv3 = self.ObLs[i][3]

                        self.CsvWrite(csv1,csv2,csv3)
                    
                        name = self.ObLs[i][0]
                        self.Tab_Terminal(name)
                    
                        

                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)


                elif self.ObLs[i][0] == ("CsvRead") :

                    try:

                        cr1 = self.ObLs[i][1]
                        cr2 = self.ObLs[i][2]
                        
                        self.CsvRead(cr1,cr2)

                        name = self.ObLs[i][0]
                        self.Tab_Terminal(name)
                    
                    
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

         

                elif self.ObLs[i][0] == ("MaxWin") :

                    try:

                        max = self.ObLs[i][1]

                        self.MaxWin()

                        name = self.ObLs[i][0]

                        self.Tab_Terminal(name)
                    
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)


                elif self.ObLs[i][0] == ("TimeSleep") :

                    try:

                        ts = float(self.ObLs[i][1])

                        self.TimeSleep(ts)

                        name = self.ObLs[i][0]

                        self.Tab_Terminal(name)

                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)


                elif self.ObLs[i][0] == ("Click") :

                    try:

                        cl = self.ObLs[i][1]
                        cr = str(cl)

                        self.Click(cr)

                        name = self.ObLs[i][0]

                        self.Tab_Terminal(name)
                    
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)
                
                elif self.ObLs[i][0] == ("MousePosition") :

                    try:

                        self.MousePosition()

                        name = self.ObLs[i][0]

                        self.Tab_Terminal(name)
                    
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

                
                elif self.ObLs[i][0] == ("MoveToPosition") :

                    
                    try :
                        
                        mtp1 = self.ObLs[i][1]
                        mtp2 = self.ObLs[i][2]
                    
                        self.MoveToPosition(mtp1,mtp2)

                        name = self.ObLs[i][0]

                        self.Tab_Terminal(name)
                    
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

                
                elif self.ObLs[i][0] == ("MoveToPositionClick") :

                    
                    try :
                        
                        mtpc1 = self.ObLs[i][1]
                        mtpc2 = self.ObLs[i][2]
                    
                        self.MoveToPositionClick(mtpc1,mtpc2)

                        name = self.ObLs[i][0]

                        self.Tab_Terminal(name)
                    
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

                
                elif self.ObLs[i][0] == ("MoveToPositionDoubleClick") :

                    
                    try :
                        
                        mtpdc1 = self.ObLs[i][1]
                        mtpdc2 = self.ObLs[i][2]
                    
                        self.MoveToPositionDoubleClick(mtpdc1,mtpdc2)

                        name = self.ObLs[i][0]

                        self.Tab_Terminal(name)
                    
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

                

                   
                
                elif self.ObLs[i][0] == ("MakeClipBoard") :

                    try:

                        f1 = self.ObLs[i][1]
                        f2 = self.ObLs[i][2]
                        f3 = self.ObLs[i][3]

                        self.MakeClipBoard(f1,f2,f3)

                        name = self.ObLs[i][0]

                        self.Tab_Terminal(name)
                    
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

                
                elif self.ObLs[i][0] == ("Script") :

                    try:

                        sc = self.ObLs[i][1]

                        self.S_Script(sc)

                        name = self.ObLs[i][0]

                        self.Tab_Terminal(name)

                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)


                elif self.ObLs[i][0] == ("Ocr_Eng") :

                    try:

                        ocr = self.ObLs[i][1]

                        self.Ocr_Eng(ocr)

                        name = self.ObLs[i][0]

                        self.Tab_Terminal(name)
                    
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

                
                elif self.ObLs[i][0] == ("Ocr_Kor") :

                    try:

                        ocr1 = self.ObLs[i][1]
                        ocr2 = self.ObLs[i][2]

                        self.Ocr_Kor(ocr1,ocr2)

                        name = self.ObLs[i][0]

                        self.Tab_Terminal(name)
                    
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

                    
                
                else : 

                    print('해당하는항목이없습니다')

            
            
#############################################################################################
#################### start 버튼 클릭시 해당되는 이름의 함수 호출 ##############################
################### 각 함수들은 각각의 기능을 수행 ############################################
###############################################################################################                


                    

    def OpenBrowser(self,str1) :
        
        # 완료 06-20 / assign 오류 해결
        # 참고해서 만들것
        url = str1

        for i in range((len(self.ObLs))): # self.obls 값
            if self.ObLs[i][0] == 'Assign':
                if self.ObLs[i][1] == url : # 넣는값
                    url = self.ObLs[i][2]
                else :
                    print('')
              
                                 
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.implicitly_wait(10)


    def MakeFolder(self,str1):

        # 완료 06-20 / assign 오류 해결
        test1 = str1

        for i in range((len(self.ObLs))): # self.obls 값
            if self.ObLs[i][0] == 'Assign':
                if self.ObLs[i][1] == test1 : # 넣는값
                    test1 = self.ObLs[i][2]
                else :
                    print('')

        os.mkdir(test1)
        

    def BrowserClose(self) :

        # 완료 06-20 / assign 오류 해결
        self.driver.close()

    def SwitchWin(self,str1):
        
        test1 = str1

        self.driver.switch_to.window(self.driver.window_handles[int(test1)])

    def PageDown(self,str1,str2):
        
        # 완료 06-20 / assign 오류 해결

        test1 = str1
        test2 = str2

        for i in range((len(self.ObLs))): # self.obls 값
            if self.ObLs[i][0] == 'Assign':
                if self.ObLs[i][1] == test1 : # 넣는값
                    test1 = self.ObLs[i][2]
                else : 
                    print('')
                if self.ObLs[i][1] == test2 : # 넣는값
                    test2 = self.ObLs[i][2]
                else : 
                    print('')
                

        test3 = self.driver.find_element_by_tag_name(test1)

        for i in range(int(test2)):
            # test.click()
            test3.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)

        print('PageDown이 실행되었습니다')
    
    def Enter(self):
        
        # 완료 06-20 / assign 오류 해결
        pyautogui.press('enter')

        print('Enter이 실행되었습니다')
    


    

    def Assign(self,str1,str2):

        # 완료 06-20 / assign 오류 해결

        a = str1
        b = str2

        test = {a:b}
        
        # 완료 06-20 / assign 오류 해결
        
        print('Assign 기능이 실행되었습니다')

        


    def SetText(self,str1,str2) :

        # 완료 06-20 / assign 오류 해결
        test1 = str1
        test2 = str2


        for i in range((len(self.ObLs))): # self.obls 값
            if self.ObLs[i][0] == 'Assign':
                if self.ObLs[i][1] == test1 : # 넣는값
                    test1 = self.ObLs[i][2]
                else : 
                    print('')

                if self.ObLs[i][1] == test2 : # 넣는값
                    test2 = self.ObLs[i][2]
                else : 
                    print('')

        
        self.driver.find_element_by_xpath(test1).send_keys(test2)
        print("SetText 기능이 실행되었습니다.")

    
    def TypeWrite(self,str1) :

        # 완료 06-20 / assign 오류 해결
        test1 = str1


        for i in range((len(self.ObLs))): # self.obls 값
            if self.ObLs[i][0] == 'Assign':
                if self.ObLs[i][1] == test1 : # 넣는값
                    test1 = self.ObLs[i][2]
                else : 
                    print('')

        
        pyautogui.typewrite(str(test1))
        print("typewrite 기능이 실행되었습니다.")

    



    def TextCrawling(self,str1,str2,str3,str4,str5,str6) :
        
        # 완료 06-20 / assign 오류 해결

        html = self.driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        result = []

        test1 = str1
        test2 = str2
        test3 = str3
        test4 = str4
        test5 = str5
        test6 = str6

        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test1 : # 넣는값
                    test1 = self.ObLs[i][2]
                else : 
                    print('')

                if self.ObLs[i][1] == test2 : # 넣는값
                    test2 = self.ObLs[i][2]
                else : 
                    print('')

                if self.ObLs[i][1] == test3 : # 넣는값
                    test3 = self.ObLs[i][2]
                else : 
                    print('')

                if self.ObLs[i][1] == test4 : # 넣는값
                    test4 = self.ObLs[i][2]
                else : 
                    print('')

                if self.ObLs[i][1] == test5 : # 넣는값
                    test5 = self.ObLs[i][2]
                else : 
                    print('')
        

        cr = soup.select(test1)
        

        for i in cr:

            tmp = []

            # 사용자 입력값 비교 if문
            if(test2 != 'Default'):
                tmp.append(i.select(test2)[0].text.strip())
            if(test3 != 'Default') :
                tmp.append(i.select(test3)[0].text.strip())
            if(test4 != 'Default') :
                tmp.append(i.select(test4)[0].text.strip())
            if(test5 != 'Default') :
                tmp.append(i.select(test5)[0].text.strip())
            else : 
                print("크롤링 실험중 입니다.")

           
            result.append(tmp)       


        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test6 : # 넣는값
                    self.ObLs[i][2] = result
                else : 
                    print('담긴값이 없습니다')

    

        t_result = "\n".join(map(str,result))
        self.T_text.append(t_result)
        print(result)

        
        print("Clawling 기능이 실행되었습니다.")


    def ImageCrawling(self,str1,str2,str3,str4):
        
        # 완료 06-20 / assign 오류 해결

        test1 = str1
        test2 = str2
        test3 = str3
        test4 = str4

        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test1 : # 넣는값
                    test1 = self.ObLs[i][2]
                else : 
                    print('')

                if self.ObLs[i][1] == test2 : # 넣는값
                    test2 = self.ObLs[i][2]
                else : 
                    print('')

                if self.ObLs[i][1] == test3 : # 넣는값
                    test3 = self.ObLs[i][2]
                else : 
                    print('')

                if self.ObLs[i][1] == test4 : # 넣는값
                    test4 = self.ObLs[i][2]
                else : 
                    print('')


        html = self.driver.page_source
        soup = BeautifulSoup(html,'html.parser')

        n = 1

        img = soup.find_all(class_= test1)

        for i in img :
            imgurl = i[test2]
            with urlopen(imgurl) as f:
                with open(test3 +"/" + str(n) + test4 , 'wb')as h : 
                    img = f.read() 
                    h.write(img) 
            n+=1 


    def InstaImageCrawling(self,str1,str2):

        test1 = str1
        test2 = str2

        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test1 : # 넣는값
                    test1 = self.ObLs[i][2]
                else : 
                    print('')

                if self.ObLs[i][1] == test2 : # 넣는값
                    test2 = self.ObLs[i][2]
                else : 
                    print('')
        
        html = self.driver.page_source
        soup = BeautifulSoup(html,'html.parser')

        insta = soup.select('.v1Nh3.kIKUG._bz0w')

        n = 1

        for i in insta :
            imgurl = i.select_one('.KL4Bh').img['src']
            with urlopen(imgurl) as f:
                with open(test1+"/"+str(n)+test2,'wb') as h:
                    img = f.read()
                    h.write(img)
            n+=1
            print(imgurl)

        



        print('InstaImageCrawling 기능이 실행되었습니다')
    



    def ExcelWrite(self,str1,str2,str3):
        
        # 완료 06-20 / assign 오류 해결

        test1 = str1
        test2 = str2
        test3 = str3
        

        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test1 : # 넣는값
                    test1 = self.ObLs[i][2]
                else : 
                    print('')

                if self.ObLs[i][1] == test2 : # 넣는값
                    test2 = self.ObLs[i][2]
                else : 
                    print('')

                if self.ObLs[i][1] == test3 : # 넣는값
                    test3 = self.ObLs[i][2]
                else : 
                    print('')

        data = pd.DataFrame(list(test1))
        data1 = "".join(map(str,test2))
        data2 = data1.split(',')
        data.columns = data2
        data.to_excel(test3, index = False)

    def ExcelRead(self,str1,str2):
        
        test1 = str1
        test2 = str2

        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test1 : # 넣는값
                    test1 = self.ObLs[i][2]
                else : 
                    print('')

        test = pd.read_excel(test1)
        test3 = test.values.tolist()

        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test2 : # 넣는값
                    self.ObLs[i][2] = test3
                else : 
                    print('담긴값이 없습니다')
        
        result = "\n".join(map(str,test3)) 
        self.T_text.append(result)

    def CsvRead(self,str1,str2):

        # 완료 06-20 / assign 오류 해결

        test1 = str1
        test2 = str2

        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test1 : # 넣는값
                    test1 = self.ObLs[i][2]
                else : 
                    print('')

        test = pd.read_csv(test1,encoding = 'cp949')
        test3 = test.values.tolist()

        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test2 : # 넣는값
                    self.ObLs[i][2] = test3
                else : 
                    print('담긴값이 없습니다')
        
        result = "\n".join(map(str,test3)) 
        self.T_text.append(result)
        

        

    
    def CsvWrite(self,str1,str2,str3):

        # 완료 06-20 / assign 오류 해결 
        
        test1 = str1
        test2 = str2
        test3 = str3
       


        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test1 : # 넣는값
                    test1 = self.ObLs[i][2]
                else : 
                    print('')

                if self.ObLs[i][1] == test2 : # 넣는값
                    test2 = self.ObLs[i][2]
                else : 
                    print('')

                if self.ObLs[i][1] == test3 : # 넣는값
                    test3 = self.ObLs[i][2]
                else : 
                    print('')

        
        data = pd.DataFrame(list(test1))
        data1 = "".join(map(str,test2))
        data2 = data1.split(',')
        data.columns = data2
        data.to_csv(test3, index = False , encoding = 'cp949')

    def RowDropNa(self,str1) :

        # 완료 06-20 / assign 오류 해결
        #  
        test1 = str1
        
        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test1 : # 넣는값
                    test1 = self.ObLs[i][2]
                else : 
                    print('')

        test1 = pd.DataFrame(list(test1))

        test1 = test1.dropna()
        print(test1)

        print('rowdropna가 실행되었습니다')
        

        
    def ColumnDropNa(self,str1) :

        # 완료 06-20 / assign 오류 해결
        #  
        test1 = str1

        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test1 : # 넣는값
                    test1 = self.ObLs[i][2]
                else : 
                    print('')

        test1 = pd.DataFrame(list(test1))

        test1 = test1.dropna(axis = 1)
        print(test1)

        print('columndropna가 실행되었습니다')
    
    def FillNa(self,str1,str2) :

        # 완료 06-20 / assign 오류 해결
        #  
        test1 = str1
        test2 = str2

        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test1 : # 넣는값
                    test1 = self.ObLs[i][2]
                else : 
                    print('')

                if self.ObLs[i][1] == test2 : # 넣는값
                    test2 = self.ObLs[i][2]
                else : 
                    print('')

        test1 = pd.DataFrame(list(test1))

        test1 = test1.fillna(test2)
        print(test1)
        

        print('Fillna가 실행되었습니다')

        
    def MaxWin(self) :

        # 완료 06-20 / assign 오류 해결
        #  
        self.driver.maximize_window()


    def TimeSleep(self,int1) :
        
        # 완료 06-20 / assign 오류 해결 

        test1 = int1

        for i in range((len(self.ObLs))): # self.obls 값
            if self.ObLs[i][0] == 'Assign':
                if self.ObLs[i][1] == test1 : # 넣는값
                    test1 = self.ObLs[i][2]
                else : 
                    print('')

        

        time.sleep(test1)


    def Click(self,str1) :

        # 완료 06-20 / assign 오류 해결
        test1 = str1

        for i in range((len(self.ObLs))): # self.obls 값
            if self.ObLs[i][0] == 'Assign':
                if self.ObLs[i][1] == test1 : # 넣는값
                    test1 = self.ObLs[i][2]
                else : 
                    print('')
        

        self.driver.find_element_by_xpath(test1).click()
        

        print("Click이 실행되었습니다")
    
    def MousePosition(self) :

        # 완료 06-20 / assign 오류 해결

        test1 = pyautogui.position()
        
        result = str(test1)
        self.T_text.append(result)

        print("MousePosition이 실행되었습니다")
    
    def MoveToPosition(self,str1,str2) :

        # 완료 06-20 / assign 오류 해결
        test1 = str1
        test2 = str2

        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test1 : # 넣는값
                    test1 = self.ObLs[i][2]
                else : 
                    print('')

                if self.ObLs[i][1] == test2 : # 넣는값
                    test2 = self.ObLs[i][2]
                else : 
                    print('')
        
        pyautogui.moveTo(int(test1),int(test2))

        print("MoveToPosition 실행되었습니다")
    
    def MoveToPositionClick(self,str1,str2) :

        # 완료 06-20 / assign 오류 해결
        test1 = str1
        test2 = str2

        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test1 : # 넣는값
                    test1 = self.ObLs[i][2]
                else : 
                    print('')

                if self.ObLs[i][1] == test2 : # 넣는값
                    test2 = self.ObLs[i][2]
                else : 
                    print('')
        
        pyautogui.click(int(test1),int(test2))

        print("MoveToPositionClick 실행되었습니다")
    
    def MoveToPositionDoubleClick(self,str1,str2) :

        # 완료 06-20 / assign 오류 해결
        test1 = str1
        test2 = str2

        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test1 : # 넣는값
                    test1 = self.ObLs[i][2]
                else : 
                    print('')

                if self.ObLs[i][1] == test2 : # 넣는값
                    test2 = self.ObLs[i][2]
                else : 
                    print('')
        
        pyautogui.doubleClick(int(test1),int(test2))

        print("MoveToPositionDoubleClick 실행되었습니다")

    





    def MakeClipBoard(self,str1,str2,str3) :
        
        # 완료 06-20 / assign 오류 해결

        test1 = str1
        test2 = str2
        test3 = str3

        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test1 : # 넣는값
                    test1 = self.ObLs[i][2]
                else : 
                    print('')

                if self.ObLs[i][1] == test2 : # 넣는값
                    test2 = self.ObLs[i][2]
                else : 
                    print('')

                if self.ObLs[i][1] == test3 : # 넣는값
                    test3 = self.ObLs[i][2]
                else : 
                    print('')

        
        f = open(test1, mode = test2, encoding = test3)

        print("MakeClipBoard이 실행되었습니다")

    
    def FRead(self,str) :

        # 완료 06-20 / assign 오류 해결
        
        print("Fread이 실행되었습니다")

    

    def Resize(self,str1,str2,str3,str4):

        # 완료 06-20 / assign 오류 해결
        
        test1 = str1
        test2 = str2
        test3 = str3
        test4 = str4

        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test1 : # 넣는값
                    test1 = self.ObLs[i][2]
                else : 
                    print('')

                if self.ObLs[i][1] == test2 : # 넣는값
                    test2 = self.ObLs[i][2]
                else : 
                    print('')

                if self.ObLs[i][1] == test3 : # 넣는값
                    test3 = self.ObLs[i][2]
                else : 
                    print('')

                if self.ObLs[i][1] == test4 : # 넣는값
                    test4 = self.ObLs[i][2]
                else : 
                    print('')


        file_list = os.listdir(test3)

        img_list = []
        for el in file_list:
            splt = el.split(".")
            ext = splt.pop()
            if ext in "jpg jpeg png bmp JPG JPEG PNG BMP":
                img_list.append(el)

        total_image = len(img_list)
        
        index = 1
        result = []
        for name in img_list :

            img = Image.open('%s%s'%(test3+"/", name)) 
            img_array = np.array(img) 
            img_resize = cv2.resize(img_array, (int(test1),int(test2)), interpolation = cv2.INTER_AREA) 
            img = Image.fromarray(img_resize) 
            img.save('%s%s'%(test4 + "/", name)) 

            result.append(('Resize :' + name + '   ' + str(index) + '/' + str(total_image)))
            index = index + 1

        r_result = "\n".join(map(str,result))
        self.T_text.append(r_result)


        

    def ImgSquare(self,str1,str2):

        # 완료 06-20 / assign 오류 해결

        test1 = str1
        test2 = str2

        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test1 : # 넣는값
                    test1 = self.ObLs[i][2]
                else : 
                    print('')

                if self.ObLs[i][1] == test2 : # 넣는값
                    test2 = self.ObLs[i][2]
                else : 
                    print('')

        

        files = os.listdir(test1)

        for el in files:
            splt = el.split(".")
            ext = splt.pop()
            if ext in "jpg jpeg png bmp JPG JPEG PNG BMP": 
                image = Image.open(test1 + "/" + el) 
                x, y = image.size 
                if x > y :
                    new_size = x 
                    x_offset = 0 
                    y_offset = int((x-y)/2) 
                elif y > x: 
                    new_size = y 
                    x_offset = int((y-x) / 2) 
                    y_offset = 0
            
                background_color = "white"  
                new_image = Image.new("RGBA", (new_size, new_size), background_color) 
                new_image.paste(image, (x_offset, y_offset)) 

       
                outfile_name = ".".join(splt) + ".png" 
                new_image.save(test2 + "/" + outfile_name)


        print('ImgSquare가 실행되었습니다')



    
    def ConvertGray(self,str1,str2):

        # 완료 06-20 / assign 오류 해결
        
        
        test1 = str1
        test2 = str2

        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test1 : # 넣는값
                    test1 = self.ObLs[i][2]
                else : 
                    print('')

                if self.ObLs[i][1] == test2 : # 넣는값
                    test2 = self.ObLs[i][2]
                else : 
                    print('')


        file_list = os.listdir(test1)


        img_list = []
        for el in file_list:
            splt = el.split(".")
            ext = splt.pop()
            if ext in "jpg jpeg png bmp JPG JPEG PNG BMP":
                img_list.append(el)

        total_image = len(img_list)
        
        index = 1
        result = []

        for name in img_list :

            img = Image.open('%s%s'%(test1+"/", name))
            img_array = np.array(img)
            #image = Image.fromarray(im2).convert('RGB')
            img = Image.fromarray(img_array).convert('L') #위의 이미지 리사이즈하는 기능에서 여기만 바뀜 *상대경로만(str) 있으면 전체 다 회색조로 변환
            img.save('%s%s'%(test2 + "/" , name))

            result.append(('ConvertGray :'+ name + '   ' + str(index) + '/' + str(total_image)))
            index = index + 1

        t_result = "\n".join(map(str,result))
        self.T_text.append(t_result)

        print('ConvertGray 기능이 실행되었습니다')


    def ThresHolding(self,str1,str2):

        # 완료 06-20 / assign 오류 해결
        
        test1 = str1
        test2 = str2

        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test1 : # 넣는값
                    test1 = self.ObLs[i][2]
                else : 
                    print('')

                if self.ObLs[i][1] == test2 : # 넣는값
                    test2 = self.ObLs[i][2]
                else : 
                    print('')

        
        orpath = test1
        path = orpath + "/" 
        output_dir =  test2

        file_list = os.listdir(path)

        img_list = []

        for el in file_list:
            splt = el.split(".")
            ext = splt.pop()
            if ext in "jpg jpeg png bmp JPG JPEG PNG BMP":
                img_list.append(el)
        
        total_image = len(img_list)

        imagePaths = [os.path.join(path,file_name) for file_name in os.listdir(path)]
        index = 0

        rgb3 = 255
        rgb4 = 99
        rgb5 = 10

        max_output_value = rgb3   
        neighborhood_size = rgb4   
        subtract_from_mean = rgb5

        result= []

        for name in img_list :

            index = index + 1

            img = Image.open(path+name)
            img_array = np.array(img, 'uint8')

            image_binarized = cv2.adaptiveThreshold(img_array,
                                       max_output_value,
                                       cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv2.THRESH_BINARY,
                                       neighborhood_size,
                                       subtract_from_mean)
            
            cv2.imwrite(output_dir + "/" + name, image_binarized)

            result.append((name + '   ' + str(index) + '/' + str(total_image)))
            
        
        t_result = "\n".join(map(str,result))
        self.T_text.append(t_result)
        


        print('이미지 이진화가 완료되었습니다. ')



    def EqualizeHist(self,str1,str2):

        # 완료 06-20 / assign 오류 해결
        
        test1 = str1
        test2 = str2

        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test1 : # 넣는값
                    test1 = self.ObLs[i][2]
                else : 
                    print('')

                if self.ObLs[i][1] == test2 : # 넣는값
                    test2 = self.ObLs[i][2]
                else : 
                    print('')

        
        orpath = test1
        path = orpath + "/"
        output_dir = test2

        file_list = os.listdir(orpath)
        img_list = []

        for el in file_list:
            splt = el.split(".")
            ext = splt.pop()
            if ext in "jpg jpeg png bmp JPG JPEG PNG BMP":
                img_list.append(el)
        
        total_image = len(img_list)
        index = 0
        result = []

        for name in img_list :
            index = index + 1

            img = Image.open(path+name)
            img_array = np.array(img)

            img_array = np.array(img, 'uint8')
            image_enhanced = cv2.equalizeHist(img_array) 
    
            cv2.imwrite(output_dir + "/" + name, image_enhanced)

            result.append((name + '   ' + str(index) + '/' + str(total_image)))
        

        t_result = "\n".join(map(str,result))
        self.T_text.append(t_result)




        print('EqualizeHist 가 실행되었습니다.')



    def ColorEqualizeHist(self,str1,str2):

        test1 = str1
        test2 = str2

        for i in range((len(self.ObLs))): # self.obls 값

                if self.ObLs[i][0] == 'Assign':

                    if self.ObLs[i][1] == test1 : # 넣는값
                        test1 = self.ObLs[i][2]
                    else : 
                        print('')

                    if self.ObLs[i][1] == test2 : # 넣는값
                        test2 = self.ObLs[i][2]
                    else : 
                        print('')
    
        orpath = test1

        path = orpath + "/"

        output_dir = test2

        file_list = os.listdir(path)

        img_list = []

        for el in file_list:
            splt = el.split(".")
            ext = splt.pop()
            if ext in "jpg jpeg png bmp JPG JPEG PNG BMP":
                img_list.append(el)

        total_image = len(img_list)

        index = 0
        result = []

        for name in img_list :
            
            index = index+1
            img = Image.open(path+name)
            img_array = np.array(img)
            img_array = np.array(img, 'uint8')
            image_yuv = cv2.cvtColor(img_array, cv2.COLOR_BGR2YUV)
            image_yuv[:, :, 0] = cv2.equalizeHist(image_yuv[:, :, 0])
            image_rgb = cv2.cvtColor(image_yuv, cv2.COLOR_YUV2RGB)
            cv2.imwrite(output_dir + "/" + name, image_rgb)
            result.append((name + '   ' + str(index) + '/' + str(total_image)))


        t_result = "\n".join(map(str,result))
        self.T_text.append(t_result)

    def Blur(self,str1,str2,str3,str4) :

        test1 = str1
        test2 = str2
        test3 = str3
        test4 = str4

        for i in range((len(self.ObLs))): # self.obls 값

                if self.ObLs[i][0] == 'Assign':

                    if self.ObLs[i][1] == test1 : # 넣는값
                        test1 = self.ObLs[i][2]
                    else : 
                        print('')

                    if self.ObLs[i][1] == test2 : # 넣는값
                        test2 = self.ObLs[i][2]
                    else : 
                        print('')
                    
                    if self.ObLs[i][1] == test3 : # 넣는값
                        test3 = self.ObLs[i][2]
                    else : 
                        print('')

                    if self.ObLs[i][1] == test4 : # 넣는값
                        test4 = self.ObLs[i][2]
                    else : 
                        print('')

        
        orpath = test3
        path = orpath + "/"
        output_dir = test4

        blur_x = test1
        blur_y = test2

        file_list = os.listdir(path)
        img_list = []

        for el in file_list:
            splt = el.split(".")
            ext = splt.pop()
            if ext in "jpg jpeg png bmp JPG JPEG PNG BMP":
                img_list.append(el)


        total_image = len(img_list)
        index = 0
        result = []

        for name in img_list :
            index = index + 1
            img = cv2.imread(path+name) 
            img_array = np.array(img)
            image_blurry = cv2.blur(img_array, (int(blur_x),int(blur_y))) 
            cv2.imwrite(output_dir + "/" + name, image_blurry)
            result.append((name + '   ' + str(index) + '/' + str(total_image)))
        
        t_result = "\n".join(map(str,result))
        self.T_text.append(t_result)


    def Blur_2D(self,str1,str2,str3) :
        
        test1 = str1
        test2 = str2
        test3 = str3

        for i in range((len(self.ObLs))): # self.obls 값

                if self.ObLs[i][0] == 'Assign':

                    if self.ObLs[i][1] == test1 : # 넣는값
                        test1 = self.ObLs[i][2]
                    else : 
                        print('')

                    if self.ObLs[i][1] == test2 : # 넣는값
                        test2 = self.ObLs[i][2]
                    else : 
                        print('')
                    
                    if self.ObLs[i][1] == test3 : # 넣는값
                        test3 = self.ObLs[i][2]
                    else : 
                        print('')

        orpath = test2
        path = orpath + "/"
        output_dir = test3

        file_list = os.listdir(path)

        img_list = []

        for el in file_list:
            splt = el.split(".")
            ext = splt.pop()
            if ext in "jpg jpeg png bmp JPG JPEG PNG BMP":
                img_list.append(el)

        total_image = len(img_list)
        index = 0

        value_2d = int(test1)
        kernel = np.ones((value_2d, value_2d)) / value_2d**2
        result = []

        for name in img_list :

            index = index + 1
            img = cv2.imread(path+name) 
            img_array = np.array(img)
            image_kernel = cv2.filter2D(img_array, -1, kernel) 
            cv2.imwrite(output_dir + "/" + name, image_kernel)
            result.append((name + '   ' + str(index) + '/' + str(total_image)))

        t_result = "\n".join(map(str,result))
        self.T_text.append(t_result)






        print('Blur_2D 기능이 실행되었습니다.')


    def GausianBlur(self,str1,str2,str3,str4,str5):

        test1 = str1
        test2 = str2
        test3 = str3
        test4 = str4
        test5 = str5

        for i in range((len(self.ObLs))): # self.obls 값

                if self.ObLs[i][0] == 'Assign':

                    if self.ObLs[i][1] == test1 : # 넣는값
                        test1 = self.ObLs[i][2]
                    else : 
                        print('')

                    if self.ObLs[i][1] == test2 : # 넣는값
                        test2 = self.ObLs[i][2]
                    else : 
                        print('')
                    
                    if self.ObLs[i][1] == test3 : # 넣는값
                        test3 = self.ObLs[i][2]
                    else : 
                        print('')

                    if self.ObLs[i][1] == test4 : # 넣는값
                        test4 = self.ObLs[i][2]
                    else : 
                        print('')
                    
                    if self.ObLs[i][1] == test5 : # 넣는값
                        test5 = self.ObLs[i][2]
                    else : 
                        print('')

        
        orpath = test1
        path = orpath + "/"
        output_dir = test2

        file_list = os.listdir(path)

        img_list = []

        for el in file_list:
            splt = el.split(".")
            ext = splt.pop()
            if ext in "jpg jpeg png bmp JPG JPEG PNG BMP":
                img_list.append(el)

        total_image = len(img_list)
        index = 0

        k_width = test3 
        k_height = test4  
        sigma = test5

        result = []

        for name in img_list :
            index = index + 1

            img = cv2.imread(path+name)
            img_array = np.array(img)

            img_array = np.array(img, 'uint8')
            image_gaussian = cv2.GaussianBlur(img_array, (int(k_width),int(k_height)), int(sigma)) #가우시안 블러 기능
            cv2.imwrite(output_dir + "/" + name, image_gaussian)
            result.append((name + '   ' + str(index) + '/' + str(total_image)))

        t_result = "\n".join(map(str,result))
        self.T_text.append(t_result) 

    def MedianBlur(self,str1,str2,str3) :
        
        test1 = str1
        test2 = str2
        test3 = str3

        for i in range((len(self.ObLs))): # self.obls 값

                if self.ObLs[i][0] == 'Assign':

                    if self.ObLs[i][1] == test1 : # 넣는값
                        test1 = self.ObLs[i][2]
                    else : 
                        print('')

                    if self.ObLs[i][1] == test2 : # 넣는값
                        test2 = self.ObLs[i][2]
                    else : 
                        print('')
                    
                    if self.ObLs[i][1] == test3 : # 넣는값
                        test3 = self.ObLs[i][2]
                    else : 
                        print('')
        
        
        orpath = test1
        path = orpath + "/"
        output_dir = test2

        file_list = os.listdir(path)

        img_list = []

        for el in file_list:
            splt = el.split(".")
            ext = splt.pop()
            if ext in "jpg jpeg png bmp JPG JPEG PNG BMP":
                img_list.append(el)

        total_image = len(img_list)
        index = 0
        Kernel_size = test3

        result = []

        for name in img_list :
            index = index + 1
            img = cv2.imread(path+name)
            img_array = np.array(img, 'uint8')
            image_median = cv2.medianBlur(img_array, int(Kernel_size)) 
            cv2.imwrite(output_dir + "/" + name, image_median)
            result.append((name + '   ' + str(index) + '/' + str(total_image)))

        t_result = "\n".join(map(str,result))
        self.T_text.append(t_result) 

    def BilateralBlur(self,str1,str2,str3,str4,str5):

        test1 = str1
        test2 = str2
        test3 = str3
        test4 = str4
        test5 = str5

        for i in range((len(self.ObLs))): # self.obls 값

                if self.ObLs[i][0] == 'Assign':

                    if self.ObLs[i][1] == test1 : # 넣는값
                        test1 = self.ObLs[i][2]
                    else : 
                        print('')

                    if self.ObLs[i][1] == test2 : # 넣는값
                        test2 = self.ObLs[i][2]
                    else : 
                        print('')
                    
                    if self.ObLs[i][1] == test3 : # 넣는값
                        test3 = self.ObLs[i][2]
                    else : 
                        print('')

                    if self.ObLs[i][1] == test4 : # 넣는값
                        test4 = self.ObLs[i][2]
                    else : 
                        print('')
                    
                    if self.ObLs[i][1] == test5 : # 넣는값
                        test5 = self.ObLs[i][2]
                    else : 
                        print('')

        orpath = test1
        path = orpath + "/"
        output_dir = test2

        file_list = os.listdir(path)
        img_list = []

        for el in file_list:
            splt = el.split(".")
            ext = splt.pop()
            if ext in "jpg jpeg png bmp JPG JPEG PNG BMP":
                img_list.append(el)

        total_image = len(img_list)
        index = 0

        result = []

        pixel = test3 
        color_space = test4 
        sigma = test5

        for name in img_list :
            index = index + 1
            img = cv2.imread(path+name)
            img_array = np.array(img, 'uint8')
            image_bilateral = cv2.bilateralFilter(img_array, int(pixel),int(color_space),int(sigma)) #쌍방 필터 기능
            cv2.imwrite(output_dir + "/" + name, image_bilateral)
            result.append((name + '   ' + str(index) + '/' + str(total_image)))
        
        t_result = "\n".join(map(str,result))
        self.T_text.append(t_result)

    def Filter_Content(self,str1,str2):
        
        test1 = str1
        test2 = str2 

        for i in range((len(self.ObLs))): # self.obls 값

                if self.ObLs[i][0] == 'Assign':

                    if self.ObLs[i][1] == test1 : # 넣는값
                        test1 = self.ObLs[i][2]
                    else : 
                        print('')
        
        content = []
        filtered_content = []

        # 읽어온 파일의 데이터 2차원 배열로 저장
        for i in list(test1) :
            content.append(i)

        # 불필요한 부분 제거 결과값 2차원 배열
        for i in content:
            filtered_content.append((str(i).replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('\n','')))
        
        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test2 : # 넣는값
                    self.ObLs[i][2] = filtered_content
                else : 
                    print('담긴값이 없습니다')
        t_result = "\n".join(map(str,filtered_content))
        self.T_text.append(t_result)


    def Morphs(self,str1,str2):
        
        test1 = str1
        test2 = str2

        for i in range((len(self.ObLs))): # self.obls 값

                if self.ObLs[i][0] == 'Assign':

                    if self.ObLs[i][1] == test1 : # 넣는값
                        test1 = self.ObLs[i][2]
                    else : 
                        print('')
        
        Okt = konlpy.tag.Okt()
        Okt_morphs = []

        for i in list(test1) :
            Okt_morphs.append((Okt.pos(i)))
        

        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test2 : # 넣는값
                    self.ObLs[i][2] = Okt_morphs
                else : 
                    print('담긴값이 없습니다')
        
        t_result = "\n".join(map(str,Okt_morphs))
        self.T_text.append(t_result)


    def Extract_Word(self,str1,str2):

        test1 = str1
        test2 = str2

        for i in range((len(self.ObLs))): # self.obls 값

                if self.ObLs[i][0] == 'Assign':

                    if self.ObLs[i][1] == test1 : # 넣는값
                        test1 = self.ObLs[i][2]
                    else : 
                        print('')
        
        Noun_words = []

        for i in list(test1) :
            Noun_words_1 = []
            for word, pos in i:
                if pos == 'Noun':
                    Noun_words_1.append(word)
            Noun_words.append(Noun_words_1)
        
        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test2 : # 넣는값
                    self.ObLs[i][2] = Noun_words
                else : 
                    print('담긴값이 없습니다')
        
        t_result = "\n".join(map(str,Noun_words))
        self.T_text.append(t_result)        

    def Counter_Word(self,str1,str2):

        test1 = str1
        test2 = str2

        for i in range((len(self.ObLs))): # self.obls 값

                if self.ObLs[i][0] == 'Assign':

                    if self.ObLs[i][1] == test1 : # 넣는값
                        test1 = self.ObLs[i][2]
                    else : 
                        print('')

        result= []

        for i in test1 :
            c = Counter(i)
            result.append((c.most_common(100))) # 상위 100개 출력하기
        
        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test2 : # 넣는값
                    self.ObLs[i][2] = result
                else : 
                    print('담긴값이 없습니다')
        
        t_result = "\n".join(map(str,result))
        self.T_text.append(t_result)
    
    def WordCloud(self,str1):
        
        test1 = str1

        for i in range((len(self.ObLs))): # self.obls 값

                if self.ObLs[i][0] == 'Assign':

                    if self.ObLs[i][1] == test1 : # 넣는값
                        test1 = self.ObLs[i][2]
                    else : 
                        print('')
        
        FONT_PATH = 'C:/Windows/Fonts/malgun.ttf' # For Korean characters


        noun_text = ''
        for i in test1:
            for word in i:
                noun_text = noun_text +' '+word
        
        wordcloud = WordCloud(max_font_size=60, relative_scaling=.5, font_path=FONT_PATH).generate(noun_text) # generate() 는 하나의 string value를 입력 받음
        plt.figure()
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()

    
    
    def Ocr_Eng(self,str1):
        
        # 완료 06-20 / assign 오류 해결

        test1 = str1

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test1 : # 넣는값
                    test1 = self.ObLs[i][2]
                else : 
                    print('')

        # add = str 
        im = Image.open(test1)
        addim = pytesseract.image_to_string(im)
        self.T_text.append(addim)



    def Ocr_Kor(self,str1,str2):

        # 완료 06-20 / assign 오류 해결

        test1 = str1
        test2 = str2

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test1 : # 넣는값
                    test1 = self.ObLs[i][2]
                else : 
                    test1 = str1
                
        
        orpath = test1
        path = orpath + "/"

        result = []

        file_list = os.listdir(path)
        img_list = []

        for el in file_list:
            splt = el.split(".")
            ext = splt.pop()
            if ext in "jpg jpeg png bmp JPG JPEG PNG BMP":
                img_list.append(el)
        
        for name in img_list :

            img = Image.open(path+name)
            img_array = np.array(img)
            
            addim = pytesseract.image_to_string(img_array,lang='kor')
            result.append(addim)
        
        for i in range((len(self.ObLs))): # self.obls 값

            if self.ObLs[i][0] == 'Assign':

                if self.ObLs[i][1] == test2 : # 넣는값
                    self.ObLs[i][2] = result
                else : 
                    print('담긴값이 없습니다')

        t_result = "\n".join(map(str,result))
        self.T_text.append(t_result)
        



    def AddScript(self):

        # 완료 06-17
        print("AddScript 버튼이 실행되었습니다.")
        self.Py_Text.toPlainText()
        test = self.Py_Text.toPlainText()


        self.te_1.addItem("Script")

        print("add item이 성공하였습니다.")
        


        test1 = self.DicAddScript['DicAddScript']['DicAddScriptName'][0] 
        test2 = test

        self.ObLs.append([test1,test2])
        



    def S_Script(self,sc):

        # 완료 06-17
        code = compile(sc,'<string>','exec')
        exec(code)
        
        print("S_Script 버튼이 실행되었습니다.")


    


    

    def RemoveList(self):
        # 완료 06-17
        try:
            
            for i in self.te_1.selectedIndexes():
                ii = str(self.te_1.itemFromIndex(i).text())

            it = self.te_1.currentRow()
            self.te_1.takeItem(it)

            #해당되는 리스트 값을 삭제
            del self.ObLs[it]

        except :
            test = '현재 리스트에 삭제할 항목이 없습니다'
            self.P_text.append(test)
        
       

    def RemoveListAll(self):
        # 완료 06-17
        
        try :

            self.te_1.clear()
            self.ObLs = []

        except :

            test = '현재 리스트에 삭제할 항목이 없습니다'
            self.P_text.append(test)
       
    ################## 삭제할 예정####################
    
    def Home(self) :
        

        self.groupBox1.hide()
        self.groupBox2.hide()
        self.groupBox3.hide()
        self.groupBox4.hide()
        self.groupBox5.hide()
        self.groupBox6.hide()
        self.groupBox7.hide()
        self.Sub_Home()

    ################## 삭제할 예정####################



    ################## 삭제할 예정####################
    ###################################################
    def Sub_Home(self):


        self.groupBox8 = QGroupBox('')

        self.tsbt1 = QPushButton("메인 화면으로 돌아가기")
        self.tsbt2 = QPushButton("파일 저장 하기")
        self.tsbt3 = QPushButton("파일 불러오기")
        self.tsbt4 = QPushButton("Help")

        self.tsbt1.setFixedSize(300,80)
        self.tsbt2.setFixedSize(300,80)
        self.tsbt3.setFixedSize(300,80)
        self.tsbt4.setFixedSize(300,80)

        self.tsbt1.setStyleSheet('Color : black; font : 20pt; background-color:white; border-radius:30px')
        self.tsbt2.setStyleSheet('Color : black; font : 20pt; background-color:white; border-radius:30px')
        self.tsbt3.setStyleSheet('Color : black; font : 20pt; background-color:white; border-radius:30px')
        self.tsbt4.setStyleSheet('Color : black; font : 20pt; background-color:white; border-radius:30px')

        
        self.tsbt1.clicked.connect(self.ReloadMain)
        self.tsbt2.clicked.connect(self.FileSave)
        self.tsbt3.clicked.connect(self.FileLoad)
        self.tsbt4.clicked.connect(self.Help)

        
        
        grid = QGridLayout()

    
        self.groupBox8.resize(1300, 900)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())




        self.groupBox8.setLayout(grid)

        grid.addWidget(self.tsbt1,0,0)
        grid.addWidget(self.tsbt2,2,0)
        grid.addWidget(self.tsbt3,4,0)
        grid.addWidget(self.tsbt4,6,0)
        
        self.groupBox8.show()
        self.close()
        ####################################
        ################## 삭제할 예정####################




    #####################################################################
    ############# addlist 함수 소스와 동일해야함 #########################
    #####################################################################

    def add_search(self):

        ilist = self.tmplist.selectedIndexes()

        for i in ilist:
            a = str(self.tmplist.itemFromIndex(i).text())
            self.te_1.addItem(a)

        
        if a == 'OpenBrowser' :

            test1 = self.DicOpenBrowser['DicOpenBrowser']['DicOpenBrowserName'][0]
            test2 = self.DicOpenBrowser['DicOpenBrowser']['DicOpenBrowserUrl'][0]
            
            
            self.ObLs.append([test1,test2])

        elif a == 'ImageCrawling' :
            
            test1 = self.DicImageCrawling['DicImageCrawling']['DicImageCrawlingName'][0]
            test2 = self.DicImageCrawling['DicImageCrawling']['DicImageCrawlingValues1'][0]
            test3 = self.DicImageCrawling['DicImageCrawling']['DicImageCrawlingValues2'][0]
            test4 = self.DicImageCrawling['DicImageCrawling']['DicImageCrawlingValues3'][0]
            test5 = self.DicImageCrawling['DicImageCrawling']['DicImageCrawlingValues4'][0]
            
            self.ObLs.append([test1,test2,test3,test4,test5])

        elif a == 'InstaImageCrawling' :
            
            test1 = self.DicInstaImageCrawling['DicInstaImageCrawling']['DicInstaImageCrawlingName'][0]
            test2 = self.DicInstaImageCrawling['DicInstaImageCrawling']['DicInstaImageCrawlingValues1'][0]
            test3 = self.DicInstaImageCrawling['DicInstaImageCrawling']['DicInstaImageCrawlingValues2'][0]
            
            self.ObLs.append([test1,test2,test3])


        elif a == 'MakeFolder' :

            test1 = self.DicMakeFolder['DicMakeFolder']['DicMakeFolderName'][0]
            test2 = self.DicMakeFolder['DicMakeFolder']['DicMakeFolderValue'][0]
            
            
            self.ObLs.append([test1,test2])
    

        elif a == 'PageDown' :

            test1 = self.DicPageDown['DicPageDown']['DicPageDownName'][0]
            test2 = self.DicPageDown['DicPageDown']['DicPageDownTag'][0]
            test3 = self.DicPageDown['DicPageDown']['DicPageDownCount'][0]
            
            self.ObLs.append([test1,test2,test3])

        elif a == 'ImgSquare' :

            test1 = self.DicImgSquare['DicImgSquare']['DicImgSquareName'][0]
            test2 = self.DicImgSquare['DicImgSquare']['DicImgSquareValues1'][0]
            test3 = self.DicImgSquare['DicImgSquare']['DicImgSquareValues2'][0]
            
            
            self.ObLs.append([test1,test2,test3])

            

        elif a == 'BrowserClose' :

            test1 = self.DicBrowserClose['DicBrowserClose']['DicBrowserCloseName'][0]
            test2 = self.DicBrowserClose['DicBrowserClose']['DicBrowserCloseValue'][0]
            
            
            self.ObLs.append([test1,test2])


        
        elif a == 'Assign' :

            test1 = self.DicAssign['DicAssign']['DicAssignName'][0]
            test2 = self.DicAssign['DicAssign']['DicAssignValueName'][0]
            test3 = self.DicAssign['DicAssign']['DicAssignValueVariable'][0]
            
            
            self.ObLs.append([test1,test2,test3])

            

        
        elif a == 'SetText' :

            test1 = self.DicSetText['DicSetText']['DicSetTextName'][0]
            test2 = self.DicSetText['DicSetText']['DicSetTextValues1'][0]
            test3 = self.DicSetText['DicSetText']['DicSetTextValues2'][0]
            
            
            self.ObLs.append([test1,test2,test3])


        elif a == 'For' :

            test1 = self.DicFor['DicFor']['DicForName'][0]
            test2 = self.DicFor['DicFor']['DicForValues1'][0]
            test3 = self.DicFor['DicFor']['DicForValues2'][0]
            test4 = self.DicFor['DicFor']['DicForValues3'][0]
            
            
            self.ObLs.append([test1,test2,test3,test4])



        elif a == 'TextCrawling' :

            test1 = self.DicTextCrawling['DicTextCrawling']['DicTextCrawlingName'][0]
            test2 = self.DicTextCrawling['DicTextCrawling']['DicTextCrawlingValues1'][0]
            test3 = self.DicTextCrawling['DicTextCrawling']['DicTextCrawlingValues2'][0]
            test4 = self.DicTextCrawling['DicTextCrawling']['DicTextCrawlingValues3'][0]
            test5 = self.DicTextCrawling['DicTextCrawling']['DicTextCrawlingValues4'][0]
            test6 = self.DicTextCrawling['DicTextCrawling']['DicTextCrawlingValues5'][0]
            test7 = self.DicTextCrawling['DicTextCrawling']['DicTextCrawlingValues6'][0]
            
            
            self.ObLs.append([test1,test2,test3,test4,test5,test6,test7])


        
        elif a == 'ExcelRead' :

            test1 = self.DicExcelRead['DicExcelRead']['DicExcelReadName'][0]
            test2 = self.DicExcelRead['DicExcelRead']['DicExcelReadValues1'][0]
            test3 = self.DicExcelRead['DicExcelRead']['DicExcelReadValues2'][0]
            
            self.ObLs.append([test1,test2,test3])
        
        elif a == 'ExcelWrite' :

            test1 = self.DicExcelWrite['DicExcelWrite']['DicExcelWriteName'][0]
            test2 = self.DicExcelWrite['DicExcelWrite']['DicExcelWriteValues1'][0]
            test3 = self.DicExcelWrite['DicExcelWrite']['DicExcelWriteValues2'][0]
            test4 = self.DicExcelWrite['DicExcelWrite']['DicExcelWriteValues3'][0]
           
            
            self.ObLs.append([test1,test2,test3,test4])


        elif a == 'CsvRead' :

            test1 = self.DicCsvRead['DicCsvRead']['DicCsvReadName'][0]
            test2 = self.DicCsvRead['DicCsvRead']['DicCsvReadValues1'][0]
            test3 = self.DicCsvRead['DicCsvRead']['DicCsvReadValues2'][0]
            
            self.ObLs.append([test1,test2,test3])

        
        elif a == 'CsvWrite' :

            test1 = self.DicCsvWrite['DicCsvWrite']['DicCsvWriteName'][0]
            test2 = self.DicCsvWrite['DicCsvWrite']['DicCsvWriteValues1'][0]
            test3 = self.DicCsvWrite['DicCsvWrite']['DicCsvWriteValues2'][0]
            test4 = self.DicCsvWrite['DicCsvWrite']['DicCsvWriteValues3'][0]
           
            
            
            self.ObLs.append([test1,test2,test3,test4])    


        elif a == 'MaxWin' :

            test1 = self.DicMaxWin['DicMaxWin']['DicMaxWinName'][0]
            test2 = self.DicMaxWin['DicMaxWin']['DicMaxWinValue'][0]
           
            
            self.ObLs.append([test1,test2])

        
        elif a == 'TimeSleep' :

            test1 = self.DicTimeSleep['DicTimeSleep']['DicTimeSleepName'][0]
            test2 = self.DicTimeSleep['DicTimeSleep']['DicTimeSleepValue'][0]
           
            
            self.ObLs.append([test1,test2])




        elif a == 'Click' :

            test1 = self.DicClick['DicClick']['DicClickName'][0]
            test2 = self.DicClick['DicClick']['DicClickValue'][0]
            
            
            self.ObLs.append([test1,test2])



        elif a == 'MakeClipBoard':

            test1 = self.DicMakeClipBoard['DicMakeClipBoard']['DicMakeClipBoardName'][0]
            test2 = self.DicMakeClipBoard['DicMakeClipBoard']['DicMakeClipBoardValues1'][0]
            test3 = self.DicMakeClipBoard['DicMakeClipBoard']['DicMakeClipBoardValues2'][0]
            test4 = self.DicMakeClipBoard['DicMakeClipBoard']['DicMakeClipBoardValues3'][0]

           
            self.ObLs.append([test1,test2,test3,test4])



        elif a == 'Resize':

            test1 = self.DicResize['DicResize']['DicResizeName'][0]
            test2 = self.DicResize['DicResize']['DicResizeValues1'][0]
            test3 = self.DicResize['DicResize']['DicResizeValues2'][0]
            test4 = self.DicResize['DicResize']['DicResizeValues3'][0]
            test5 = self.DicResize['DicResize']['DicResizeValues4'][0]

            self.ObLs.append([test1,test2,test3,test4,test5])


        elif a == 'ConvertGray':

            test1 = self.DicConvertGray['DicConvertGray']['DicConvertGrayName'][0]
            test2 = self.DicConvertGray['DicConvertGray']['DicConvertGrayValues1'][0]
            test3 = self.DicConvertGray['DicConvertGray']['DicConvertGrayValues1'][0]

            self.ObLs.append([test1,test2,test3])


        
        elif a == 'ThresHolding':

            test1 = self.DicThresHolding['DicThresHolding']['DicThresHoldingName'][0]
            test2 = self.DicThresHolding['DicThresHolding']['DicThresHoldingValues1'][0]
            test3 = self.DicThresHolding['DicThresHolding']['DicThresHoldingValues2'][0]

            self.ObLs.append([test1,test2,test3])

        
        elif a == 'EqualizeHist':

            test1 = self.DicEqualizeHist['DicEqualizeHist']['DicEqualizeHistName'][0]
            test2 = self.DicEqualizeHist['DicEqualizeHist']['DicEqualizeHistValues1'][0]
            test3 = self.DicEqualizeHist['DicEqualizeHist']['DicEqualizeHistValues2'][0]

            self.ObLs.append([test1,test2,test3])

        
        elif a == 'ColorEqualizeHist':

            test1 = self.DicColorEqualizeHist['DicColorEqualizeHist']['DicColorEqualizeHistName'][0]
            test2 = self.DicColorEqualizeHist['DicColorEqualizeHist']['DicColorEqualizeHistValues1'][0]
            test3 = self.DicColorEqualizeHist['DicColorEqualizeHist']['DicColorEqualizeHistValues2'][0]

            self.ObLs.append([test1,test2,test3])

        
        elif a == 'Blur':

            test1 = self.DicBlur['DicBlur']['DicBlurName'][0]
            test2 = self.DicBlur['DicBlur']['DicBlurValues1'][0]
            test3 = self.DicBlur['DicBlur']['DicBlurValues2'][0]
            test4 = self.DicBlur['DicBlur']['DicBlurValues3'][0]
            test5 = self.DicBlur['DicBlur']['DicBlurValues4'][0]

            self.ObLs.append([test1,test2,test3,test4,test5])

        elif a == 'Blur_2D':

            test1 = self.Dic2DBlur['Dic2DBlur']['Dic2DBlurName'][0]
            test2 = self.Dic2DBlur['Dic2DBlur']['Dic2DBlurValues1'][0]
            test3 = self.Dic2DBlur['Dic2DBlur']['Dic2DBlurValues2'][0]
            test4 = self.Dic2DBlur['Dic2DBlur']['Dic2DBlurValues3'][0]
            

            self.ObLs.append([test1,test2,test3,test4])

        elif a == 'GausianBlur':

            test1 = self.DicGausianBlur['DicGausianBlur']['DicGausianBlurName'][0]
            test2 = self.DicGausianBlur['DicGausianBlur']['DicGausianBlurValues1'][0]
            test3 = self.DicGausianBlur['DicGausianBlur']['DicGausianBlurValues2'][0]
            test4 = self.DicGausianBlur['DicGausianBlur']['DicGausianBlurValues3'][0]
            test5 = self.DicGausianBlur['DicGausianBlur']['DicGausianBlurValues4'][0]
            test6 = self.DicGausianBlur['DicGausianBlur']['DicGausianBlurValues5'][0]
            

            self.ObLs.append([test1,test2,test3,test4,test5,test6])

        elif a == 'MedianBlur':

            test1 = self.DicMedianBlur['DicMedianBlur']['DicMedianBlurName'][0]
            test2 = self.DicMedianBlur['DicMedianBlur']['DicMedianBlurValues1'][0]
            test3 = self.DicMedianBlur['DicMedianBlur']['DicMedianBlurValues2'][0]
            test4 = self.DicMedianBlur['DicMedianBlur']['DicMedianBlurValues3'][0]
           

            self.ObLs.append([test1,test2,test3,test4])

        elif a == 'BilateralBlur':

            test1 = self.DicBilateralBlur['DicBilateralBlur']['DicBilateralBlurName'][0]
            test2 = self.DicBilateralBlur['DicBilateralBlur']['DicBilateralBlurValues1'][0]
            test3 = self.DicBilateralBlur['DicBilateralBlur']['DicBilateralBlurValues2'][0]
            test4 = self.DicBilateralBlur['DicBilateralBlur']['DicBilateralBlurValues3'][0]
            test5 = self.DicBilateralBlur['DicBilateralBlur']['DicBilateralBlurValues4'][0]
            test6 = self.DicBilateralBlur['DicBilateralBlur']['DicBilateralBlurValues5'][0]
           
            self.ObLs.append([test1,test2,test3,test4,test5,test6])
        
  
        elif a == 'Ocr_Eng':

            test1 = self.DicOcr_Eng['DicOcr_Eng']['DicOcr_EngName'][0]
            test2 = self.DicOcr_Eng['DicOcr_Eng']['DicOcr_EngValue'][0]

            self.ObLs.append([test1,test2])


        elif a == 'Ocr_Kor':

            test1 = self.DicOcr_Kor['DicOcr_Kor']['DicOcr_KorName'][0]
            test2 = self.DicOcr_Kor['DicOcr_Kor']['DicOcr_KorValue'][0]

            self.ObLs.append([test1,test2])
        
    #####################################################################
    ############# addlist 함수 소스와 동일해야함 #########################
    #####################################################################
        
           

    def Search(self):

        self.tmplist.clear()

        kyword = self.tslb.text()
        if kyword == '':
            return
        iterator = QTreeWidgetItemIterator(self.tw)
        test = []
        while iterator.value():
            item = iterator.value()
            if not item.text(0):
                table = self.tw.itemWidget(item, 0)
            else:

                test.append(item.text(0))

            iterator += 1

        kyword2 = str(kyword).upper()

        for i in test:
            ii = str(i).upper()
            if kyword2 in ii:
                self.tmplist.addItem(str(i))
            

    ############### 삭제할 예정 #####################

    def ReloadMain(self) :

        self.show()
        self.groupBox1.show()
        self.groupBox2.show()
        self.groupBox3.show()
        self.groupBox4.show()
        self.groupBox5.show()
        self.groupBox6.show()
        self.groupBox7.show()
        self.groupBox8.hide()

    ############### 삭제할 예정 #####################

    ############### 삭제할 예정 #####################

    def Debug(self):

        print("Debug 기능이 실행되었습니다.")
    
    ############### 삭제할 예정 #####################


    def FileLoad(self):

        fname = QFileDialog.getOpenFileName(self)
        
        if fname[0]:

            with open(fname[0], 'r') as file :
                
                data = file.readline()
                self.ObLs = eval(data)
               

        # 파일 불러오기 test 중

        for i in range(len(self.ObLs)):
            test = self.ObLs[i][0]
            self.te_1.addItem(test)
                



        print("=====파일 불러오기 버튼 기능이 실행되었습니다=====")

    def FileSave(self):
        
        fname = QFileDialog.getSaveFileName(self)
        
        if fname[0]:

            with open(fname[0], 'w') as file :
                test = str(self.ObLs)
                file.write(test)
        
        else:
            QMessageBox.about(self, "Warning", "파일을 선택하지 않았습니다.")

        print("=====파일 저장 버튼 기능이 실행되었습니다=====")


    def Help(self):
        print("=====도움말 버튼 기능이 실행되었습니다=====")


    def Tab_Problem(self) :
        
        self.P_text.append("메인 화면에 추가된 항목이 없습니다 ")

    def Tab_Terminal(self , name):

        now = datetime.now()
        test = name

        self.T_text.append(str(now)+" : "+"("+test+")"+" 실행되었습니다 .")


    def Tab_Terminal_Fail(self , name):

        now = datetime.now()
        test = name

        self.T_text.append(str(now)+" : "+"("+test+")"+" 실행되지 않았습니다.")


  
    def Up(self):

        # 0626 구현중
        # 구현실패
        

        try:
            
            crow = self.te_1.currentRow()
            
            if crow > 0 :

                for i in self.te_1.selectedIndexes():
                    ii = str(self.te_1.itemFromIndex(i).text())
                    self.te_1.takeItem(crow)
                    self.te_1.insertItem(crow-1,ii)
                
                tmp = []
        
                tmp = self.ObLs[crow]
                self.ObLs[crow] = self.ObLs[crow-1]
                self.ObLs[crow-1] = tmp

                self.te_1.setCurrentRow(int(crow-1))

                print(self.ObLs)
            
            else : 

                print('up 실패')
            
        except:

            print('up 예외처리')
            
            

        
        

       

    def Down(self) :

        # 0626 구현중
        
        try:
            
            crow = self.te_1.currentRow()
            test = self.te_1.count()
            
            if crow < (test-1) :

                for i in self.te_1.selectedIndexes():
                    ii = str(self.te_1.itemFromIndex(i).text())
                    self.te_1.takeItem(crow)
                    self.te_1.insertItem(crow+1,ii)
                
                tmp = []
        
                tmp = self.ObLs[crow]
                self.ObLs[crow] = self.ObLs[crow+1]
                self.ObLs[crow+1] = tmp

                self.te_1.setCurrentRow(int(crow+1))



                print(self.ObLs)
            
            
            elif crow == (test-1):

                print('down 실패')

        except :

            
            print('down 예외처리')


    # 0624 for문 오류발견 ---- 수정중 #
    # 0620 for문 오류수정 및 해결 #

    ################################################################################################################
    ############################ start 버튼과 동일하게 기능 구현 및 a+ 부분만 추가 ##################################
    ################################################################################################################

    def EachFor(self,str1,str2,str3):
        
        test = int(str1)
        a = test-1
        b = int(str2) 
        c = int(str3)

        for i in range(c-1):
            a = test-1
            for ii in range(b-1):

                if self.ObLs[a][0] == ("OpenBrowser") :
                    
                    try :

                        ob = self.ObLs[a][1]
                        self.OpenBrowser(ob)
                        a+=1
                        
                
                    
                    except:

                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)
                        self.driver.close()


                elif self.ObLs[a][0] == ("MakeFolder") :

                    try :

                        mk = self.ObLs[a][1]
                        self.MakeFolder(mk)
                        a+=1
                    
                    except:

                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)


                elif self.ObLs[a][0] == ("PageDown") :

                    try :

                        pd1 = self.ObLs[a][1]
                        pd2 = self.ObLs[a][2]
                        self.PageDown(pd1,pd2)
                        a+=1
                    
                    except:

                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)


                elif self.ObLs[a][0] == ("BrowserClose") :

                    try:

                        bc = self.ObLs[a][1]
                        self.BrowserClose()
                        a+=1
                    
                    except:

                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)



                elif self.ObLs[a][0] == ("Assign") :

                    try:

                        as1 = self.ObLs[a][1]
                        as2 = self.ObLs[a][2]                    
                        self.Assign(as1,as2)
                        a+=1
                    
                    except:
                        
                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)

            
                elif self.ObLs[a][0] == ("SetText") :

                    try:

                        tx1 = self.ObLs[a][1]
                        tx2 = self.ObLs[a][2]

                        self.SetText(tx1,tx2)

                        a+=1

                    except:
                        
                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)

                elif self.ObLs[a][0] == ("For") :

                    try:

                        fr1 = self.ObLs[a][1]
                        fr2 = self.ObLs[a][2]
                        fr3 = self.ObLs[a][3]

                        self.EachFor(fr1,fr2,fr3)

                        a+=1
                    
                    except:
                        
                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)


                elif self.ObLs[a][0] == ("TextCrawling") :

                    try:

                        cr1 = self.ObLs[a][1]
                        cr2 = self.ObLs[a][2]
                        cr3 = self.ObLs[a][3]
                        cr4 = self.ObLs[a][4]
                        cr5 = self.ObLs[a][5]
                        cr6 = self.ObLs[a][6]

                        self.TextCrawling(cr1,cr2,cr3,cr4,cr5,cr6)
                    
                        a+=1
                    
                        
                    
                    except:
                        
                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)

                
                elif self.ObLs[a][0] == ("ImageCrawling") :

                  
                    try:

                        icr1 = self.ObLs[a][1]
                        icr2 = self.ObLs[a][2]
                        icr3 = self.ObLs[a][3]
                        icr4 = self.ObLs[a][4]
                    
                        self.ImageCrawling(icr1,icr2,icr3,icr4)

                        name = self.ObLs[a][0]
                        self.Tab_Terminal(name)
                    
                    except:
                  
                        
                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)

                elif self.ObLs[i][0] == ("InstaImageCrawling") :

                  
                    try:

                        ic1 = self.ObLs[a][1]
                        ic2 = self.ObLs[a][2]
                    
                        self.InstaImageCrawling(ic1,ic2)

                        
                    
                    except:
                  
                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)


                elif self.ObLs[a][0] == ("Resize") :

                    try:

                        rs1 = self.ObLs[a][1]
                        rs2 = self.ObLs[a][2]
                        rs3 = self.ObLs[a][3]
                        rs4 = self.ObLs[a][4]
                    
                        self.Resize(rs1,rs2,rs3,rs4)

                        a+=1
                    
                    except:
                        
                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)

                elif self.ObLs[a][0] == ("ConvertGray") :

                    
                    try:
                        cg1 = self.ObLs[a][1]
                        cg2 = self.ObLs[a][2]

                        self.ConvertGray(cg1,cg2)
                    
                        a+=1
                    
                      
                    except:
                        
                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)


                elif self.ObLs[a][0] == ("ImgSquare") :

                    try:

                        is1 = self.ObLs[a][1]
                        is2 = self.ObLs[a][2]

                        self.ImgSquare(is1,is2)
                    
                        a+=1
                    
                    
                    except:
                        
                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)


                elif self.ObLs[a][0] == ("ThresHolding") :

                    try:

                        th1 = self.ObLs[a][1]
                        th2 = self.ObLs[a][2]

                        self.ThresHolding(th1,th2)
                    
                        a+=1
                    
                   
                    
                    except:
                        
                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)

                
                elif self.ObLs[a][0] == ("EqualizeHist") :

                    try:

                        eh1 = self.ObLs[a][1]
                        eh2 = self.ObLs[a][2]

                        self.EqualizeHist(eh1,eh2)
                    
                        a+=1
                    
                   
                    except:
                        
                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)

                
                elif self.ObLs[a][0] == ("ColorEqualizeHist") :

                   
                    try:
                        ceh1 = self.ObLs[a][1]
                        ceh2 = self.ObLs[a][2]

                        self.ColorEqualizeHist(ceh1,ceh2)
                    
                        a+=1
                    
                   
                    except:
                        
                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)

                
                elif self.ObLs[a][0] == ("Blur") :

                   
                    try:

                        bl1 = self.ObLs[a][1]
                        bl2 = self.ObLs[a][2]
                        bl3 = self.ObLs[a][3]
                        bl4 = self.ObLs[a][4]

                        self.Blur(bl1,bl2,bl3,bl4)
                    
                        a+=1
                    
                   
                    except:
                        
                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)

                
                elif self.ObLs[a][0] == ("Blur_2D") :

                   
                   
                    try:
                        dbl1 = self.ObLs[a][1]
                        dbl2 = self.ObLs[a][2]
                        dbl3 = self.ObLs[a][3] 

                        self.Blur_2D(dbl1,dbl2,dbl3)
                    
                        a+=1
                    
                   
                    except:
                        
                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)

                
                elif self.ObLs[i][0] == ("GausianBlur") :

                   
                   
                    try:

                        gb1 = self.ObLs[i][1]
                        gb2 = self.ObLs[i][2]
                        gb3 = self.ObLs[i][3]
                        gb4 = self.ObLs[i][4]
                        gb5 = self.ObLs[i][5] 

                        self.GausianBlur(gb1,gb2,gb3,gb4,gb5)
                    
                        a+=1
                    
                   
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

                
                elif self.ObLs[i][0] == ("MedianBlur") :

                   
                    try:

                        mb1 = self.ObLs[i][1]
                        mb2 = self.ObLs[i][2]
                        mb3 = self.ObLs[i][3]

                        self.MedianBlur(mb1,mb2,mb3)
                    
                        a+=1
                    
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

                
                elif self.ObLs[i][0] == ("BilateralBlur") :

                   
                    try:

                        bb1 = self.ObLs[i][1]
                        bb2 = self.ObLs[i][2]
                        bb3 = self.ObLs[i][3]
                        bb4 = self.ObLs[i][4]
                        bb5 = self.ObLs[i][5]

                        self.BilateralBlur(bb1,bb2,bb3,bb4,bb5)
                    
                        a+=1
                    
                    except:
                        
                        name = self.ObLs[i][0]
                        self.Tab_Terminal_Fail(name)

                                


                elif self.ObLs[a][0] == ("ExcelWrite") :

                    try:

                        ex1 = self.ObLs[a][1]
                        ex2 = self.ObLs[a][2]
                        ex3 = self.ObLs[a][3]
                    
                        self.ExcelWrite(ex1,ex2,ex3)

                        a+=1
                    
                        
                    
                    except:
                        
                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)

                
                elif self.ObLs[a][0] == ("ExcelRead") :


                    try:

                        er1 = self.ObLs[a][1]
                        er2 = self.ObLs[a][2]
                        
                        self.ExcelRead(er1,er2)

                        a+=1
                    
                        
                    
                    except:
                        
                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)


                
                elif self.ObLs[a][0] == ("CsvWrite") :

                    try:

                        csv1 = self.ObLs[a][1]
                        csv2 = self.ObLs[a][2]
                        csv3 = self.ObLs[a][3]

                        self.CsvWrite(csv1,csv2,csv3)
                    
                        a+=1
                    
                        

                    except:
                        
                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)


                elif self.ObLs[a][0] == ("CsvRead") :

                    try:

                        cr1 = self.ObLs[a][1]
                        cr2 = self.ObLs[a][2]
                        
                        self.CsvRead(cr1,cr2)

                        a+=1
                    
                    
                    except:
                        
                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)

         

                elif self.ObLs[a][0] == ("MaxWin") :

                    try:

                        # max = self.ObLs[a][1]

                        self.MaxWin()

                        a+=1
                    
                    except:
                        
                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)


                elif self.ObLs[a][0] == ("TimeSleep") :

                    try:

                        ts = float(self.ObLs[a][1])

                        self.TimeSleep(ts)

                        a+=1

                    except:
                        
                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)


                elif self.ObLs[a][0] == ("Click") :

                    try:

                        cl = self.ObLs[a][1]
                        cr = str(cl)

                        self.Click(cr)

                        a+=1
                    
                    except:
                        
                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)

                   
                
                elif self.ObLs[a][0] == ("MakeClipBoard") :

                    try:

                        f1 = self.ObLs[a][1]
                        f2 = self.ObLs[a][2]
                        f3 = self.ObLs[a][3]

                        self.MakeClipBoard(f1,f2,f3)

                        a+=1
                    
                    except:
                        
                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)

                
                elif self.ObLs[a][0] == ("Script") :

                    try:

                        sc = self.ObLs[a][1]

                        self.S_Script(sc)

                        a+=1

                    except:
                        
                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)


                elif self.ObLs[a][0] == ("Ocr_Eng") :

                    try:

                        ocr = self.ObLs[a][1]

                        self.Ocr_Eng(ocr)

                        a+=1
                    
                    except:
                        
                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)

                
                elif self.ObLs[a][0] == ("Ocr_Kor") :

                    try:

                        ocr = self.ObLs[a][1]

                        self.Ocr_Kor(ocr)

                        a+=1
                    
                    except:
                        
                        name = self.ObLs[a][0]
                        self.Tab_Terminal_Fail(name)

                    
                
                else : 

                    print('해당하는항목이없습니다')
                   
                    

        print("for문이 실행되었습니다.")
    
    ################################################################################################################
    ############################ start 버튼과 동일하게 기능 구현 및 a+ 부부만 추가 ##################################
    ################################################################################################################

    

    






    



    
        


 
#=============================================================def 함수 정의==========================================================#





if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()