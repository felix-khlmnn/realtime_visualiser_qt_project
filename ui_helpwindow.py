# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'helpwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QTextBrowser,
    QWidget)

class Ui_helpWindow(object):
    def setupUi(self, helpWindow):
        if not helpWindow.objectName():
            helpWindow.setObjectName(u"helpWindow")
        helpWindow.resize(600, 400)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpFaq))
        helpWindow.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(helpWindow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textBrowser = QTextBrowser(helpWindow)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout.addWidget(self.textBrowser)


        self.retranslateUi(helpWindow)

        QMetaObject.connectSlotsByName(helpWindow)
    # setupUi

    def retranslateUi(self, helpWindow):
        helpWindow.setWindowTitle(QCoreApplication.translate("helpWindow", u"Hilfe", None))
        self.textBrowser.setHtml(QCoreApplication.translate("helpWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700;\">Realtime Latency Visualiser</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Dieses Programm dient der Visualisierung von Messergebnissen des &quot;Cyclictest&quot;, einem Test, welcher der \u00dcberpr\u00fcfung der Echtzeitf\u00e4higkeit eines Linux-Systems dient.</"
                        "p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Programmaufbau</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In der oberen linken Ecke des Programmfensters wird, sobald eine Datei geladen wurde, das Histogramm dargestellt. Rechts daneben befindet sich die Messwertinformationstabelle, welche verschiedene statistische Werte des Datensatzes beinhaltet. Zuguterletzt befindet sich unten eine Kommandozeile, mit der Datenwerte aus dem Datensatz abgefragt werden k\u00f6nnen.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p "
                        "style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Wie visualisiere ich eine Datei?</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Die Visualisierung wird gestartet, sobald \u00fcber die Schaltfl\u00e4che &quot;Histogramm laden&quot; eine entsprechend formatierte Textdatei ausgew\u00e4hlt worden ist. Um die korrekte Funktion des Programms zu gew\u00e4hrleisten, empfehle ich, die unmodifizierte Ausgabedatei des &quot;Cyclictest&quot; zu nutzen.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Welche Befehle sind in der Komm"
                        "andozeile implementiert?</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Folgende Befehle k\u00f6nnen derzeit verwendet werden:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-family:'Courier New';\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">show x:y</li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Zeigt die Werte des Datensatzes an, von x bis y.</p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-family:'Courier New';\" style=\" "
                        "margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">exit</li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Beendet das Programm.</p></body></html>", None))
    # retranslateUi

