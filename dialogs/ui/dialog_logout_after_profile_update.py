# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_logout_after_profile_update.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Dialog_LogoutAfterProfileUpdate(object):
    def setupUi(self, Dialog_LogoutAfterProfileUpdate):
        if not Dialog_LogoutAfterProfileUpdate.objectName():
            Dialog_LogoutAfterProfileUpdate.setObjectName(u"Dialog_LogoutAfterProfileUpdate")
        Dialog_LogoutAfterProfileUpdate.resize(452, 223)
        Dialog_LogoutAfterProfileUpdate.setStyleSheet(u"QDialog {\n"
"background-color: #FFF\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog_LogoutAfterProfileUpdate)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label = QLabel(Dialog_LogoutAfterProfileUpdate)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"color: #000\n"
"}")
        self.label.setWordWrap(True)
        self.label.setMargin(10)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(Dialog_LogoutAfterProfileUpdate)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel {\n"
"color: #000\n"
"}")
        self.label_2.setWordWrap(True)
        self.label_2.setMargin(10)

        self.verticalLayout.addWidget(self.label_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(Dialog_LogoutAfterProfileUpdate)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setFont(font)
        self.buttonBox.setStyleSheet(u"\n"
"QDialogButtonBox QPushButton {\n"
"    background-color: #FFF;\n"
"    color: #000;\n"
"}\n"
"QDialogButtonBox QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}\n"
"QDialogButtonBox QPushButton:pressed {\n"
"    background-color: #21618c;\n"
"}\n"
"\n"
"")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox, 0, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi(Dialog_LogoutAfterProfileUpdate)
        self.buttonBox.accepted.connect(Dialog_LogoutAfterProfileUpdate.accept)
        self.buttonBox.rejected.connect(Dialog_LogoutAfterProfileUpdate.reject)

        QMetaObject.connectSlotsByName(Dialog_LogoutAfterProfileUpdate)
    # setupUi

    def retranslateUi(self, Dialog_LogoutAfterProfileUpdate):
        Dialog_LogoutAfterProfileUpdate.setWindowTitle(QCoreApplication.translate("Dialog_LogoutAfterProfileUpdate", u"Profile Update - Logout Required", None))
        self.label.setText(QCoreApplication.translate("Dialog_LogoutAfterProfileUpdate", u"Your profile has been successfully updated.", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_LogoutAfterProfileUpdate", u"For the app to work properly with these new changes, you will now be logged out. Please log in again to continue using the app with your updated profile.", None))
    # retranslateUi

