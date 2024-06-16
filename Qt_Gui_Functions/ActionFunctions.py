# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QFileDialog

from HelperFunctions import DebugTools

from Middleware.FileSelection_To_DataParser import FileSelection_To_DataParser

from Parsing.dataparser import DataParser

from Charts.ChartData import ChartData

from chartwidget import ChartWidget

class ActionFunctions:

    def __init__(self, fileSelection_To_DataParser: FileSelection_To_DataParser, chartWidget: ChartWidget):
        # Middleware that connects our load histogram function to the dataparser
        # Use the same as the main script
        self.fileSelection_To_DataParser = fileSelection_To_DataParser

        self.chartWidget = chartWidget


    # Programm beenden
    def programmBeenden(self):
        sys.exit(0)

    def histogrammDateiLaden(self) -> str:
        """
        Loads a histogram file and starts parsing
        """
        file_information = QFileDialog.getOpenFileName(None, "Histogrammdatei laden", "C:\\Users\\kuhlmannf\\Documents\\Hochschule_Lokal\\GPY")

        # The file name is stored at the first index of the file_information tuple
        file_name = file_information[0]

        try:
            DebugTools.debugPrint("Loading the following file", file_name)

            dataParser = DataParser(file_path=file_name)

            # Start the read and parse workflow
            # TODO: Refactor into init!
            dataParser.read_file()
            dataParser.parse_data()

            parsedData = dataParser.get_data()
            # Put the data inside of the chart
            chartData = ChartData(parsedData.values)
            maxValues = parsedData.maximumLatencies
            minValues = parsedData.minimumLatencies

            chartData.convertHistogramDataToDataSeries(maxValues, minValues)

            # Set the chart display to the converted data
            self.chartWidget.displaySeries(chartData.getChartDataSeries())

        except FileNotFoundError:
            # The user cancelled the file selection, return an empty string
            DebugTools.debugPrint("No file selected")
            self.fileSelection_To_DataParser.histogramData = ""
