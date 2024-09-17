# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)
import assets_rc

class Ui_SettingsFormWindow(object):
    def setupUi(self, SettingsFormWindow):
        if not SettingsFormWindow.objectName():
            SettingsFormWindow.setObjectName(u"SettingsFormWindow")
        SettingsFormWindow.resize(1100, 599)
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        SettingsFormWindow.setWindowIcon(icon)
        SettingsFormWindow.setStyleSheet(u"background-color: #fff;\n"
"color: #000;\n"
"")
        self.gridLayout_2 = QGridLayout(SettingsFormWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 3, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 5, 0, 1, 3)

        self.frame = QFrame(SettingsFormWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 3)

        self.widget = QWidget(SettingsFormWindow)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_Save = QPushButton(self.widget)
        self.pushButton_Save.setObjectName(u"pushButton_Save")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        self.pushButton_Save.setFont(font1)
        self.pushButton_Save.setAutoFillBackground(False)
        self.pushButton_Save.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.pushButton_Save)

        self.pushButton_Cancel = QPushButton(self.widget)
        self.pushButton_Cancel.setObjectName(u"pushButton_Cancel")
        self.pushButton_Cancel.setFont(font1)
        self.pushButton_Cancel.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.pushButton_Cancel)


        self.gridLayout_2.addWidget(self.widget, 4, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.frame_3 = QFrame(SettingsFormWindow)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(500, 0))
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_ErrorMessageForUsername = QLabel(self.frame_3)
        self.label_ErrorMessageForUsername.setObjectName(u"label_ErrorMessageForUsername")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(10)
        self.label_ErrorMessageForUsername.setFont(font2)
        self.label_ErrorMessageForUsername.setStyleSheet(u"color: #FF0000;")

        self.gridLayout.addWidget(self.label_ErrorMessageForUsername, 7, 0, 1, 1)

        self.lineEdit_Username = QLineEdit(self.frame_3)
        self.lineEdit_Username.setObjectName(u"lineEdit_Username")
        self.lineEdit_Username.setFont(font2)
        self.lineEdit_Username.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid #808080;\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.lineEdit_Username, 6, 0, 1, 2)

        self.label_ErrorMessageForCurrentPassword = QLabel(self.frame_3)
        self.label_ErrorMessageForCurrentPassword.setObjectName(u"label_ErrorMessageForCurrentPassword")
        self.label_ErrorMessageForCurrentPassword.setFont(font2)
        self.label_ErrorMessageForCurrentPassword.setStyleSheet(u"color: #FF0000;")

        self.gridLayout.addWidget(self.label_ErrorMessageForCurrentPassword, 10, 0, 1, 1)

        self.label_Profile = QLabel(self.frame_3)
        self.label_Profile.setObjectName(u"label_Profile")
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.label_Profile.setFont(font3)
        self.label_Profile.setStyleSheet(u"QLabel {\n"
"    border-bottom: 2px solid black;\n"
"    padding-bottom: 5px;\n"
"}")

        self.gridLayout.addWidget(self.label_Profile, 0, 0, 1, 2, Qt.AlignmentFlag.AlignLeft)

        self.lineEdit_ConfirmNewPassword = QLineEdit(self.frame_3)
        self.lineEdit_ConfirmNewPassword.setObjectName(u"lineEdit_ConfirmNewPassword")
        self.lineEdit_ConfirmNewPassword.setFont(font2)
        self.lineEdit_ConfirmNewPassword.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid #808080;\n"
"border-radius: 5px;")
        self.lineEdit_ConfirmNewPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.lineEdit_ConfirmNewPassword, 16, 0, 1, 2)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"margin-top: 10px;")

        self.gridLayout.addWidget(self.label_2, 8, 0, 1, 1)

        self.lineEdit_CurrentPassword = QLineEdit(self.frame_3)
        self.lineEdit_CurrentPassword.setObjectName(u"lineEdit_CurrentPassword")
        self.lineEdit_CurrentPassword.setFont(font2)
        self.lineEdit_CurrentPassword.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid #808080;\n"
"border-radius: 5px;")
        self.lineEdit_CurrentPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.lineEdit_CurrentPassword, 9, 0, 1, 2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 18, 0, 1, 2)

        self.lineEdit_NewPassword = QLineEdit(self.frame_3)
        self.lineEdit_NewPassword.setObjectName(u"lineEdit_NewPassword")
        self.lineEdit_NewPassword.setFont(font2)
        self.lineEdit_NewPassword.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid #808080;\n"
