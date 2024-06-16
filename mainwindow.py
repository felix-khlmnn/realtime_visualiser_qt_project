# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

# Import of the generated UI class
from ui_mainwindow import Ui_MainWindow

# Functions that are triggered by actions
from Qt_Gui_Functions.ActionFunctions import ActionFunctions

# Middleware for exchanging data such as the histogram data
from Middleware.FileSelection_To_DataParser import FileSelection_To_DataParser

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)  # Setup the UI

        self.fileSelection_To_DataParser = FileSelection_To_DataParser()

        self.actionFunctions = ActionFunctions(self.fileSelection_To_DataParser, self.chartWidget)

        # Connect the actions to their respective functions
        self.actionProgramm_beenden.triggered.connect(self.actionFunctions.programmBeenden)
        self.actionHistogrammdatei_laden.triggered.connect(self.actionFunctions.histogrammDateiLaden)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
