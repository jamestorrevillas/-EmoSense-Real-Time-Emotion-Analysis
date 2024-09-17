# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui2'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import assets_rc

class Ui_HomeWindow(object):
    def setupUi(self, HomeWindow):
        if not HomeWindow.objectName():
            HomeWindow.setObjectName(u"HomeWindow")
        HomeWindow.resize(1277, 645)
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        HomeWindow.setWindowIcon(icon)
        HomeWindow.setStyleSheet(u"background-color: #fff;\n"
"color: #000;\n"
"")
        self.gridLayout_2 = QGridLayout(HomeWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_3 = QFrame(HomeWindow)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setMargin(10)

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 7, 0, 1, 2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 4, 0, 1, 2)

        self.pushButton_ActivateNow = QPushButton(self.frame_3)
        self.pushButton_ActivateNow.setObjectName(u"pushButton_ActivateNow")
        self.pushButton_ActivateNow.setMinimumSize(QSize(338, 42))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        self.pushButton_ActivateNow.setFont(font1)
        self.pushButton_ActivateNow.setAutoFillBackground(False)
        self.pushButton_ActivateNow.setStyleSheet(u"QPushButton {\n"
"    background-color: #011BA1;\n"
"    color: #fff;\n"
"    padding: 10px;\n"
"    border: 1px solid #000;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #00008B;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #000070; \n"
"    color: #fff;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_ActivateNow, 6, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 0, 1, 2)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.label.setFont(font2)

        self.gridLayout.addWidget(self.label, 2, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setPixmap(QPixmap(u":/icons/images/icons/logo.png"))

        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7.setWordWrap(True)

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout_2.addWidget(self.frame_3, 3, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 4, 0, 1, 5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 3, 4, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 3, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 0, 1, 5)

        self.frame_4 = QFrame(HomeWindow)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(800, 600))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea = QScrollArea(self.frame_4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea { \n"
"background-color: #fafafa;\n"
"border: 1px solid #fafafa;\n"
"border-radius: 10px;\n"
"padding-top: 20px;\n"
"padding-bottom: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 738, 464))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.label_HomeContent = QLabel(self.widget)
        self.label_HomeContent.setObjectName(u"label_HomeContent")
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(10)
        self.label_HomeContent.setFont(font3)
        self.label_HomeContent.setStyleSheet(u"padding-top: 0px;\n"
"padding-bottom: 0px;")
        self.label_HomeContent.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.label_HomeContent.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_HomeContent)


        self.verticalLayout.addWidget(self.widget)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea, 1, 1, 1, 1)

        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setPixmap(QPixmap(u":/icons/images/icons/light-bulb.png"))

        self.horizontalLayout_2.addWidget(self.label_15)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(16)
        font4.setBold(True)
        self.label_12.setFont(font4)

        self.horizontalLayout_2.addWidget(self.label_12)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.gridLayout_3.addWidget(self.frame, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_4, 3, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 3, 0, 1, 1)


        self.retranslateUi(HomeWindow)

        QMetaObject.connectSlotsByName(HomeWindow)
    # setupUi

    def retranslateUi(self, HomeWindow):
        HomeWindow.setWindowTitle(QCoreApplication.translate("HomeWindow", u"EmoSense", None))
        self.label_5.setText(QCoreApplication.translate("HomeWindow", u"Turn on Real-time Emotion Recognition", None))
        self.pushButton_ActivateNow.setText(QCoreApplication.translate("HomeWindow", u"Activate Now", None))
        self.label.setText(QCoreApplication.translate("HomeWindow", u"Welcome to EmoSense", None))
        self.label_11.setText("")
        self.label_7.setText(QCoreApplication.translate("HomeWindow", u"An Intelligent Companion for Real-Time Emotion Insights and Well-Being", None))
        self.label_HomeContent.setText(QCoreApplication.translate("HomeWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi efficitur orci eu vestibulum tempus. Cras feugiat semper ex, ut feugiat justo. Aenean in consequat elit, nec accumsan nunc. Nunc ultrices ultricies magna, id malesuada neque interdum sed. Morbi ac pretium tellus. Sed maximus tortor magna, id vulputate lectus rutrum vitae. Morbi ac tortor vel elit vehicula iaculis. Integer dolor lorem, tempor ac venenatis at, commodo ut sapien. Nullam est ante,  feugiat non magna nec, gravida dignissim lorem. In neque metus, ultrices convallis est quis, sollicitudin accumsan lectus. Nulla facilisi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Phasellus id consequat dolor. Nunc porta nisl nisl, vel varius diam faucibus in.", None))
        self.label_15.setText("")
        self.label_12.setText(QCoreApplication.translate("HomeWindow", u"How Real-Time Emotion Recognition Works", None))
    # retranslateUi

