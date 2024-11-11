# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'themchitieu.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Nhapchitieu_Dialog(object):
    def setupUi(self, Nhapchitieu_Dialog):
        if not Nhapchitieu_Dialog.objectName():
            Nhapchitieu_Dialog.setObjectName(u"Nhapchitieu_Dialog")
        Nhapchitieu_Dialog.resize(548, 414)
        Nhapchitieu_Dialog.setStyleSheet(u"QDialog{\n"
"	background-color:white;\n"
"}\n"
"\n"
"QlineEdit{\n"
"	border:1px solid gray;\n"
"	border-radius:6px;\n"
"	padding-left:15px;\n"
"	height:35px;\n"
"}\n"
"\n"
"QDateEdit{\n"
"	border:1px solid gray;\n"
"	border-radius:6px;\n"
"	padding-left:15px;\n"
"	height:31px;\n"
"}\n"
"QComboBox{\n"
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
        self.gridLayout = QGridLayout(Nhapchitieu_Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.ThemChitieumoi_label = QLabel(Nhapchitieu_Dialog)
        self.ThemChitieumoi_label.setObjectName(u"ThemChitieumoi_label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.ThemChitieumoi_label.setFont(font)

        self.horizontalLayout_5.addWidget(self.ThemChitieumoi_label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.line = QFrame(Nhapchitieu_Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Chon_label = QLabel(Nhapchitieu_Dialog)
        self.Chon_label.setObjectName(u"Chon_label")
        font1 = QFont()
        font1.setPointSize(12)
        self.Chon_label.setFont(font1)

        self.verticalLayout_2.addWidget(self.Chon_label)

        self.Luachondanhmuc_combobox = QComboBox(Nhapchitieu_Dialog)
        self.Luachondanhmuc_combobox.addItem("")
        self.Luachondanhmuc_combobox.addItem("")
        self.Luachondanhmuc_combobox.addItem("")
        self.Luachondanhmuc_combobox.addItem("")
        self.Luachondanhmuc_combobox.addItem("")
        self.Luachondanhmuc_combobox.addItem("")
        self.Luachondanhmuc_combobox.addItem("")
        self.Luachondanhmuc_combobox.setObjectName(u"Luachondanhmuc_combobox")
        font2 = QFont()
        font2.setBold(True)
        font2.setKerning(True)
        self.Luachondanhmuc_combobox.setFont(font2)

        self.verticalLayout_2.addWidget(self.Luachondanhmuc_combobox)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tenchitieu_label = QLabel(Nhapchitieu_Dialog)
        self.tenchitieu_label.setObjectName(u"tenchitieu_label")
        self.tenchitieu_label.setFont(font1)
        self.tenchitieu_label.setMargin(5)

        self.verticalLayout_4.addWidget(self.tenchitieu_label)

        self.nhaptenchitieu = QLineEdit(Nhapchitieu_Dialog)
        self.nhaptenchitieu.setObjectName(u"nhaptenchitieu")
        self.nhaptenchitieu.setMinimumSize(QSize(0, 35))
        self.nhaptenchitieu.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_4.addWidget(self.nhaptenchitieu)


        self.gridLayout.addLayout(self.verticalLayout_4, 1, 1, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.ngaychiteu_label = QLabel(Nhapchitieu_Dialog)
        self.ngaychiteu_label.setObjectName(u"ngaychiteu_label")
        self.ngaychiteu_label.setFont(font1)

        self.verticalLayout_6.addWidget(self.ngaychiteu_label)

        self.chonngay_editdate = QDateEdit(Nhapchitieu_Dialog)
        self.chonngay_editdate.setObjectName(u"chonngay_editdate")
        font3 = QFont()
        font3.setPointSize(8)
        self.chonngay_editdate.setFont(font3)
        self.chonngay_editdate.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(0, 0, 0)))
        self.chonngay_editdate.setCalendarPopup(True)

        self.verticalLayout_6.addWidget(self.chonngay_editdate)


        self.gridLayout.addLayout(self.verticalLayout_6, 2, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.sotien_lable = QLabel(Nhapchitieu_Dialog)
        self.sotien_lable.setObjectName(u"sotien_lable")
        self.sotien_lable.setFont(font1)
        self.sotien_lable.setMargin(5)

        self.verticalLayout_5.addWidget(self.sotien_lable)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.nhapsotien_linedit = QLineEdit(Nhapchitieu_Dialog)
        self.nhapsotien_linedit.setObjectName(u"nhapsotien_linedit")
        self.nhapsotien_linedit.setMinimumSize(QSize(0, 35))
        self.nhapsotien_linedit.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_3.addWidget(self.nhapsotien_linedit)

        self.label = QLabel(Nhapchitieu_Dialog)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setPointSize(10)
        self.label.setFont(font4)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Tenchitieu_label = QLabel(Nhapchitieu_Dialog)
        self.Tenchitieu_label.setObjectName(u"Tenchitieu_label")
        self.Tenchitieu_label.setFont(font1)

        self.verticalLayout.addWidget(self.Tenchitieu_label)

        self.ghichu_text = QTextEdit(Nhapchitieu_Dialog)
        self.ghichu_text.setObjectName(u"ghichu_text")
        self.ghichu_text.setFont(font4)

        self.verticalLayout.addWidget(self.ghichu_text)


        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(278, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.them_Btn = QPushButton(Nhapchitieu_Dialog)
        self.them_Btn.setObjectName(u"them_Btn")
        self.them_Btn.setMinimumSize(QSize(0, 41))
        self.them_Btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color:white;\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	font-weight:bold;\n"
"	font-size:15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.them_Btn)

        self.exit_btn = QPushButton(Nhapchitieu_Dialog)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setMinimumSize(QSize(0, 41))
        self.exit_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #585858;\n"
"	color:white;\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	font-weight:bold;\n"
"	font-size:15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.exit_btn)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 2)


        self.retranslateUi(Nhapchitieu_Dialog)

        QMetaObject.connectSlotsByName(Nhapchitieu_Dialog)
    # setupUi

    def retranslateUi(self, Nhapchitieu_Dialog):
        Nhapchitieu_Dialog.setWindowTitle(QCoreApplication.translate("Nhapchitieu_Dialog", u"Dialog", None))
        self.ThemChitieumoi_label.setText(QCoreApplication.translate("Nhapchitieu_Dialog", u"Th\u00eam chi ti\u00eau m\u1edbi", None))
        self.Chon_label.setText(QCoreApplication.translate("Nhapchitieu_Dialog", u"Danh m\u1ee5c", None))
        self.Luachondanhmuc_combobox.setItemText(0, QCoreApplication.translate("Nhapchitieu_Dialog", u"\u0110i ch\u1ee3", None))
        self.Luachondanhmuc_combobox.setItemText(1, QCoreApplication.translate("Nhapchitieu_Dialog", u"Y t\u1ebf", None))
        self.Luachondanhmuc_combobox.setItemText(2, QCoreApplication.translate("Nhapchitieu_Dialog", u"Gi\u1ea3i tr\u00ed", None))
        self.Luachondanhmuc_combobox.setItemText(3, QCoreApplication.translate("Nhapchitieu_Dialog", u"H\u00f3a \u0111\u01a1n", None))
        self.Luachondanhmuc_combobox.setItemText(4, QCoreApplication.translate("Nhapchitieu_Dialog", u"\u0110\u1ea7u t\u01b0, ti\u1ebft ki\u1ec7m", None))
        self.Luachondanhmuc_combobox.setItemText(5, QCoreApplication.translate("Nhapchitieu_Dialog", u"Kh\u00e1c", None))
        self.Luachondanhmuc_combobox.setItemText(6, QCoreApplication.translate("Nhapchitieu_Dialog", u"\u0102n u\u1ed1ng", None))

        self.tenchitieu_label.setText(QCoreApplication.translate("Nhapchitieu_Dialog", u"T\u00ean chi ti\u00eau", None))
        self.ngaychiteu_label.setText(QCoreApplication.translate("Nhapchitieu_Dialog", u"Ng\u00e0y chi ti\u00eau", None))
        self.sotien_lable.setText(QCoreApplication.translate("Nhapchitieu_Dialog", u"S\u1ed1 ti\u1ec1n", None))
        self.label.setText(QCoreApplication.translate("Nhapchitieu_Dialog", u"VN\u0110", None))
        self.Tenchitieu_label.setText(QCoreApplication.translate("Nhapchitieu_Dialog", u"Ghi ch\u00fa", None))
        self.them_Btn.setText(QCoreApplication.translate("Nhapchitieu_Dialog", u"Th\u00eam", None))
        self.exit_btn.setText(QCoreApplication.translate("Nhapchitieu_Dialog", u"Tr\u1edf l\u1ea1i", None))
    # retranslateUi

