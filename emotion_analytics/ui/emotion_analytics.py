# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'emotion_analytics.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCalendarWidget, QCheckBox,
    QComboBox, QGridLayout, QLabel, QScrollArea,
    QSizePolicy, QSpacerItem, QTextBrowser, QVBoxLayout,
    QWidget)
import assets_rc

class Ui_EmotionAnalyticsWindow(object):
    def setupUi(self, EmotionAnalyticsWindow):
        if not EmotionAnalyticsWindow.objectName():
            EmotionAnalyticsWindow.setObjectName(u"EmotionAnalyticsWindow")
        EmotionAnalyticsWindow.resize(1295, 645)
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        EmotionAnalyticsWindow.setWindowIcon(icon)
        EmotionAnalyticsWindow.setStyleSheet(u"background-color: #fff;\n"
"color: #000;\n"
"")
        self.gridLayout_2 = QGridLayout(EmotionAnalyticsWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea = QScrollArea(EmotionAnalyticsWindow)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1458, 2766))
        self.scrollAreaWidgetContents.setStyleSheet(u"m")
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(50, 9, 50, -1)
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(13)
        font.setBold(True)
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2)

        self.comboBox_TimeFrame = QComboBox(self.widget_4)
        self.comboBox_TimeFrame.addItem("")
        self.comboBox_TimeFrame.addItem("")
        self.comboBox_TimeFrame.addItem("")
        self.comboBox_TimeFrame.setObjectName(u"comboBox_TimeFrame")
        self.comboBox_TimeFrame.setMinimumSize(QSize(300, 0))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        self.comboBox_TimeFrame.setFont(font1)
        self.comboBox_TimeFrame.setStyleSheet(u"background-color: #E5E4E2;\n"
"border-radius: 5px;\n"
"")

        self.verticalLayout_2.addWidget(self.comboBox_TimeFrame)

        self.calendarWidget_Date = QCalendarWidget(self.widget_4)
        self.calendarWidget_Date.setObjectName(u"calendarWidget_Date")
        self.calendarWidget_Date.setMinimumSize(QSize(0, 250))
        self.calendarWidget_Date.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_2.addWidget(self.calendarWidget_Date)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"margin-left: 5px;")

        self.verticalLayout_2.addWidget(self.label_4)

        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_4 = QGridLayout(self.widget_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.checkBox_Surprise = QCheckBox(self.widget_5)
        self.checkBox_Surprise.setObjectName(u"checkBox_Surprise")
        self.checkBox_Surprise.setFont(font1)
        self.checkBox_Surprise.setChecked(True)

        self.gridLayout_4.addWidget(self.checkBox_Surprise, 0, 3, 1, 1)

        self.checkBox_Disgust = QCheckBox(self.widget_5)
        self.checkBox_Disgust.setObjectName(u"checkBox_Disgust")
        self.checkBox_Disgust.setFont(font1)
        self.checkBox_Disgust.setChecked(True)

        self.gridLayout_4.addWidget(self.checkBox_Disgust, 1, 3, 1, 1)

        self.checkBox_Anger = QCheckBox(self.widget_5)
        self.checkBox_Anger.setObjectName(u"checkBox_Anger")
        self.checkBox_Anger.setFont(font1)
        self.checkBox_Anger.setChecked(True)

        self.gridLayout_4.addWidget(self.checkBox_Anger, 1, 0, 1, 1)

        self.checkBox_Happiness = QCheckBox(self.widget_5)
        self.checkBox_Happiness.setObjectName(u"checkBox_Happiness")
        self.checkBox_Happiness.setFont(font1)
        self.checkBox_Happiness.setChecked(True)

        self.gridLayout_4.addWidget(self.checkBox_Happiness, 0, 1, 1, 1)

        self.checkBox_Contempt = QCheckBox(self.widget_5)
        self.checkBox_Contempt.setObjectName(u"checkBox_Contempt")
        self.checkBox_Contempt.setFont(font1)
        self.checkBox_Contempt.setChecked(True)

        self.gridLayout_4.addWidget(self.checkBox_Contempt, 0, 2, 1, 1)

        self.checkBox_Sadness = QCheckBox(self.widget_5)
        self.checkBox_Sadness.setObjectName(u"checkBox_Sadness")
        self.checkBox_Sadness.setFont(font1)
        self.checkBox_Sadness.setChecked(True)

        self.gridLayout_4.addWidget(self.checkBox_Sadness, 1, 1, 1, 1)

        self.checkBox_Neutral = QCheckBox(self.widget_5)
        self.checkBox_Neutral.setObjectName(u"checkBox_Neutral")
        self.checkBox_Neutral.setFont(font1)
        self.checkBox_Neutral.setChecked(True)

        self.gridLayout_4.addWidget(self.checkBox_Neutral, 0, 0, 1, 1)

        self.checkBox_Fear = QCheckBox(self.widget_5)
        self.checkBox_Fear.setObjectName(u"checkBox_Fear")
        self.checkBox_Fear.setFont(font1)
        self.checkBox_Fear.setChecked(True)

        self.gridLayout_4.addWidget(self.checkBox_Fear, 1, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_5)


        self.gridLayout.addWidget(self.widget_4, 4, 0, 1, 2)

        self.label_EmotionAnalyticsDescription = QLabel(self.widget)
        self.label_EmotionAnalyticsDescription.setObjectName(u"label_EmotionAnalyticsDescription")
        self.label_EmotionAnalyticsDescription.setMinimumSize(QSize(0, 60))
        self.label_EmotionAnalyticsDescription.setFont(font1)
        self.label_EmotionAnalyticsDescription.setScaledContents(False)
        self.label_EmotionAnalyticsDescription.setWordWrap(True)

        self.gridLayout.addWidget(self.label_EmotionAnalyticsDescription, 1, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 3)

        self.label_EmotionAnalyticsTitle = QLabel(self.widget)
        self.label_EmotionAnalyticsTitle.setObjectName(u"label_EmotionAnalyticsTitle")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.label_EmotionAnalyticsTitle.setFont(font2)

        self.gridLayout.addWidget(self.label_EmotionAnalyticsTitle, 0, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 5, 0, 1, 3)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)

        self.textBrowser_SummaryAndRecommendations = QTextBrowser(self.widget)
        self.textBrowser_SummaryAndRecommendations.setObjectName(u"textBrowser_SummaryAndRecommendations")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_SummaryAndRecommendations.sizePolicy().hasHeightForWidth())
        self.textBrowser_SummaryAndRecommendations.setSizePolicy(sizePolicy)
        self.textBrowser_SummaryAndRecommendations.setMinimumSize(QSize(0, 2000))
        self.textBrowser_SummaryAndRecommendations.setFont(font1)
        self.textBrowser_SummaryAndRecommendations.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textBrowser_SummaryAndRecommendations.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.textBrowser_SummaryAndRecommendations.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)

        self.gridLayout.addWidget(self.textBrowser_SummaryAndRecommendations, 7, 0, 1, 3)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 21))
        self.label.setFont(font)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.comboBox_SelectChart = QComboBox(self.widget_2)
        self.comboBox_SelectChart.addItem("")
        self.comboBox_SelectChart.setObjectName(u"comboBox_SelectChart")
        self.comboBox_SelectChart.setMinimumSize(QSize(250, 0))
        self.comboBox_SelectChart.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_SelectChart.setFont(font1)
        self.comboBox_SelectChart.setStyleSheet(u"background-color: #E5E4E2;\n"
"border-radius: 5px;\n"
"")

        self.gridLayout_3.addWidget(self.comboBox_SelectChart, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.widget_ChartPlaceholder = QWidget(self.widget_2)
        self.widget_ChartPlaceholder.setObjectName(u"widget_ChartPlaceholder")
        self.widget_ChartPlaceholder.setMinimumSize(QSize(900, 427))
        self.widget_ChartPlaceholder.setMaximumSize(QSize(16777215, 427))
        self.widget_ChartPlaceholder.setStyleSheet(u"border: 1px solid #000;\n"
"border-radius: 10px;")
        self.verticalLayout_3 = QVBoxLayout(self.widget_ChartPlaceholder)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.gridLayout_3.addWidget(self.widget_ChartPlaceholder, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 4, 2, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.retranslateUi(EmotionAnalyticsWindow)

        QMetaObject.connectSlotsByName(EmotionAnalyticsWindow)
    # setupUi

    def retranslateUi(self, EmotionAnalyticsWindow):
        EmotionAnalyticsWindow.setWindowTitle(QCoreApplication.translate("EmotionAnalyticsWindow", u"EmoSense", None))
        self.label_2.setText(QCoreApplication.translate("EmotionAnalyticsWindow", u"Time Frame", None))
        self.comboBox_TimeFrame.setItemText(0, QCoreApplication.translate("EmotionAnalyticsWindow", u"Daily", None))
        self.comboBox_TimeFrame.setItemText(1, QCoreApplication.translate("EmotionAnalyticsWindow", u"Weekly", None))
        self.comboBox_TimeFrame.setItemText(2, QCoreApplication.translate("EmotionAnalyticsWindow", u"Monthly", None))

        self.label_3.setText(QCoreApplication.translate("EmotionAnalyticsWindow", u"Filter Emotions", None))
        self.label_4.setText(QCoreApplication.translate("EmotionAnalyticsWindow", u"Check/Uncheck to show specific emotions", None))
        self.checkBox_Surprise.setText(QCoreApplication.translate("EmotionAnalyticsWindow", u"Surprise", None))
        self.checkBox_Disgust.setText(QCoreApplication.translate("EmotionAnalyticsWindow", u"Disgust", None))
        self.checkBox_Anger.setText(QCoreApplication.translate("EmotionAnalyticsWindow", u"Anger", None))
        self.checkBox_Happiness.setText(QCoreApplication.translate("EmotionAnalyticsWindow", u"Happiness", None))
        self.checkBox_Contempt.setText(QCoreApplication.translate("EmotionAnalyticsWindow", u"Contempt", None))
        self.checkBox_Sadness.setText(QCoreApplication.translate("EmotionAnalyticsWindow", u"Sadness", None))
        self.checkBox_Neutral.setText(QCoreApplication.translate("EmotionAnalyticsWindow", u"Neutral", None))
        self.checkBox_Fear.setText(QCoreApplication.translate("EmotionAnalyticsWindow", u"Fear", None))
        self.label_EmotionAnalyticsDescription.setText(QCoreApplication.translate("EmotionAnalyticsWindow", u"Emotion analytics involves using technology to analyze human emotions through facial expressions, voice tones, and other cues. It helps improve customer experiences, diagnose mental health, and enhance human-computer interactions.", None))
        self.label_EmotionAnalyticsTitle.setText(QCoreApplication.translate("EmotionAnalyticsWindow", u"Emotion Analytics", None))
        self.label_6.setText(QCoreApplication.translate("EmotionAnalyticsWindow", u"Summary and Recommendations", None))
        self.label.setText(QCoreApplication.translate("EmotionAnalyticsWindow", u"Emotion Distribution Over Time", None))
        self.comboBox_SelectChart.setItemText(0, QCoreApplication.translate("EmotionAnalyticsWindow", u"Line Chart", None))

    # retranslateUi

