# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        if not LoginForm.objectName():
            LoginForm.setObjectName(u"LoginForm")
        LoginForm.resize(1100, 599)
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        LoginForm.setWindowIcon(icon)
        LoginForm.setStyleSheet(u"background-color: #fff;\n"
"color: #000;\n"
"")
        self.gridLayout_2 = QGridLayout(LoginForm)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 4, 0, 1, 3)

        self.frame_3 = QFrame(LoginForm)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(11)
        font.setBold(True)
        self.label_10.setFont(font)

        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 6, 0, 1, 2)

        self.pushButton_GoBack = QPushButton(self.frame_3)
        self.pushButton_GoBack.setObjectName(u"pushButton_GoBack")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
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

        self.gridLayout.addWidget(self.pushButton_GoBack, 8, 0, 1, 2)

        self.pushButton_Login = QPushButton(self.frame_3)
        self.pushButton_Login.setObjectName(u"pushButton_Login")
        self.pushButton_Login.setFont(font1)
        self.pushButton_Login.setAutoFillBackground(False)
        self.pushButton_Login.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton_Login, 7, 0, 1, 2)

        self.lineEdit_Password = QLineEdit(self.frame_3)
        self.lineEdit_Password.setObjectName(u"lineEdit_Password")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(10)
        self.lineEdit_Password.setFont(font2)
        self.lineEdit_Password.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid #808080;\n"
"border-radius: 5px;")
        self.lineEdit_Password.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.lineEdit_Password, 4, 0, 1, 2)

        self.label_WelcomeMessage = QLabel(self.frame_3)
        self.label_WelcomeMessage.setObjectName(u"label_WelcomeMessage")
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(14)
        self.label_WelcomeMessage.setFont(font3)

        self.gridLayout.addWidget(self.label_WelcomeMessage, 0, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 2)

        self.label_ErrorMessage = QLabel(self.frame_3)
        self.label_ErrorMessage.setObjectName(u"label_ErrorMessage")
        self.label_ErrorMessage.setFont(font2)
        self.label_ErrorMessage.setStyleSheet(u"color: #FF0000;")

        self.gridLayout.addWidget(self.label_ErrorMessage, 5, 0, 1, 2)


        self.gridLayout_2.addWidget(self.frame_3, 3, 1, 1, 1)

        self.frame = QFrame(LoginForm)
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

        QWidget.setTabOrder(self.lineEdit_Password, self.pushButton_Login)
        QWidget.setTabOrder(self.pushButton_Login, self.pushButton_GoBack)

        self.retranslateUi(LoginForm)

        QMetaObject.connectSlotsByName(LoginForm)
    # setupUi

    def retranslateUi(self, LoginForm):
        LoginForm.setWindowTitle(QCoreApplication.translate("LoginForm", u"EmoSense", None))
        self.label_10.setText(QCoreApplication.translate("LoginForm", u"Password", None))
        self.pushButton_GoBack.setText(QCoreApplication.translate("LoginForm", u"Go Back", None))
        self.pushButton_Login.setText(QCoreApplication.translate("LoginForm", u"Login", None))
        self.lineEdit_Password.setPlaceholderText(QCoreApplication.translate("LoginForm", u"Enter your password here", None))
        self.label_WelcomeMessage.setText(QCoreApplication.translate("LoginForm", u"Glad you're back @username!", None))
        self.label_ErrorMessage.setText(QCoreApplication.translate("LoginForm", u"<for error message>", None))
        self.label.setText(QCoreApplication.translate("LoginForm", u"Welcome to EmoSense", None))
        self.label_7.setText(QCoreApplication.translate("LoginForm", u"Login locally to monitor your emotions and well-being", None))
    # retranslateUi

