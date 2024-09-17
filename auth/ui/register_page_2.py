# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register_page_2.ui2'
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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import assets_rc

class Ui_RegisterFormWindow2(object):
    def setupUi(self, RegisterFormWindow2):
        if not RegisterFormWindow2.objectName():
            RegisterFormWindow2.setObjectName(u"RegisterFormWindow2")
        RegisterFormWindow2.resize(1100, 599)
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        RegisterFormWindow2.setWindowIcon(icon)
        RegisterFormWindow2.setStyleSheet(u"background-color: #fff;\n"
"color: #000;\n"
"")
        self.gridLayout_2 = QGridLayout(RegisterFormWindow2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_3 = QFrame(RegisterFormWindow2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(14)
        self.label_9.setFont(font)

        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_CreateAccount = QPushButton(self.frame_3)
        self.pushButton_CreateAccount.setObjectName(u"pushButton_CreateAccount")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        self.pushButton_CreateAccount.setFont(font1)
        self.pushButton_CreateAccount.setAutoFillBackground(False)
        self.pushButton_CreateAccount.setStyleSheet(u"QPushButton {\n"
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
"}")

        self.gridLayout.addWidget(self.pushButton_CreateAccount, 13, 0, 1, 2)

        self.lineEdit_ConfirmPassword = QLineEdit(self.frame_3)
        self.lineEdit_ConfirmPassword.setObjectName(u"lineEdit_ConfirmPassword")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(10)
        self.lineEdit_ConfirmPassword.setFont(font2)
        self.lineEdit_ConfirmPassword.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid #808080;\n"
"border-radius: 5px;")
        self.lineEdit_ConfirmPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.lineEdit_ConfirmPassword, 10, 0, 1, 1)

        self.lineEdit_Username = QLineEdit(self.frame_3)
        self.lineEdit_Username.setObjectName(u"lineEdit_Username")
        self.lineEdit_Username.setFont(font2)
        self.lineEdit_Username.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid #808080;\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.lineEdit_Username, 3, 0, 1, 1)

        self.label_ErrorMessageForConfirmPassword = QLabel(self.frame_3)
        self.label_ErrorMessageForConfirmPassword.setObjectName(u"label_ErrorMessageForConfirmPassword")
        self.label_ErrorMessageForConfirmPassword.setFont(font2)
        self.label_ErrorMessageForConfirmPassword.setStyleSheet(u"color: #FF0000;")

        self.gridLayout.addWidget(self.label_ErrorMessageForConfirmPassword, 11, 0, 1, 1)

        self.label_ErrorMessageForPassword = QLabel(self.frame_3)
        self.label_ErrorMessageForPassword.setObjectName(u"label_ErrorMessageForPassword")
        self.label_ErrorMessageForPassword.setFont(font2)
        self.label_ErrorMessageForPassword.setStyleSheet(u"color: #FF0000;")

        self.gridLayout.addWidget(self.label_ErrorMessageForPassword, 8, 0, 1, 1)

        self.pushButton_GoBack = QPushButton(self.frame_3)
        self.pushButton_GoBack.setObjectName(u"pushButton_GoBack")
        self.pushButton_GoBack.setFont(font1)
        self.pushButton_GoBack.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFF;\n"
"    color: #000;\n"
"    padding: 10px;\n"
"    border: 1px solid #000;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #EEE; \n"
"    color: #000;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CCC;  \n"
"    color: #000;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_GoBack, 14, 0, 1, 2)

        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.label_12.setFont(font3)
        self.label_12.setStyleSheet(u"margin-top: 10px;")

        self.gridLayout.addWidget(self.label_12, 9, 0, 1, 1)

        self.lineEdit_Password = QLineEdit(self.frame_3)
        self.lineEdit_Password.setObjectName(u"lineEdit_Password")
        self.lineEdit_Password.setFont(font2)
        self.lineEdit_Password.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid #808080;\n"
"border-radius: 5px;")
        self.lineEdit_Password.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.lineEdit_Password, 7, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 2)

        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"margin-top: 10px;")

        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 1)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 12, 0, 1, 2)

        self.label_ErrorMessageForUsername = QLabel(self.frame_3)
        self.label_ErrorMessageForUsername.setObjectName(u"label_ErrorMessageForUsername")
        self.label_ErrorMessageForUsername.setFont(font2)
        self.label_ErrorMessageForUsername.setStyleSheet(u"color: #FF0000;")

        self.gridLayout.addWidget(self.label_ErrorMessageForUsername, 4, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 3, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 3, 2, 1, 1)

        self.frame = QFrame(RegisterFormWindow2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(20)
        font4.setBold(True)
        self.label.setFont(font4)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 4, 0, 1, 3)

        QWidget.setTabOrder(self.lineEdit_Username, self.lineEdit_Password)
        QWidget.setTabOrder(self.lineEdit_Password, self.lineEdit_ConfirmPassword)
        QWidget.setTabOrder(self.lineEdit_ConfirmPassword, self.pushButton_CreateAccount)
        QWidget.setTabOrder(self.pushButton_CreateAccount, self.pushButton_GoBack)

        self.retranslateUi(RegisterFormWindow2)

        QMetaObject.connectSlotsByName(RegisterFormWindow2)
    # setupUi

    def retranslateUi(self, RegisterFormWindow2):
        RegisterFormWindow2.setWindowTitle(QCoreApplication.translate("RegisterFormWindow2", u"EmoSense", None))
        self.label_9.setText(QCoreApplication.translate("RegisterFormWindow2", u"We're happy to have you!", None))
        self.pushButton_CreateAccount.setText(QCoreApplication.translate("RegisterFormWindow2", u"Create Account", None))
        self.lineEdit_ConfirmPassword.setPlaceholderText(QCoreApplication.translate("RegisterFormWindow2", u"Re-enter password here", None))
        self.lineEdit_Username.setPlaceholderText(QCoreApplication.translate("RegisterFormWindow2", u"Enter username here", None))
        self.label_ErrorMessageForConfirmPassword.setText(QCoreApplication.translate("RegisterFormWindow2", u"<for error message>", None))
        self.label_ErrorMessageForPassword.setText(QCoreApplication.translate("RegisterFormWindow2", u"<for error message>", None))
        self.pushButton_GoBack.setText(QCoreApplication.translate("RegisterFormWindow2", u"Go Back", None))
        self.label_12.setText(QCoreApplication.translate("RegisterFormWindow2", u"Confirm Password", None))
        self.lineEdit_Password.setPlaceholderText(QCoreApplication.translate("RegisterFormWindow2", u"Enter password here", None))
        self.label_10.setText(QCoreApplication.translate("RegisterFormWindow2", u"Password", None))
        self.label_8.setText(QCoreApplication.translate("RegisterFormWindow2", u"Username", None))
        self.label_ErrorMessageForUsername.setText(QCoreApplication.translate("RegisterFormWindow2", u"<for error message>", None))
        self.label.setText(QCoreApplication.translate("RegisterFormWindow2", u"Welcome to EmoSense", None))
        self.label_7.setText(QCoreApplication.translate("RegisterFormWindow2", u"Create an account locally to monitor your emotions and well-being", None))
    # retranslateUi

