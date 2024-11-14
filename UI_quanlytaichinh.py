# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quanlytaichinh.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(975, 588)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menu_Btn = QPushButton(self.widget)
        self.menu_Btn.setObjectName(u"menu_Btn")
        self.menu_Btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.menu_Btn.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u":/icon/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu_Btn.setIcon(icon)
        self.menu_Btn.setIconSize(QSize(25, 25))
        self.menu_Btn.setCheckable(True)
        self.menu_Btn.setAutoExclusive(False)

        self.horizontalLayout_4.addWidget(self.menu_Btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.realTime = QLineEdit(self.widget)
        self.realTime.setObjectName(u"realTime")
        font = QFont()
        font.setPointSize(10)
        self.realTime.setFont(font)
        self.realTime.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout.addWidget(self.realTime)

        self.notepad_btn = QPushButton(self.widget)
        self.notepad_btn.setObjectName(u"notepad_btn")
        self.notepad_btn.setStyleSheet(u"border:none;")
        icon1 = QIcon()
        icon1.addFile(u":/icon/question_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.notepad_btn.setIcon(icon1)
        self.notepad_btn.setIconSize(QSize(23, 23))

        self.horizontalLayout.addWidget(self.notepad_btn)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.i_button = QPushButton(self.widget)
        self.i_button.setObjectName(u"i_button")
        self.i_button.setStyleSheet(u"border:none;")
        icon2 = QIcon()
        icon2.addFile(u":/icon/information_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.i_button.setIcon(icon2)
        self.i_button.setIconSize(QSize(23, 23))

        self.horizontalLayout_4.addWidget(self.i_button)


        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget_page = QStackedWidget(self.widget_3)
        self.stackedWidget_page.setObjectName(u"stackedWidget_page")
        self.stackedWidget_page.setStyleSheet(u"")
        self.quanlichichieu_page = QWidget()
        self.quanlichichieu_page.setObjectName(u"quanlichichieu_page")
        self.gridLayout_3 = QGridLayout(self.quanlichichieu_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.Quanlichitieu_lable = QLabel(self.quanlichichieu_page)
        self.Quanlichitieu_lable.setObjectName(u"Quanlichitieu_lable")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.Quanlichitieu_lable.setFont(font1)

        self.horizontalLayout_10.addWidget(self.Quanlichitieu_lable)


        self.verticalLayout_12.addLayout(self.horizontalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.them_Btn = QPushButton(self.quanlichichieu_page)
        self.them_Btn.setObjectName(u"them_Btn")
        self.them_Btn.setEnabled(True)
        self.them_Btn.setMinimumSize(QSize(50, 41))
        font2 = QFont()
        font2.setBold(True)
        self.them_Btn.setFont(font2)
        self.them_Btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color:white;\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"}")

        self.horizontalLayout_7.addWidget(self.them_Btn)

        self.themchi_Btn = QPushButton(self.quanlichichieu_page)
        self.themchi_Btn.setObjectName(u"themchi_Btn")
        self.themchi_Btn.setMinimumSize(QSize(50, 41))
        self.themchi_Btn.setFont(font2)
        self.themchi_Btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #E33220;\n"
"	color:white;\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"}")

        self.horizontalLayout_7.addWidget(self.themchi_Btn)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_7)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.Chondanhmuc_comboBox = QComboBox(self.quanlichichieu_page)
        self.Chondanhmuc_comboBox.addItem("")
        self.Chondanhmuc_comboBox.addItem("")
        self.Chondanhmuc_comboBox.addItem("")
        self.Chondanhmuc_comboBox.addItem("")
        self.Chondanhmuc_comboBox.addItem("")
        self.Chondanhmuc_comboBox.addItem("")
        self.Chondanhmuc_comboBox.addItem("")
        self.Chondanhmuc_comboBox.addItem("")
        self.Chondanhmuc_comboBox.addItem("")
        self.Chondanhmuc_comboBox.setObjectName(u"Chondanhmuc_comboBox")
        font3 = QFont()
        font3.setBold(True)
        font3.setKerning(True)
        self.Chondanhmuc_comboBox.setFont(font3)
        self.Chondanhmuc_comboBox.setStyleSheet(u"QComboBox{\n"
"	border:2px solid white;\n"
"	border-radius:8px;\n"
"	padding:1px 18px 1px 3px;\n"
"	background-color:black;\n"
"	color:white;\n"
"	height:35px;\n"
"	padding-left:15px;\n"
"	font-weight:bold;\n"
"	selection-background-color:#2980B9;\n"
"}")

        self.horizontalLayout_8.addWidget(self.Chondanhmuc_comboBox)

        self.timchitieu_lineEdit = QLineEdit(self.quanlichichieu_page)
        self.timchitieu_lineEdit.setObjectName(u"timchitieu_lineEdit")
        self.timchitieu_lineEdit.setMinimumSize(QSize(0, 39))
        self.timchitieu_lineEdit.setStyleSheet(u"background-color: rgb(154, 154, 154);")

        self.horizontalLayout_8.addWidget(self.timchitieu_lineEdit)


        self.verticalLayout_11.addLayout(self.horizontalLayout_8)


        self.verticalLayout_12.addLayout(self.verticalLayout_11)


        self.gridLayout_3.addLayout(self.verticalLayout_12, 0, 0, 1, 1)

        self.chitieu_table = QTableWidget(self.quanlichichieu_page)
        if (self.chitieu_table.columnCount() < 6):
            self.chitieu_table.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.chitieu_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.chitieu_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.chitieu_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.chitieu_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.chitieu_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.chitieu_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.chitieu_table.setObjectName(u"chitieu_table")
        self.chitieu_table.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight:bold;\n"
"	background-color:black;\n"
"	color:white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color:#F4F9FA;\n"
"}")
        self.chitieu_table.setAlternatingRowColors(True)

        self.gridLayout_3.addWidget(self.chitieu_table, 1, 0, 1, 1)

        self.stackedWidget_page.addWidget(self.quanlichichieu_page)
        self.phantichchitieu_page = QWidget()
        self.phantichchitieu_page.setObjectName(u"phantichchitieu_page")
        self.gridLayout_2 = QGridLayout(self.phantichchitieu_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.phantichchitieu_title = QLabel(self.phantichchitieu_page)
        self.phantichchitieu_title.setObjectName(u"phantichchitieu_title")
        font4 = QFont()
        font4.setPointSize(17)
        font4.setBold(True)
        self.phantichchitieu_title.setFont(font4)

        self.verticalLayout_6.addWidget(self.phantichchitieu_title)

        self.chonChartWidget = QWidget(self.phantichchitieu_page)
        self.chonChartWidget.setObjectName(u"chonChartWidget")
        self.chonChartWidget.setStyleSheet(u"QWidget{\n"
"	background-color: #C2C2C2;\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton{\n"
"	color: #94CDFF;\n"
"	border-radius:5px;\n"
"	height:30px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #0056D2;\n"
"	color:white;\n"
"	font-weight:bold;\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.chonChartWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, 0, 9, 0)
        self.circle_chart = QPushButton(self.chonChartWidget)
        self.circle_chart.setObjectName(u"circle_chart")
        icon3 = QIcon()
        icon3.addFile(u":/icon/pie-chart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/icon/pie-chart_while.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.circle_chart.setIcon(icon3)
        self.circle_chart.setIconSize(QSize(20, 20))
        self.circle_chart.setCheckable(True)
        self.circle_chart.setAutoExclusive(True)

        self.horizontalLayout_5.addWidget(self.circle_chart)

        self.chart = QPushButton(self.chonChartWidget)
        self.chart.setObjectName(u"chart")
        icon4 = QIcon()
        icon4.addFile(u":/icon/bar-chart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/icon/bar_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.chart.setIcon(icon4)
        self.chart.setIconSize(QSize(20, 20))
        self.chart.setCheckable(True)
        self.chart.setAutoExclusive(True)

        self.horizontalLayout_5.addWidget(self.chart)


        self.verticalLayout_6.addWidget(self.chonChartWidget)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.chonNgayWidget = QWidget(self.phantichchitieu_page)
        self.chonNgayWidget.setObjectName(u"chonNgayWidget")
        self.chonNgayWidget.setStyleSheet(u"QPushButton{\n"
"	background-color:#0056d2;\n"
"	color:white;\n"
"	border-radius:5px;\n"
"	height:20px;\n"
"	font-weight:bold;\n"
"}")
        self.gridLayout_6 = QGridLayout(self.chonNgayWidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_4 = QLabel(self.chonNgayWidget)
        self.label_4.setObjectName(u"label_4")
        font5 = QFont()
        font5.setPointSize(9)
        font5.setBold(True)
        self.label_4.setFont(font5)

        self.horizontalLayout_11.addWidget(self.label_4)

        self.first_date = QDateEdit(self.chonNgayWidget)
        self.first_date.setObjectName(u"first_date")
        self.first_date.setFont(font)
        self.first_date.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"alternate-background-color: rgb(85, 170, 255);\n"
"\n"
"")
        self.first_date.setCalendarPopup(True)
        self.first_date.setDate(QDate(2023, 12, 31))

        self.horizontalLayout_11.addWidget(self.first_date)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_5 = QLabel(self.chonNgayWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)

        self.horizontalLayout_12.addWidget(self.label_5)

        self.second_date = QDateEdit(self.chonNgayWidget)
        self.second_date.setObjectName(u"second_date")
        self.second_date.setFont(font)
        self.second_date.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"alternate-background-color: rgb(85, 170, 255);")
        self.second_date.setCalendarPopup(True)
        self.second_date.setDate(QDate(2024, 1, 1))

        self.horizontalLayout_12.addWidget(self.second_date)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_12)


        self.verticalLayout_7.addLayout(self.horizontalLayout_13)

        self.submit_date = QPushButton(self.chonNgayWidget)
        self.submit_date.setObjectName(u"submit_date")

        self.verticalLayout_7.addWidget(self.submit_date)


        self.gridLayout_6.addLayout(self.verticalLayout_7, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.chonNgayWidget, 0, 0, 1, 1)


        self.horizontalLayout_6.addLayout(self.gridLayout_5)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)

        self.stackedWidget_phantichchitieu = QStackedWidget(self.phantichchitieu_page)
        self.stackedWidget_phantichchitieu.setObjectName(u"stackedWidget_phantichchitieu")
        self.stackedWidget_phantichchitieu.setLineWidth(1)
        self.pie_chart = QWidget()
        self.pie_chart.setObjectName(u"pie_chart")
        self.gridLayout_4 = QGridLayout(self.pie_chart)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.bieudo_tron_Thu = QFrame(self.pie_chart)
        self.bieudo_tron_Thu.setObjectName(u"bieudo_tron_Thu")
        self.bieudo_tron_Thu.setStyleSheet(u"background-color: rgb(124, 255, 146);")
        self.bieudo_tron_Thu.setFrameShape(QFrame.StyledPanel)
        self.bieudo_tron_Thu.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.bieudo_tron_Thu, 0, 0, 1, 1)

        self.bieudo_tron_Chi = QFrame(self.pie_chart)
        self.bieudo_tron_Chi.setObjectName(u"bieudo_tron_Chi")
        self.bieudo_tron_Chi.setStyleSheet(u"background-color: rgb(255, 110, 132);")
        self.bieudo_tron_Chi.setFrameShape(QFrame.StyledPanel)
        self.bieudo_tron_Chi.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.bieudo_tron_Chi, 0, 1, 1, 1)

        self.stackedWidget_phantichchitieu.addWidget(self.pie_chart)
        self.bar_chart = QWidget()
        self.bar_chart.setObjectName(u"bar_chart")
        self.verticalLayout_10 = QVBoxLayout(self.bar_chart)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.bieudo_cot_ThuChi = QFrame(self.bar_chart)
        self.bieudo_cot_ThuChi.setObjectName(u"bieudo_cot_ThuChi")
        self.bieudo_cot_ThuChi.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.bieudo_cot_ThuChi.setFrameShape(QFrame.StyledPanel)
        self.bieudo_cot_ThuChi.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.bieudo_cot_ThuChi)

        self.stackedWidget_phantichchitieu.addWidget(self.bar_chart)

        self.gridLayout_2.addWidget(self.stackedWidget_phantichchitieu, 1, 0, 1, 1)

        self.stackedWidget_page.addWidget(self.phantichchitieu_page)
        self.goiytietkiem_page = QWidget()
        self.goiytietkiem_page.setObjectName(u"goiytietkiem_page")
        self.gridLayout_10 = QGridLayout(self.goiytietkiem_page)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.frame_2 = QFrame(self.goiytietkiem_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border:none;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        self.label_6.setFont(font6)

        self.horizontalLayout_15.addWidget(self.label_6)

        self.chonthangnam_GYTK = QComboBox(self.frame_2)
        self.chonthangnam_GYTK.addItem("")
        self.chonthangnam_GYTK.setObjectName(u"chonthangnam_GYTK")
        self.chonthangnam_GYTK.setFont(font)
        self.chonthangnam_GYTK.setStyleSheet(u"border:none;\n"
"background-color: rgb(197, 248, 255);")

        self.horizontalLayout_15.addWidget(self.chonthangnam_GYTK)


        self.gridLayout_8.addLayout(self.horizontalLayout_15, 0, 0, 1, 1)

        self.goiy_btn = QPushButton(self.frame_2)
        self.goiy_btn.setObjectName(u"goiy_btn")
        self.goiy_btn.setFont(font)
        self.goiy_btn.setStyleSheet(u"background-color:rgb(252, 255, 216);\n"
"")

        self.gridLayout_8.addWidget(self.goiy_btn, 0, 1, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QFrame{\n"
"	border-image: url(:/icon/khungGY.png) 4 6 1 2;\n"
"	background-color: rgb(184, 231, 234);\n"
"	\n"
"}\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.goiy_show = QLabel(self.frame_4)
        self.goiy_show.setObjectName(u"goiy_show")
        font7 = QFont()
        font7.setPointSize(9)
        self.goiy_show.setFont(font7)
        self.goiy_show.setStyleSheet(u"QLabel {\n"
"        border-image: none; \n"
"\n"
"    }")
        self.goiy_show.setTextFormat(Qt.AutoText)

        self.gridLayout_7.addWidget(self.goiy_show, 1, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(1)
        self.gridLayout_12 = QGridLayout(self.frame_3)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(211, 181))
        self.frame_5.setMaximumSize(QSize(231, 201))
        self.frame_5.setStyleSheet(u"QFrame {\n"
"	border-image: url(\":/icon/GYTK_bg.png\") 10 10 10 10 stretch stretch;\n"
"	border:none;\n"
"}\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.gridLayout_12.addWidget(self.frame_5, 0, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_3)


        self.gridLayout_8.addLayout(self.verticalLayout_9, 1, 0, 1, 2)


        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frame_2, 0, 0, 1, 1)

        self.stackedWidget_page.addWidget(self.goiytietkiem_page)
        self.setting_page = QWidget()
        self.setting_page.setObjectName(u"setting_page")
        self.gridLayout_11 = QGridLayout(self.setting_page)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame = QFrame(self.setting_page)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border:none;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(41, 21, 246, 51))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout_8.addWidget(self.label_7)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(50, -1, 0, -1)
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        font8 = QFont()
        font8.setPointSize(12)
        font8.setBold(True)
        self.label_8.setFont(font8)

        self.horizontalLayout_14.addWidget(self.label_8)

        self.show_colorMenu_edit = QLineEdit(self.layoutWidget)
        self.show_colorMenu_edit.setObjectName(u"show_colorMenu_edit")
        self.show_colorMenu_edit.setFont(font)
        self.show_colorMenu_edit.setFocusPolicy(Qt.NoFocus)
        self.show_colorMenu_edit.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.show_colorMenu_edit)

        self.chose_colorMenu_edit = QComboBox(self.layoutWidget)
        self.chose_colorMenu_edit.addItem("")
        self.chose_colorMenu_edit.addItem("")
        self.chose_colorMenu_edit.addItem("")
        self.chose_colorMenu_edit.addItem("")
        self.chose_colorMenu_edit.setObjectName(u"chose_colorMenu_edit")
        font9 = QFont()
        font9.setPointSize(12)
        self.chose_colorMenu_edit.setFont(font9)

        self.horizontalLayout_14.addWidget(self.chose_colorMenu_edit)


        self.verticalLayout_8.addLayout(self.horizontalLayout_14)


        self.gridLayout_11.addWidget(self.frame, 0, 0, 1, 1)

        self.stackedWidget_page.addWidget(self.setting_page)

        self.verticalLayout_5.addWidget(self.stackedWidget_page)


        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)

        self.icon_only_Widget = QWidget(self.centralwidget)
        self.icon_only_Widget.setObjectName(u"icon_only_Widget")
        self.icon_only_Widget.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_Widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_Widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/icon/big_icon.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.quanlichiteu_Btn1 = QPushButton(self.icon_only_Widget)
        self.quanlichiteu_Btn1.setObjectName(u"quanlichiteu_Btn1")
        self.quanlichiteu_Btn1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icon/quanlychitieu_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/icon/quanlychitieu_blue.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.quanlichiteu_Btn1.setIcon(icon5)
        self.quanlichiteu_Btn1.setIconSize(QSize(25, 25))
        self.quanlichiteu_Btn1.setCheckable(True)
        self.quanlichiteu_Btn1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.quanlichiteu_Btn1)

        self.phantichchiteu_Btn1 = QPushButton(self.icon_only_Widget)
        self.phantichchiteu_Btn1.setObjectName(u"phantichchiteu_Btn1")
        self.phantichchiteu_Btn1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icon/growth_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/icon/growth_blue.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.phantichchiteu_Btn1.setIcon(icon6)
        self.phantichchiteu_Btn1.setIconSize(QSize(25, 25))
        self.phantichchiteu_Btn1.setCheckable(True)
        self.phantichchiteu_Btn1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.phantichchiteu_Btn1)

        self.goiytietkiem_Btn1 = QPushButton(self.icon_only_Widget)
        self.goiytietkiem_Btn1.setObjectName(u"goiytietkiem_Btn1")
        self.goiytietkiem_Btn1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icon/idea_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/icon/idea_blue.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.goiytietkiem_Btn1.setIcon(icon7)
        self.goiytietkiem_Btn1.setIconSize(QSize(25, 25))
        self.goiytietkiem_Btn1.setCheckable(True)
        self.goiytietkiem_Btn1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.goiytietkiem_Btn1)

        self.setting_Btn1 = QPushButton(self.icon_only_Widget)
        self.setting_Btn1.setObjectName(u"setting_Btn1")
        self.setting_Btn1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icon/settings_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(u":/icon/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.setting_Btn1.setIcon(icon8)
        self.setting_Btn1.setIconSize(QSize(25, 25))
        self.setting_Btn1.setCheckable(True)
        self.setting_Btn1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.setting_Btn1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 102, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.close_Btn1 = QPushButton(self.icon_only_Widget)
        self.close_Btn1.setObjectName(u"close_Btn1")
        self.close_Btn1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icon/close_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_Btn1.setIcon(icon9)
        self.close_Btn1.setIconSize(QSize(25, 25))
        self.close_Btn1.setCheckable(True)

        self.verticalLayout_3.addWidget(self.close_Btn1)


        self.gridLayout.addWidget(self.icon_only_Widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 24, -1)
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/icon/big_icon.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font8)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, 0, -1)
        self.quanlichiteu_Btn2 = QPushButton(self.icon_name_widget)
        self.quanlichiteu_Btn2.setObjectName(u"quanlichiteu_Btn2")
        self.quanlichiteu_Btn2.setFont(font7)
        self.quanlichiteu_Btn2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.quanlichiteu_Btn2.setIcon(icon5)
        self.quanlichiteu_Btn2.setIconSize(QSize(25, 25))
        self.quanlichiteu_Btn2.setCheckable(True)
        self.quanlichiteu_Btn2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.quanlichiteu_Btn2)

        self.phantichchiteu_Btn2 = QPushButton(self.icon_name_widget)
        self.phantichchiteu_Btn2.setObjectName(u"phantichchiteu_Btn2")
        self.phantichchiteu_Btn2.setFont(font7)
        self.phantichchiteu_Btn2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.phantichchiteu_Btn2.setIcon(icon6)
        self.phantichchiteu_Btn2.setIconSize(QSize(25, 25))
        self.phantichchiteu_Btn2.setCheckable(True)
        self.phantichchiteu_Btn2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.phantichchiteu_Btn2)

        self.goiytietkiem_Btn2 = QPushButton(self.icon_name_widget)
        self.goiytietkiem_Btn2.setObjectName(u"goiytietkiem_Btn2")
        self.goiytietkiem_Btn2.setFont(font7)
        self.goiytietkiem_Btn2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.goiytietkiem_Btn2.setIcon(icon7)
        self.goiytietkiem_Btn2.setIconSize(QSize(25, 25))
        self.goiytietkiem_Btn2.setCheckable(True)
        self.goiytietkiem_Btn2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.goiytietkiem_Btn2)

        self.setting_Btn2 = QPushButton(self.icon_name_widget)
        self.setting_Btn2.setObjectName(u"setting_Btn2")
        self.setting_Btn2.setFont(font7)
        self.setting_Btn2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setting_Btn2.setIcon(icon8)
        self.setting_Btn2.setIconSize(QSize(25, 25))
        self.setting_Btn2.setCheckable(True)
        self.setting_Btn2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.setting_Btn2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 102, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.close_Btn2 = QPushButton(self.icon_name_widget)
        self.close_Btn2.setObjectName(u"close_Btn2")
        self.close_Btn2.setFont(font7)
        self.close_Btn2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.close_Btn2.setIcon(icon9)
        self.close_Btn2.setIconSize(QSize(25, 25))
        self.close_Btn2.setCheckable(True)

        self.verticalLayout_4.addWidget(self.close_Btn2)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu_Btn.toggled.connect(self.icon_only_Widget.setHidden)
        self.menu_Btn.toggled.connect(self.icon_name_widget.setVisible)
        self.setting_Btn1.toggled.connect(self.setting_Btn2.setChecked)
        self.goiytietkiem_Btn1.toggled.connect(self.goiytietkiem_Btn2.setChecked)
        self.phantichchiteu_Btn1.toggled.connect(self.phantichchiteu_Btn2.setChecked)
        self.quanlichiteu_Btn1.toggled.connect(self.quanlichiteu_Btn2.setChecked)
        self.setting_Btn2.toggled.connect(self.setting_Btn1.setChecked)
        self.goiytietkiem_Btn2.toggled.connect(self.goiytietkiem_Btn1.setChecked)
        self.quanlichiteu_Btn2.toggled.connect(self.quanlichiteu_Btn1.setChecked)
        self.phantichchiteu_Btn2.toggled.connect(self.phantichchiteu_Btn1.setChecked)
        self.close_Btn1.clicked.connect(MainWindow.close)
        self.close_Btn2.clicked.connect(MainWindow.close)

        self.stackedWidget_page.setCurrentIndex(0)
        self.stackedWidget_phantichchitieu.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_Btn.setText("")
        self.notepad_btn.setText("")
        self.i_button.setText("")
        self.Quanlichitieu_lable.setText(QCoreApplication.translate("MainWindow", u"Qu\u1ea3n l\u00fd chi ti\u00eau", None))
        self.them_Btn.setText(QCoreApplication.translate("MainWindow", u"Thu", None))
        self.themchi_Btn.setText(QCoreApplication.translate("MainWindow", u"Chi", None))
        self.Chondanhmuc_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Ch\u1ecdn danh m\u1ee5c", None))
        self.Chondanhmuc_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0110i ch\u1ee3", None))
        self.Chondanhmuc_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Y t\u1ebf", None))
        self.Chondanhmuc_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Gi\u1ea3i tr\u00ed", None))
        self.Chondanhmuc_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"H\u00f3a \u0111\u01a1n", None))
        self.Chondanhmuc_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"\u0110\u1ea7u t\u01b0, ti\u1ebft ki\u1ec7m", None))
        self.Chondanhmuc_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"\u0102n u\u1ed1ng", None))
        self.Chondanhmuc_comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Kh\u00e1c", None))
        self.Chondanhmuc_comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"T\u1ea5t c\u1ea3", None))

        self.timchitieu_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"T\u00ecm chi ti\u00eau...", None))
        ___qtablewidgetitem = self.chitieu_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"STT", None));
        ___qtablewidgetitem1 = self.chitieu_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian", None));
        ___qtablewidgetitem2 = self.chitieu_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Danh m\u1ee5c", None));
        ___qtablewidgetitem3 = self.chitieu_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"T\u00ean chi ti\u00eau", None));
        ___qtablewidgetitem4 = self.chitieu_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 ti\u1ec1n", None));
        ___qtablewidgetitem5 = self.chitieu_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Ghi ch\u00fa", None));
        self.phantichchitieu_title.setText(QCoreApplication.translate("MainWindow", u"Ph\u00e2n t\u00edch chi ti\u00eau", None))
        self.circle_chart.setText("")
        self.chart.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"T\u1eeb :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ebfn :", None))
        self.submit_date.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"G\u1ee3i \u00fd ti\u1ebft ki\u1ec7m cho:", None))
        self.chonthangnam_GYTK.setItemText(0, QCoreApplication.translate("MainWindow", u"Th\u00e1ng/N\u0103m", None))

        self.chonthangnam_GYTK.setCurrentText(QCoreApplication.translate("MainWindow", u"Th\u00e1ng/N\u0103m", None))
        self.goiy_btn.setText(QCoreApplication.translate("MainWindow", u"G\u1ee3i \u00fd", None))
        self.goiy_show.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Thay \u0111\u1ed5i m\u00e0u s\u1eafc", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.chose_colorMenu_edit.setItemText(0, QCoreApplication.translate("MainWindow", u"Default", None))
        self.chose_colorMenu_edit.setItemText(1, QCoreApplication.translate("MainWindow", u"Black", None))
        self.chose_colorMenu_edit.setItemText(2, QCoreApplication.translate("MainWindow", u"Purple", None))
        self.chose_colorMenu_edit.setItemText(3, QCoreApplication.translate("MainWindow", u"Green", None))

        self.label.setText("")
        self.quanlichiteu_Btn1.setText("")
        self.phantichchiteu_Btn1.setText("")
        self.goiytietkiem_Btn1.setText("")
        self.setting_Btn1.setText("")
        self.close_Btn1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Qu\u1ea3n l\u00fd", None))
        self.quanlichiteu_Btn2.setText(QCoreApplication.translate("MainWindow", u"Qu\u1ea3n l\u00fd chi ti\u00eau", None))
        self.phantichchiteu_Btn2.setText(QCoreApplication.translate("MainWindow", u"Ph\u00e2n t\u00edch chi ti\u00eau", None))
        self.goiytietkiem_Btn2.setText(QCoreApplication.translate("MainWindow", u"G\u1ee3i \u00fd ti\u1ebft ki\u1ec7m", None))
        self.setting_Btn2.setText(QCoreApplication.translate("MainWindow", u"C\u00e0i \u0111\u1eb7t", None))
        self.close_Btn2.setText(QCoreApplication.translate("MainWindow", u"\u0110\u00f3ng", None))
    # retranslateUi

