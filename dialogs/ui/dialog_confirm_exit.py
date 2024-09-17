# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_confirm_exit.ui'
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
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog_ConfirmExit(object):
    def setupUi(self, Dialog_ConfirmExit):
        if not Dialog_ConfirmExit.objectName():
            Dialog_ConfirmExit.setObjectName(u"Dialog_ConfirmExit")
        Dialog_ConfirmExit.resize(400, 113)
        Dialog_ConfirmExit.setStyleSheet(u"QDialog {\n"
"background-color: #FFF\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog_ConfirmExit)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog_ConfirmExit)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"color: #000\n"
"}")
        self.label.setMargin(10)

        self.verticalLayout.addWidget(self.label)

        self.buttonBox = QDialogButtonBox(Dialog_ConfirmExit)
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
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Yes)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog_ConfirmExit)
        self.buttonBox.accepted.connect(Dialog_ConfirmExit.accept)
        self.buttonBox.rejected.connect(Dialog_ConfirmExit.reject)

        QMetaObject.connectSlotsByName(Dialog_ConfirmExit)
    # setupUi

    def retranslateUi(self, Dialog_ConfirmExit):
        Dialog_ConfirmExit.setWindowTitle(QCoreApplication.translate("Dialog_ConfirmExit", u"Exit Application", None))
        self.label.setText(QCoreApplication.translate("Dialog_ConfirmExit", u"Are you sure you want to exit the application?", None))
    # retranslateUi

