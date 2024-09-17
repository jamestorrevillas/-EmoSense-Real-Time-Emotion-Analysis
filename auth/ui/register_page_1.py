# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register_page_1.ui2'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import assets_rc

class Ui_RegisterFormWindow1(object):
    def setupUi(self, RegisterFormWindow1):
        if not RegisterFormWindow1.objectName():
            RegisterFormWindow1.setObjectName(u"RegisterFormWindow1")
        RegisterFormWindow1.resize(1100, 599)
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        RegisterFormWindow1.setWindowIcon(icon)
        RegisterFormWindow1.setStyleSheet(u"background-color: #fff;\n"
"color: #000;\n"
"")
        self.gridLayout_2 = QGridLayout(RegisterFormWindow1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(RegisterFormWindow1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(10)
        self.label_7.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 3, 0, 1, 1)

        self.frame_3 = QFrame(RegisterFormWindow1)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_DateOfBirth = QLabel(self.frame_3)
        self.label_DateOfBirth.setObjectName(u"label_DateOfBirth")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.label_DateOfBirth.setFont(font2)
        self.label_DateOfBirth.setStyleSheet(u"margin-top: 10px;")

        self.gridLayout.addWidget(self.label_DateOfBirth, 8, 0, 1, 1)

        self.pushButton_GoBack = QPushButton(self.frame_3)
        self.pushButton_GoBack.setObjectName(u"pushButton_GoBack")
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(12)
        self.pushButton_GoBack.setFont(font3)
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

        self.label_ErrorMessageForGender = QLabel(self.frame_3)
        self.label_ErrorMessageForGender.setObjectName(u"label_ErrorMessageForGender")
        self.label_ErrorMessageForGender.setFont(font1)
        self.label_ErrorMessageForGender.setStyleSheet(u"color: #FF0000;")

        self.gridLayout.addWidget(self.label_ErrorMessageForGender, 7, 0, 1, 1)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)

        self.comboBox_Gender = QComboBox(self.frame_3)
        self.comboBox_Gender.addItem("")
        self.comboBox_Gender.addItem("")
        self.comboBox_Gender.addItem("")
        self.comboBox_Gender.setObjectName(u"comboBox_Gender")
        self.comboBox_Gender.setFont(font3)
        self.comboBox_Gender.setStyleSheet(u"background-color: #E5E4E2;\n"
"border-radius: 5px;\n"
"padding-left: 20px;\n"
"\n"
"\n"
"")

        self.gridLayout.addWidget(self.comboBox_Gender, 6, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 12, 0, 1, 2)

        self.lineEdit_PreferredName = QLineEdit(self.frame_3)
        self.lineEdit_PreferredName.setObjectName(u"lineEdit_PreferredName")
        self.lineEdit_PreferredName.setMinimumSize(QSize(332, 0))
        self.lineEdit_PreferredName.setFont(font1)
        self.lineEdit_PreferredName.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid #808080;\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.lineEdit_PreferredName, 3, 0, 1, 1)

        self.pushButton_Next = QPushButton(self.frame_3)
        self.pushButton_Next.setObjectName(u"pushButton_Next")
        self.pushButton_Next.setFont(font3)
        self.pushButton_Next.setAutoFillBackground(False)
        self.pushButton_Next.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton_Next, 13, 0, 1, 2)

        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"margin-top: 10px;")

        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 2)

        self.label_ErrorMessageForDateOfBirth = QLabel(self.frame_3)
        self.label_ErrorMessageForDateOfBirth.setObjectName(u"label_ErrorMessageForDateOfBirth")
        self.label_ErrorMessageForDateOfBirth.setFont(font1)
        self.label_ErrorMessageForDateOfBirth.setStyleSheet(u"color: #FF0000;")

        self.gridLayout.addWidget(self.label_ErrorMessageForDateOfBirth, 10, 0, 1, 1)

        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(14)
        self.label_9.setFont(font4)

        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.dateEdit_DateOfBirth = QDateEdit(self.frame_3)
        self.dateEdit_DateOfBirth.setObjectName(u"dateEdit_DateOfBirth")
        self.dateEdit_DateOfBirth.setFont(font3)
        self.dateEdit_DateOfBirth.setStyleSheet(u"background-color: #E5E4E2;\n"
"border-radius: 5px;\n"
"padding-left: 10px;")

        self.gridLayout.addWidget(self.dateEdit_DateOfBirth, 9, 0, 1, 1)

        self.label_ErrorMessageForPreferredName = QLabel(self.frame_3)
        self.label_ErrorMessageForPreferredName.setObjectName(u"label_ErrorMessageForPreferredName")
        self.label_ErrorMessageForPreferredName.setFont(font1)
        self.label_ErrorMessageForPreferredName.setStyleSheet(u"color: #FF0000;")

        self.gridLayout.addWidget(self.label_ErrorMessageForPreferredName, 4, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 3, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 3, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 4, 0, 1, 3)

        QWidget.setTabOrder(self.lineEdit_PreferredName, self.comboBox_Gender)
        QWidget.setTabOrder(self.comboBox_Gender, self.dateEdit_DateOfBirth)
        QWidget.setTabOrder(self.dateEdit_DateOfBirth, self.pushButton_Next)
        QWidget.setTabOrder(self.pushButton_Next, self.pushButton_GoBack)

        self.retranslateUi(RegisterFormWindow1)

        QMetaObject.connectSlotsByName(RegisterFormWindow1)
    # setupUi

    def retranslateUi(self, RegisterFormWindow1):
        RegisterFormWindow1.setWindowTitle(QCoreApplication.translate("RegisterFormWindow1", u"EmoSense", None))
        self.label.setText(QCoreApplication.translate("RegisterFormWindow1", u"Welcome to EmoSense", None))
        self.label_7.setText(QCoreApplication.translate("RegisterFormWindow1", u"Create an account locally to monitor your emotions and well-being", None))
        self.label_DateOfBirth.setText(QCoreApplication.translate("RegisterFormWindow1", u"Date of Birth (dd/mm/yyyy)", None))
        self.pushButton_GoBack.setText(QCoreApplication.translate("RegisterFormWindow1", u"Go Back", None))
        self.label_ErrorMessageForGender.setText(QCoreApplication.translate("RegisterFormWindow1", u"<for error message>", None))
        self.label_8.setText(QCoreApplication.translate("RegisterFormWindow1", u"What should we call you?", None))
        self.comboBox_Gender.setItemText(0, QCoreApplication.translate("RegisterFormWindow1", u"Select your gender", None))
        self.comboBox_Gender.setItemText(1, QCoreApplication.translate("RegisterFormWindow1", u"Male", None))
        self.comboBox_Gender.setItemText(2, QCoreApplication.translate("RegisterFormWindow1", u"Female", None))

        self.lineEdit_PreferredName.setPlaceholderText(QCoreApplication.translate("RegisterFormWindow1", u"Enter your preferred name here", None))
        self.pushButton_Next.setText(QCoreApplication.translate("RegisterFormWindow1", u"Next", None))
        self.label_10.setText(QCoreApplication.translate("RegisterFormWindow1", u"Gender", None))
        self.label_ErrorMessageForDateOfBirth.setText(QCoreApplication.translate("RegisterFormWindow1", u"<for error message>", None))
        self.label_9.setText(QCoreApplication.translate("RegisterFormWindow1", u"We're happy to have you!", None))
        self.label_ErrorMessageForPreferredName.setText(QCoreApplication.translate("RegisterFormWindow1", u"<for error message>", None))
    # retranslateUi

