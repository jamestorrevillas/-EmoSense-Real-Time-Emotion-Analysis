# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'users.ui'
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
    QLabel, QLayout, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import assets_rc

class Ui_UsersForm(object):
    def setupUi(self, UsersForm):
        if not UsersForm.objectName():
            UsersForm.setObjectName(u"UsersForm")
        UsersForm.resize(1100, 599)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UsersForm.sizePolicy().hasHeightForWidth())
        UsersForm.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        UsersForm.setWindowIcon(icon)
        UsersForm.setStyleSheet(u"background-color: #fff;\n"
"color: #000;")
        self.gridLayout_2 = QGridLayout(UsersForm)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 4, 0, 1, 3)

        self.frame = QFrame(UsersForm)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(10)
        self.label_7.setFont(font1)

        self.verticalLayout.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_SelectUsername = QLabel(self.frame)
        self.label_SelectUsername.setObjectName(u"label_SelectUsername")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.label_SelectUsername.setFont(font2)

        self.verticalLayout.addWidget(self.label_SelectUsername, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 3)

        self.frame_3 = QFrame(UsersForm)
        self.frame_3.setObjectName(u"frame_3")
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        self.frame_3.setFont(font3)
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_CreateAnAccount = QPushButton(self.frame_3)
        self.pushButton_CreateAnAccount.setObjectName(u"pushButton_CreateAnAccount")
        self.pushButton_CreateAnAccount.setMinimumSize(QSize(338, 42))
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(12)
        self.pushButton_CreateAnAccount.setFont(font4)
        self.pushButton_CreateAnAccount.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton_CreateAnAccount, 2, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame_3, 3, 0, 1, 3)

        self.frame_4 = QFrame(UsersForm)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea = QScrollArea(self.frame_4)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(600, 300))
        self.scrollArea.setFont(font3)
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"background-color: #fafafa;\n"
"border: 1px solid #fafafa;\n"
"border-radius: 10px;\n"
"padding: 10 0 10 0px;\n"
"}")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 578, 278))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.usersContainer = QWidget(self.scrollAreaWidgetContents)
        self.usersContainer.setObjectName(u"usersContainer")
        sizePolicy.setHeightForWidth(self.usersContainer.sizePolicy().hasHeightForWidth())
        self.usersContainer.setSizePolicy(sizePolicy)
        self.usersContainer.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.usersContainer.setStyleSheet(u"")
        self.usersLayout = QVBoxLayout(self.usersContainer)
        self.usersLayout.setObjectName(u"usersLayout")
        self.usersLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.usersLayout.setContentsMargins(-1, -1, -1, 9)
        self.frame_User = QFrame(self.usersContainer)
        self.frame_User.setObjectName(u"frame_User")
        self.frame_User.setStyleSheet(u"background-color: #fff;\n"
"border: 1px solid #f5f5f5;\n"
"border-radius: 10px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;")
        self.frame_User.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_User.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_User)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_Username = QLabel(self.frame_User)
        self.label_Username.setObjectName(u"label_Username")
        self.label_Username.setStyleSheet(u"border: none;")

        self.horizontalLayout_2.addWidget(self.label_Username)

        self.label_LastActiveDate = QLabel(self.frame_User)
        self.label_LastActiveDate.setObjectName(u"label_LastActiveDate")
        self.label_LastActiveDate.setStyleSheet(u"border: none;")

        self.horizontalLayout_2.addWidget(self.label_LastActiveDate, 0, Qt.AlignmentFlag.AlignRight)


        self.usersLayout.addWidget(self.frame_User)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.usersLayout.addItem(self.verticalSpacer)


        self.verticalLayout_3.addWidget(self.usersContainer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_4, 1, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 2, 1, 1, 1)

        QWidget.setTabOrder(self.scrollArea, self.pushButton_CreateAnAccount)

        self.retranslateUi(UsersForm)

        QMetaObject.connectSlotsByName(UsersForm)
    # setupUi

    def retranslateUi(self, UsersForm):
        UsersForm.setWindowTitle(QCoreApplication.translate("UsersForm", u"EmoSense", None))
        self.label.setText(QCoreApplication.translate("UsersForm", u"Welcome to EmoSense", None))
        self.label_7.setText(QCoreApplication.translate("UsersForm", u"Login locally to monitor your emotions and well-being", None))
        self.label_SelectUsername.setText(QCoreApplication.translate("UsersForm", u"Select your username below to log in", None))
        self.pushButton_CreateAnAccount.setText(QCoreApplication.translate("UsersForm", u"Create an Account", None))
        self.label_11.setText(QCoreApplication.translate("UsersForm", u"New here? Sign up!", None))
        self.label_Username.setText(QCoreApplication.translate("UsersForm", u"johndoe123", None))
        self.label_LastActiveDate.setText(QCoreApplication.translate("UsersForm", u"Last active on 06/29/2024 at 10:30am", None))
    # retranslateUi