"border-radius: 5px;")
        self.lineEdit_NewPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.lineEdit_NewPassword, 13, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 2)

        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font4)
        self.label_12.setStyleSheet(u"margin-top: 10px;")

        self.gridLayout.addWidget(self.label_12, 15, 0, 1, 1)

        self.label_ErrorMessageForNewPassword = QLabel(self.frame_3)
        self.label_ErrorMessageForNewPassword.setObjectName(u"label_ErrorMessageForNewPassword")
        self.label_ErrorMessageForNewPassword.setFont(font2)
        self.label_ErrorMessageForNewPassword.setStyleSheet(u"color: #FF0000;")

        self.gridLayout.addWidget(self.label_ErrorMessageForNewPassword, 14, 0, 1, 1)

        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"margin-top: 10px;")

        self.gridLayout.addWidget(self.label_10, 11, 0, 1, 1)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u"margin-top: 10px;")

        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)

        self.label_ErrorMessageForConfirmNewPassword = QLabel(self.frame_3)
        self.label_ErrorMessageForConfirmNewPassword.setObjectName(u"label_ErrorMessageForConfirmNewPassword")
        self.label_ErrorMessageForConfirmNewPassword.setFont(font2)
        self.label_ErrorMessageForConfirmNewPassword.setStyleSheet(u"color: #FF0000;")

        self.gridLayout.addWidget(self.label_ErrorMessageForConfirmNewPassword, 17, 0, 1, 1)

        self.label_SuccessUpdateMessage = QLabel(self.frame_3)
        self.label_SuccessUpdateMessage.setObjectName(u"label_SuccessUpdateMessage")
        self.label_SuccessUpdateMessage.setFont(font2)

        self.gridLayout.addWidget(self.label_SuccessUpdateMessage, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 3, 1, 1, 1)

        QWidget.setTabOrder(self.lineEdit_Username, self.lineEdit_CurrentPassword)
        QWidget.setTabOrder(self.lineEdit_CurrentPassword, self.lineEdit_NewPassword)
        QWidget.setTabOrder(self.lineEdit_NewPassword, self.lineEdit_ConfirmNewPassword)
        QWidget.setTabOrder(self.lineEdit_ConfirmNewPassword, self.pushButton_Save)
        QWidget.setTabOrder(self.pushButton_Save, self.pushButton_Cancel)

        self.retranslateUi(SettingsFormWindow)

        QMetaObject.connectSlotsByName(SettingsFormWindow)
    # setupUi

    def retranslateUi(self, SettingsFormWindow):
        SettingsFormWindow.setWindowTitle(QCoreApplication.translate("SettingsFormWindow", u"EmoSense", None))
        self.label.setText(QCoreApplication.translate("SettingsFormWindow", u"Settings", None))
        self.pushButton_Save.setText(QCoreApplication.translate("SettingsFormWindow", u"Save", None))
        self.pushButton_Cancel.setText(QCoreApplication.translate("SettingsFormWindow", u"Cancel", None))
        self.label_ErrorMessageForUsername.setText(QCoreApplication.translate("SettingsFormWindow", u"<for error message>", None))
        self.lineEdit_Username.setPlaceholderText(QCoreApplication.translate("SettingsFormWindow", u"Update your username here", None))
        self.label_ErrorMessageForCurrentPassword.setText(QCoreApplication.translate("SettingsFormWindow", u"<for error message>", None))
        self.label_Profile.setText(QCoreApplication.translate("SettingsFormWindow", u"Profile", None))
        self.lineEdit_ConfirmNewPassword.setPlaceholderText(QCoreApplication.translate("SettingsFormWindow", u"Re-enter your new password here", None))
        self.label_2.setText(QCoreApplication.translate("SettingsFormWindow", u"Current Password", None))
        self.lineEdit_CurrentPassword.setPlaceholderText(QCoreApplication.translate("SettingsFormWindow", u"Enter your current password here", None))
        self.lineEdit_NewPassword.setPlaceholderText(QCoreApplication.translate("SettingsFormWindow", u"Enter your new password here", None))
        self.label_12.setText(QCoreApplication.translate("SettingsFormWindow", u"Confirm New Password", None))
        self.label_ErrorMessageForNewPassword.setText(QCoreApplication.translate("SettingsFormWindow", u"<for error message>", None))
        self.label_10.setText(QCoreApplication.translate("SettingsFormWindow", u"New Password", None))
        self.label_8.setText(QCoreApplication.translate("SettingsFormWindow", u"Username", None))
        self.label_ErrorMessageForConfirmNewPassword.setText(QCoreApplication.translate("SettingsFormWindow", u"<for error message>", None))
        self.label_SuccessUpdateMessage.setText(QCoreApplication.translate("SettingsFormWindow", u"<for successful update message>", None))
    # retranslateUi

