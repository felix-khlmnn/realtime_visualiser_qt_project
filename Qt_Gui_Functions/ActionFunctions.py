# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QFileDialog

from HelperFunctions import DebugTools

from Parsing.dataparser import DataParser

from Charts.chartdata import ChartData

from chartwidget import ChartWidget

from measurementinformationtable import MeasurementInformationTable

class ActionFunctions:

    def __init__(self, chartWidget: ChartWidget, measurementInformationTable: MeasurementInformationTable):
        self.chartWidget = chartWidget
        self.measurementInformationTable = measurementInformationTable


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
            print("Length of parsed data:", len(parsedData.values[0]))
            print("Length of chart data:", len(chartData.chartDataSeries))

            maxValues = parsedData.maximumLatencies
            minValues = parsedData.minimumLatencies

            chartData.convertHistogramDataToDataSeries(maxValues, minValues)

            self.chartWidget.clearGraph()

            # Set the chart display to the converted data
            self.chartWidget.displaySeries(chartData.getChartDataSeries())

            # Update the table data
            self.measurementInformationTable.updateValue(0, 0, parsedData.maximumLatencies)
            self.measurementInformationTable.updateValue(0, 1, parsedData.minimumLatencies)
            self.measurementInformationTable.updateValue(0, 2, parsedData.averageLatencies)
            self.measurementInformationTable.updateValue(0, 3, parsedData.standardDeviations)


        except FileNotFoundError:
            # The user cancelled the file selection, return an empty string
            DebugTools.debugPrint("No file selected")
            self.fileSelection_To_DataParser.histogramData = ""
