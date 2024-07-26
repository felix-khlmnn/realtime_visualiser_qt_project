# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem

class MeasurementInformationTable(QTableWidget):
    def __init__(self, parent=None):
        super(MeasurementInformationTable, self).__init__(parent)

        self.initUi()

    def initUi(self):
        # Set up the table
        self.setRowCount(4)
        self.setColumnCount(1)

        # Set headers
        self.setHorizontalHeaderLabels(['Wert pro Prozessor'])
        self.setVerticalHeaderLabels(['Maximum','Minimum', 'Durchschnitt', 'Standardabweichung'])

        # Strech to fill remaining space
        self.horizontalHeader().setStretchLastSection(True)

        # Set items
        self.setItem(0, 0, QTableWidgetItem())
        self.setItem(1, 0, QTableWidgetItem())
        self.setItem(2, 0, QTableWidgetItem())
        self.setItem(3, 0, QTableWidgetItem())

    def updateValue(self, row, column, values: list[float]):
        """
        This function takes a vector of float values!
        """
        # Try to update the row and column
        itemToBeUpdated = self.item(row, column)

        newString = ''
        for value in values:
            newString += f"{value:.3f}" + "\t"

        try:
            itemToBeUpdated.setText(newString)
        except Exception:
            # Item doesn't exist yet, create new
            self.setItem(row, column, QTableWidgetItem(newString))
