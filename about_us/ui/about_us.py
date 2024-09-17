# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_us.ui2'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)
import assets_rc

class Ui_AboutUsWindow(object):
    def setupUi(self, AboutUsWindow):
        if not AboutUsWindow.objectName():
            AboutUsWindow.setObjectName(u"AboutUsWindow")
        AboutUsWindow.resize(1277, 645)
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        AboutUsWindow.setWindowIcon(icon)
        AboutUsWindow.setStyleSheet(u"background-color: #fff;\n"
"color: #000;\n"
"")
        self.gridLayout_2 = QGridLayout(AboutUsWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_4 = QFrame(AboutUsWindow)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(20)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"margin: 20 0 0 80px;\n"
"")

        self.verticalLayout_2.addWidget(self.label_5)

        self.scrollArea = QScrollArea(self.frame_4)
        self.scrollArea.setObjectName(u"scrollArea")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(10)
        self.scrollArea.setFont(font1)
        self.scrollArea.setStyleSheet(u"margin: 20 0 0 0px;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1199, 508))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_AboutUsContent = QLabel(self.scrollAreaWidgetContents)
        self.label_AboutUsContent.setObjectName(u"label_AboutUsContent")
        self.label_AboutUsContent.setFont(font1)
        self.label_AboutUsContent.setStyleSheet(u"margin: 0 80 0 100px;\n"
"")
        self.label_AboutUsContent.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_AboutUsContent.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_AboutUsContent)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.gridLayout_2.addWidget(self.frame_4, 2, 0, 1, 2)


        self.retranslateUi(AboutUsWindow)

        QMetaObject.connectSlotsByName(AboutUsWindow)
    # setupUi

    def retranslateUi(self, AboutUsWindow):
        AboutUsWindow.setWindowTitle(QCoreApplication.translate("AboutUsWindow", u"EmoSense", None))
        self.label_5.setText(QCoreApplication.translate("AboutUsWindow", u"About Us", None))
        self.label_AboutUsContent.setText("")
    # retranslateUi

