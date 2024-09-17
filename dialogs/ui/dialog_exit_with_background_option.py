# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_exit_with_background_option.ui'
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
    QLabel, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog_ExitWithBackgroundOption(object):
    def setupUi(self, Dialog_ExitWithBackgroundOption):
        if not Dialog_ExitWithBackgroundOption.objectName():
            Dialog_ExitWithBackgroundOption.setObjectName(u"Dialog_ExitWithBackgroundOption")
        Dialog_ExitWithBackgroundOption.resize(400, 154)
        Dialog_ExitWithBackgroundOption.setStyleSheet(u"QDialog {\n"
"background-color: #FFF\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog_ExitWithBackgroundOption)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog_ExitWithBackgroundOption)
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

        self.widget = QWidget(Dialog_ExitWithBackgroundOption)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget {\n"
"color: #000\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioButton_Minimize = QRadioButton(self.widget)
        self.radioButton_Minimize.setObjectName(u"radioButton_Minimize")
        self.radioButton_Minimize.setFont(font)
        self.radioButton_Minimize.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.radioButton_Minimize)

        self.radioButton_Exit = QRadioButton(self.widget)
        self.radioButton_Exit.setObjectName(u"radioButton_Exit")
        self.radioButton_Exit.setFont(font)

        self.verticalLayout_2.addWidget(self.radioButton_Exit)


        self.verticalLayout.addWidget(self.widget)

        self.buttonBox = QDialogButtonBox(Dialog_ExitWithBackgroundOption)
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
"}")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog_ExitWithBackgroundOption)
        self.buttonBox.accepted.connect(Dialog_ExitWithBackgroundOption.accept)
        self.buttonBox.rejected.connect(Dialog_ExitWithBackgroundOption.reject)

        QMetaObject.connectSlotsByName(Dialog_ExitWithBackgroundOption)
    # setupUi

    def retranslateUi(self, Dialog_ExitWithBackgroundOption):
        Dialog_ExitWithBackgroundOption.setWindowTitle(QCoreApplication.translate("Dialog_ExitWithBackgroundOption", u"Exit Application", None))
        self.label.setText(QCoreApplication.translate("Dialog_ExitWithBackgroundOption", u"How would you like to proceed?", None))
        self.radioButton_Minimize.setText(QCoreApplication.translate("Dialog_ExitWithBackgroundOption", u"Minimize - App will continue running in the background", None))
        self.radioButton_Exit.setText(QCoreApplication.translate("Dialog_ExitWithBackgroundOption", u"Exit - All processes will be stopped", None))
    # retranslateUi

