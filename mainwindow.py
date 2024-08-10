# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

# Import of the generated UI class
from ui_mainwindow import Ui_MainWindow

# Functions that are triggered by actions
from Qt_Gui_Functions.ActionFunctions import ActionFunctions

class MainWindow(QMainWindow, Ui_MainWindow):
    applicationName: str = "Realtime Latency Visualiser v1.0"

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)  # Setup the UI


        self.actionFunctions = ActionFunctions(self.chartWidget, self.measurementInformationTable, self.inputLine, self.outputList)

        self.writeWelcomeMessage()

        # Connect the actions to their respective functions
        self.actionProgramm_beenden.triggered.connect(self.actionFunctions.programmBeenden)
        self.actionHistogrammdatei_laden.triggered.connect(self.actionFunctions.histogrammDateiLaden)

        # Set up the input output system
        self.inputLine.setOutputList(self.outputList)

    def writeWelcomeMessage(self):
        self.outputList.printToOut(f"Willkommen zu {self.applicationName}!\nBitte wählen Sie eine Histogrammdatei aus, um mit der Analyse zu beginnen.")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
