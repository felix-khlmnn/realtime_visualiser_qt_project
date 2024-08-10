# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QLineEdit
from outputlist import OutputList

from Parsing.datatypes import ParsedCyclictestData

class InputLine(QLineEdit):

    outputList: OutputList = None

    currentCyclictestData: ParsedCyclictestData = None

    def __init__(self, parent=None):
        super(InputLine, self).__init__(parent)
        self.returnPressed.connect(self.onReturnPressed)

    def setOutputList(self, outputList: OutputList):
        """
        Store the output list of the window
        """
        self.outputList = outputList

    def setCurrentCyclictestData(self, newCyclictestData):
        """
        Set the new dataset that can be inspected.
        """
        self.currentCyclictestData = newCyclictestData

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
            self.outputList.printToOut("Ungültige Anzahl an Argumenten:", len(splitCmd) - 1)

        match splitCmd[0]:
            case "show":
                # Disable this command if no data is present
                if self.currentCyclictestData is None:
                    self.outputList.printToOut("Es wurde kein Histogramm geladen, bitte laden Sie erst eine Datei über die UI")
                    return
                # Check if a positional argument was given
                if len(splitCmd) != 2:
                    self.outputList.printToOut("\"show\" benötigt genau ein Positionsargument, entweder einen Zahlenwert oder einen Zahlenbereich (wie zum Beispiel 10:15)")
                    return

                # Every check was successful, continue showing values
                self.showValue(splitCmd[1])
            case "exit":
                sys.exit(0)

    def showValue(self, discriminator: str):
        self.outputList.printToOut("Zeige Wert(e) an folgendem Index/folgenden Indizes:", discriminator)

        valueRange = None

        # Determine number of processors to display value on a per-processor basis
        numberOfProcessors = len(self.currentCyclictestData.values[0])

        # Determine whether the discriminator is a simple value or a range of numbers, delimited by a colon (:)
        splitDiscriminator = discriminator.split(":")

        print(splitDiscriminator)
        if len(splitDiscriminator) > 1:
            # Then, we have a range of numbers
            valueRange = range(int(splitDiscriminator[0]), int(splitDiscriminator[-1]) + 1)
        else:
            # Simple value
            valueRange = range(int(splitDiscriminator[0]), int(splitDiscriminator[0]) + 1)


        for processor in range(numberOfProcessors):
            # First, print the processor number to the outputLine
            self.outputList.printToOut(f"Prozessor {processor}:")
            # The text that will be written to the outputList
            output = "["
            for index, value in enumerate(valueRange):
                if index > 0:
                    output += ", "
                output += f"{self.currentCyclictestData.values[value][processor]}"

            output += "]"
            # Once finished, write output to outputList
            self.outputList.printToOut(output)
