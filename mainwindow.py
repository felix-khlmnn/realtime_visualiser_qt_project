# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

# Import of the generated UI class
from ui_mainwindow import Ui_MainWindow

# Functions that are triggered by actions
from Qt_Gui_Functions.ActionFunctions import ActionFunctions

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)  # Setup the UI


        self.actionFunctions = ActionFunctions(self.chartWidget, self.measurementInformationTable)

        # Connect the actions to their respective functions
        self.actionProgramm_beenden.triggered.connect(self.actionFunctions.programmBeenden)
        self.actionHistogrammdatei_laden.triggered.connect(self.actionFunctions.histogrammDateiLaden)

        # Set up the input output system
        self.inputLine.setOutputList(self.outputList)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
