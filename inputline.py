# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QLineEdit
from outputlist import OutputList

class InputLine(QLineEdit):

    outputList: OutputList = None

    def __init__(self, parent=None):
        super(InputLine, self).__init__(parent)
        self.returnPressed.connect(self.onReturnPressed)

    def setOutputList(self, outputList: OutputList):
        """
        Store the output list of the window
        """
        self.outputList = outputList

    def onReturnPressed(self):
        """
        Called when Return is pressed in the Line Edit.
        """

        self.parseCommand(self.text())

    def parseCommand(self, cmd: str):
        """
        Parses the command.
        """

        # Echo the command
        self.outputList.printToOut(cmd)

        # Empty the input line
        self.setText("")

        # Split the command to be able to analyse it
        splitCmd = cmd.split(" ")

        # Check if valid number of args was supplied
        if len(splitCmd) > 2:
            self.outputList.printToOut("Invalid number of arguments:", len(splitCmd) - 1)

        match splitCmd[0]:
            case "show":
                self.showValue(int(splitCmd[1]))
            case "exit":
                sys.exit(0)



    def showValue(self, index: int):
        self.outputList.printToOut("\tShowing value(s) at index", index)
