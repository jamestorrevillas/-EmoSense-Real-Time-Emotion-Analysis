# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'emotion_recognition.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QLabel, QSizePolicy, QSpacerItem,
    QWidget)
import assets_rc

class Ui_EmotionRecognitionWindow(object):
    def setupUi(self, EmotionRecognitionWindow):
        if not EmotionRecognitionWindow.objectName():
            EmotionRecognitionWindow.setObjectName(u"EmotionRecognitionWindow")
        EmotionRecognitionWindow.resize(1295, 645)
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        EmotionRecognitionWindow.setWindowIcon(icon)
        EmotionRecognitionWindow.setStyleSheet(u"background-color: #fff;\n"
"color: #000;\n"
"")
        self.gridLayout_2 = QGridLayout(EmotionRecognitionWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 0, 1, 5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 3, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 3, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 4, 0, 1, 5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 3, 2, 1, 1)

        self.frame_4 = QFrame(EmotionRecognitionWindow)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(800, 600))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_CameraFeed = QLabel(self.frame_4)
        self.label_CameraFeed.setObjectName(u"label_CameraFeed")
        self.label_CameraFeed.setStyleSheet(u"border: 0.5px solid #000;\n"
"")
        self.label_CameraFeed.setPixmap(QPixmap(u":/backgrounds/images/backgrounds/camera-feed.png"))

        self.gridLayout_3.addWidget(self.label_CameraFeed, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_4, 3, 3, 1, 1)

        self.frame_3 = QFrame(EmotionRecognitionWindow)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(13)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setMargin(0)

        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 3)

        self.comboBox_CameraSource = QComboBox(self.frame_3)
        self.comboBox_CameraSource.setObjectName(u"comboBox_CameraSource")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        self.comboBox_CameraSource.setFont(font1)
        self.comboBox_CameraSource.setStyleSheet(u"background-color: #E5E4E2;\n"
"border-radius: 5px;\n"
"")

        self.gridLayout.addWidget(self.comboBox_CameraSource, 9, 0, 1, 3)

        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setWordWrap(True)

        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 18, 0, 1, 3)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        font2 = QFont()
        font2.setFamilies([u"Roboto Medium"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.label_7.setWordWrap(False)
        self.label_7.setMargin(10)

        self.gridLayout.addWidget(self.label_7, 5, 2, 1, 1)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(20)
        font3.setBold(True)
        self.label.setFont(font3)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 3, Qt.AlignmentFlag.AlignLeft)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 0, 0, 1, 3)

        self.label_ErrorMessageForCameraSettings = QLabel(self.frame_3)
        self.label_ErrorMessageForCameraSettings.setObjectName(u"label_ErrorMessageForCameraSettings")
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(10)
        self.label_ErrorMessageForCameraSettings.setFont(font4)
        self.label_ErrorMessageForCameraSettings.setStyleSheet(u"color: #FF0000;")

        self.gridLayout.addWidget(self.label_ErrorMessageForCameraSettings, 10, 0, 1, 3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 7, 0, 1, 3)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_7, 3, 0, 1, 3)

        self.checkBox_ToggleActivate = QCheckBox(self.frame_3)
        self.checkBox_ToggleActivate.setObjectName(u"checkBox_ToggleActivate")
        self.checkBox_ToggleActivate.setFont(font1)

        self.gridLayout.addWidget(self.checkBox_ToggleActivate, 5, 1, 1, 1)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        font5 = QFont()
        font5.setFamilies([u"Roboto Medium"])
        font5.setPointSize(14)
        self.label_2.setFont(font5)
        self.label_2.setMargin(10)

        self.gridLayout.addWidget(self.label_2, 4, 2, 1, 1)

        self.checkBox_ToggleCameraOnOff = QCheckBox(self.frame_3)
        self.checkBox_ToggleCameraOnOff.setObjectName(u"checkBox_ToggleCameraOnOff")
        self.checkBox_ToggleCameraOnOff.setFont(font1)

        self.gridLayout.addWidget(self.checkBox_ToggleCameraOnOff, 4, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 3, 1, 1, 1)


        self.retranslateUi(EmotionRecognitionWindow)

        QMetaObject.connectSlotsByName(EmotionRecognitionWindow)
    # setupUi

    def retranslateUi(self, EmotionRecognitionWindow):
        EmotionRecognitionWindow.setWindowTitle(QCoreApplication.translate("EmotionRecognitionWindow", u"EmoSense", None))
        self.label_CameraFeed.setText("")
        self.label_5.setText(QCoreApplication.translate("EmotionRecognitionWindow", u"Change Settings/Options", None))
        self.label_11.setText(QCoreApplication.translate("EmotionRecognitionWindow", u"Our real-time emotion recognition feature analyzes your emotions on the fly for better self-awareness", None))
        self.label_7.setText(QCoreApplication.translate("EmotionRecognitionWindow", u"Turn live emotion tracking on/off", None))
        self.label.setText(QCoreApplication.translate("EmotionRecognitionWindow", u"Real-Time Emotion Recognition", None))
        self.label_ErrorMessageForCameraSettings.setText(QCoreApplication.translate("EmotionRecognitionWindow", u"TextLabel", None))
        self.checkBox_ToggleActivate.setText(QCoreApplication.translate("EmotionRecognitionWindow", u"CheckBox", None))
        self.label_2.setText(QCoreApplication.translate("EmotionRecognitionWindow", u"Turn camera on/off", None))
        self.checkBox_ToggleCameraOnOff.setText(QCoreApplication.translate("EmotionRecognitionWindow", u"CheckBox", None))
    # retranslateUi

