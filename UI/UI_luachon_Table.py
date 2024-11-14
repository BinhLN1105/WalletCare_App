# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_luachonEditTable.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_luachon_table(object):
    def setupUi(self, luachon_table):
        if not luachon_table.objectName():
            luachon_table.setObjectName(u"luachon_table")
        luachon_table.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(luachon_table.sizePolicy().hasHeightForWidth())
        luachon_table.setSizePolicy(sizePolicy)
        luachon_table.setMinimumSize(QSize(400, 300))
        luachon_table.setMaximumSize(QSize(400, 300))
        self.frame = QFrame(luachon_table)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 421, 361))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.edit_table_btn = QPushButton(self.frame)
        self.edit_table_btn.setObjectName(u"edit_table_btn")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.edit_table_btn.setFont(font)
        self.edit_table_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color:white;\n"
"	font-weight:bold;\n"
"\n"
"}")
        self.edit_table_btn.setCheckable(True)
        self.edit_table_btn.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.edit_table_btn)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.delete_table_btn = QPushButton(self.frame)
        self.delete_table_btn.setObjectName(u"delete_table_btn")
        self.delete_table_btn.setFont(font)
        self.delete_table_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #E33220;\n"
"	color:white;\n"
"	font-weight:bold;\n"
"}")
        self.delete_table_btn.setCheckable(True)
        self.delete_table_btn.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.delete_table_btn)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)


        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.close_WidgetEdit = QPushButton(self.frame)
        self.close_WidgetEdit.setObjectName(u"close_WidgetEdit")
        self.close_WidgetEdit.setFont(font)
        self.close_WidgetEdit.setStyleSheet(u"QPushButton{\n"
"	background-color: #585858;\n"
"	color:white;\n"
"	font-weight:bold;\n"
"}")
        self.close_WidgetEdit.setCheckable(True)
        self.close_WidgetEdit.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.close_WidgetEdit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.retranslateUi(luachon_table)

        QMetaObject.connectSlotsByName(luachon_table)
    # setupUi

    def retranslateUi(self, luachon_table):
        luachon_table.setWindowTitle(QCoreApplication.translate("luachon_table", u"Dialog", None))
        self.edit_table_btn.setText(QCoreApplication.translate("luachon_table", u"Ch\u1ec9nh s\u1eeda", None))
        self.delete_table_btn.setText(QCoreApplication.translate("luachon_table", u"X\u00f3a", None))
        self.close_WidgetEdit.setText(QCoreApplication.translate("luachon_table", u"\u0110\u00f3ng", None))
        self.label.setText(QCoreApplication.translate("luachon_table", u"B\u1ea1n mu\u1ed1n l\u00e0m g\u00ec ?", None))
    # retranslateUi

