# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QListWidget, QListWidgetItem

class OutputList(QListWidget):
    def __init__(self, parent=None):
        super(OutputList, self).__init__(parent)

    def printToOut(self, *args):
        """
        Takes an arbitrary number of arguments, just like print.
        """
        outStr = ""

        for arg in args:
            outStr += str(arg) + " "

        self.addItem(QListWidgetItem(outStr))

        # Should be called in the end to ensure that newest text is visible
        self.scrollToBottom()

