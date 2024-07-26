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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QSpacerItem,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from chartwidget import ChartWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 700)
        self.actionHistogrammdatei_laden = QAction(MainWindow)
        self.actionHistogrammdatei_laden.setObjectName(u"actionHistogrammdatei_laden")
        self.actionProgramm_beenden = QAction(MainWindow)
        self.actionProgramm_beenden.setObjectName(u"actionProgramm_beenden")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, 10, -1)
        self.tableWidget_2 = QTableWidget(self.centralwidget)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.verticalLayout_5.addWidget(self.tableWidget_2)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.chartWidget = ChartWidget(self.centralwidget)
        self.chartWidget.setObjectName(u"chartWidget")
        self.chartWidget.setMinimumSize(QSize(600, 400))
        self.chartWidget.setMaximumSize(QSize(600, 400))

        self.horizontalLayout.addWidget(self.chartWidget)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 0, 0, -1)
        self.measurementInformationTable = QTableWidget(self.centralwidget)
        self.measurementInformationTable.setObjectName(u"measurementInformationTable")
        self.measurementInformationTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.measurementInformationTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.verticalLayout_4.addWidget(self.measurementInformationTable)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 21))
        self.menuDatei = QMenu(self.menubar)
        self.menuDatei.setObjectName(u"menuDatei")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuDatei.menuAction())
        self.menuDatei.addAction(self.actionHistogrammdatei_laden)
        self.menuDatei.addSeparator()
        self.menuDatei.addAction(self.actionProgramm_beenden)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionHistogrammdatei_laden.setText(QCoreApplication.translate("MainWindow", u"Histogrammdatei laden", None))
        self.actionProgramm_beenden.setText(QCoreApplication.translate("MainWindow", u"Programm beenden", None))
#if QT_CONFIG(shortcut)
        self.actionProgramm_beenden.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.menuDatei.setTitle(QCoreApplication.translate("MainWindow", u"Datei", None))
    # retranslateUi

