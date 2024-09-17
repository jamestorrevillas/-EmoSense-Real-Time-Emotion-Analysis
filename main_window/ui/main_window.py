# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1277, 714)
        MainWindow.setStyleSheet(u"background-color: #fff;\n"
"color: #000;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_NavBar = QFrame(self.centralwidget)
        self.frame_NavBar.setObjectName(u"frame_NavBar")
        self.frame_NavBar.setStyleSheet(u"border-bottom: 2px solid #f5f5f5;\n"
"")
        self.frame_NavBar.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_NavBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_NavBar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.label = QLabel(self.frame_NavBar)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet(u"border: none;")
        self.label.setPixmap(QPixmap(u":/icons/images/icons/logo.png"))
        self.label.setMargin(0)

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frame_NavBar)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Roboto Medium"])
        font1.setPointSize(18)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"QLabel {\n"
"    background-color: #FFF;\n"
"    color: #000;\n"
"    border: none;\n"
"}")
        self.label_2.setTextFormat(Qt.TextFormat.PlainText)
        self.label_2.setMargin(5)

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_Home = QLabel(self.frame_NavBar)
        self.label_Home.setObjectName(u"label_Home")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(12)
        self.label_Home.setFont(font2)
        self.label_Home.setStyleSheet(u"QLabel {\n"
"    background-color: #FFF;\n"
"    color: #000;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: #011BA1;\n"
"}")
        self.label_Home.setMargin(20)

        self.horizontalLayout.addWidget(self.label_Home)

        self.label_RealTimeEmotion = QLabel(self.frame_NavBar)
        self.label_RealTimeEmotion.setObjectName(u"label_RealTimeEmotion")
        self.label_RealTimeEmotion.setFont(font2)
        self.label_RealTimeEmotion.setStyleSheet(u"QLabel {\n"
"    background-color: #FFF;\n"
"    color: #000;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: #011BA1;\n"
"}")
        self.label_RealTimeEmotion.setMargin(20)

        self.horizontalLayout.addWidget(self.label_RealTimeEmotion)

        self.label_EmotionAnalytics = QLabel(self.frame_NavBar)
        self.label_EmotionAnalytics.setObjectName(u"label_EmotionAnalytics")
        self.label_EmotionAnalytics.setFont(font2)
        self.label_EmotionAnalytics.setStyleSheet(u"QLabel {\n"
"    background-color: #FFF;\n"
"    color: #000;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: #011BA1;\n"
"}")
        self.label_EmotionAnalytics.setMargin(20)

        self.horizontalLayout.addWidget(self.label_EmotionAnalytics)

        self.label_Settings = QLabel(self.frame_NavBar)
        self.label_Settings.setObjectName(u"label_Settings")
        self.label_Settings.setFont(font2)
        self.label_Settings.setStyleSheet(u"QLabel {\n"
"    background-color: #FFF;\n"
"    color: #000;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: #011BA1;\n"
"}")
        self.label_Settings.setMargin(20)

        self.horizontalLayout.addWidget(self.label_Settings)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_AboutUs = QLabel(self.frame_NavBar)
        self.label_AboutUs.setObjectName(u"label_AboutUs")
        self.label_AboutUs.setFont(font2)
        self.label_AboutUs.setStyleSheet(u"QLabel {\n"
"    background-color: #FFF;\n"
"    color: #000;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: #011BA1;\n"
"}")
        self.label_AboutUs.setMargin(20)

        self.horizontalLayout.addWidget(self.label_AboutUs)

        self.label_Login = QLabel(self.frame_NavBar)
        self.label_Login.setObjectName(u"label_Login")
        self.label_Login.setFont(font2)
        self.label_Login.setStyleSheet(u"QLabel {\n"
"    background-color: #FFF;\n"
"    color: #000;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: #011BA1;\n"
"}")
        self.label_Login.setMargin(20)

        self.horizontalLayout.addWidget(self.label_Login)

        self.label_Logout = QLabel(self.frame_NavBar)
        self.label_Logout.setObjectName(u"label_Logout")
        self.label_Logout.setFont(font2)
        self.label_Logout.setStyleSheet(u"QLabel {\n"
"    background-color: #FFF;\n"
"    color: #000;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: #011BA1;\n"
"}")
        self.label_Logout.setMargin(20)

        self.horizontalLayout.addWidget(self.label_Logout)

        self.label_Close = QLabel(self.frame_NavBar)
        self.label_Close.setObjectName(u"label_Close")
        self.label_Close.setFont(font2)
        self.label_Close.setStyleSheet(u"QLabel {\n"
"    background-color: #FFF;\n"
"    color: #000;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: #011BA1;\n"
"}")
        self.label_Close.setMargin(20)

        self.horizontalLayout.addWidget(self.label_Close)


        self.verticalLayout.addWidget(self.frame_NavBar)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget.addWidget(self.page_4)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"EmoSense", None))
        self.label_Home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_RealTimeEmotion.setText(QCoreApplication.translate("MainWindow", u"Real-time Emotion Recognition", None))
        self.label_EmotionAnalytics.setText(QCoreApplication.translate("MainWindow", u"Emotion Analytics", None))
        self.label_Settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_AboutUs.setText(QCoreApplication.translate("MainWindow", u"About Us", None))
        self.label_Login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_Logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.label_Close.setText(QCoreApplication.translate("MainWindow", u"Close", None))
    # retranslateUi

