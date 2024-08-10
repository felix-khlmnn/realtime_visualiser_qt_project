# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

from chartwidget import ChartWidget
from inputline import InputLine
from measurementinformationtable import MeasurementInformationTable
from outputlist import OutputList

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 700)
        self.actionHistogrammdatei_laden = QAction(MainWindow)
        self.actionHistogrammdatei_laden.setObjectName(u"actionHistogrammdatei_laden")
        self.actionProgramm_beenden = QAction(MainWindow)
        self.actionProgramm_beenden.setObjectName(u"actionProgramm_beenden")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.actionProgramm_beenden.setIcon(icon)
        self.actionHilfe_anzeigen = QAction(MainWindow)
        self.actionHilfe_anzeigen.setObjectName(u"actionHilfe_anzeigen")
        self.action_ueber_Realtime_Latency_Visualiser = QAction(MainWindow)
        self.action_ueber_Realtime_Latency_Visualiser.setObjectName(u"action_ueber_Realtime_Latency_Visualiser")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogInformation))
        self.action_ueber_Realtime_Latency_Visualiser.setIcon(icon1)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.chartWidget = ChartWidget(self.centralwidget)
        self.chartWidget.setObjectName(u"chartWidget")
        self.chartWidget.setMinimumSize(QSize(600, 400))
        self.chartWidget.setMaximumSize(QSize(2000, 2000))
        self.chartWidget.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.chartWidget)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 0, 0, -1)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.measurementInformationTable = MeasurementInformationTable(self.centralwidget)
        self.measurementInformationTable.setObjectName(u"measurementInformationTable")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measurementInformationTable.sizePolicy().hasHeightForWidth())
        self.measurementInformationTable.setSizePolicy(sizePolicy)
        self.measurementInformationTable.setMinimumSize(QSize(250, 150))
        self.measurementInformationTable.setMaximumSize(QSize(300, 150))
        self.measurementInformationTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.measurementInformationTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.measurementInformationTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.measurementInformationTable.setAlternatingRowColors(False)
        self.measurementInformationTable.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.measurementInformationTable.setShowGrid(True)
        self.measurementInformationTable.setCornerButtonEnabled(False)

        self.verticalLayout_4.addWidget(self.measurementInformationTable)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.multiTabWidget = QTabWidget(self.centralwidget)
        self.multiTabWidget.setObjectName(u"multiTabWidget")
        self.multiTabWidget.setMaximumSize(QSize(16777215, 300))
        self.multiTabWidget.setTabPosition(QTabWidget.TabPosition.South)
        self.multiTabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.multiTabWidget.setElideMode(Qt.TextElideMode.ElideNone)
        self.multiTabWidget.setDocumentMode(False)
        self.multiTabWidget.setTabsClosable(False)
        self.multiTabWidget.setMovable(False)
        self.multiTabWidget.setTabBarAutoHide(False)
        self.abfrage = QWidget()
        self.abfrage.setObjectName(u"abfrage")
        self.horizontalLayout_2 = QHBoxLayout(self.abfrage)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.outputList = OutputList(self.abfrage)
        self.outputList.setObjectName(u"outputList")
        font = QFont()
        font.setFamilies([u"Consolas"])
        self.outputList.setFont(font)

        self.verticalLayout_5.addWidget(self.outputList)

        self.inputLine = InputLine(self.abfrage)
        self.inputLine.setObjectName(u"inputLine")
        self.inputLine.setFont(font)
        self.inputLine.setClearButtonEnabled(False)

        self.verticalLayout_5.addWidget(self.inputLine)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.multiTabWidget.addTab(self.abfrage, "")

        self.verticalLayout.addWidget(self.multiTabWidget)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 25))
        self.menuDatei = QMenu(self.menubar)
        self.menuDatei.setObjectName(u"menuDatei")
        self.menuHilfe = QMenu(self.menubar)
        self.menuHilfe.setObjectName(u"menuHilfe")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menuHilfe.menuAction())
        self.menuDatei.addAction(self.actionHistogrammdatei_laden)
        self.menuDatei.addSeparator()
        self.menuDatei.addAction(self.actionProgramm_beenden)
        self.menuHilfe.addAction(self.actionHilfe_anzeigen)
        self.menuHilfe.addAction(self.action_ueber_Realtime_Latency_Visualiser)

        self.retranslateUi(MainWindow)

        self.multiTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Realtime Latency Visualiser", None))
        self.actionHistogrammdatei_laden.setText(QCoreApplication.translate("MainWindow", u"Histogrammdatei laden", None))
#if QT_CONFIG(shortcut)
        self.actionHistogrammdatei_laden.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.actionProgramm_beenden.setText(QCoreApplication.translate("MainWindow", u"Programm beenden", None))
#if QT_CONFIG(shortcut)
        self.actionProgramm_beenden.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionHilfe_anzeigen.setText(QCoreApplication.translate("MainWindow", u"Hilfe anzeigen", None))
#if QT_CONFIG(tooltip)
        self.actionHilfe_anzeigen.setToolTip(QCoreApplication.translate("MainWindow", u"Hilfe anzeigen", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionHilfe_anzeigen.setShortcut(QCoreApplication.translate("MainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.action_ueber_Realtime_Latency_Visualiser.setText(QCoreApplication.translate("MainWindow", u"\u00dcber Realtime Latency Visualiser", None))
        self.inputLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Befehl eingeben", None))
        self.multiTabWidget.setTabText(self.multiTabWidget.indexOf(self.abfrage), QCoreApplication.translate("MainWindow", u"Abfrage", None))
        self.menuDatei.setTitle(QCoreApplication.translate("MainWindow", u"Datei", None))
        self.menuHilfe.setTitle(QCoreApplication.translate("MainWindow", u"Hilfe", None))
    # retranslateUi

