# This Python file uses the following encoding: utf-8
from PySide6.QtCharts import QLineSeries, QValueAxis, QLogValueAxis

class ChartData:

    # Values from the parser
    histogramData: list[list[int]] = []

    # Values to be displayed
    chartDataSeries: list[QLineSeries] = []

    # Constraints for the axes
    defaultMaxX = 400
    defaultMaxY = 10.0e8

    def __init__(self, histogramData: list[list[int]]):
        """
        When initialised, the ChartData class takes the histogram values of the parsed histogram file as an argument.
        """
        self.histogramData = histogramData


    def convertHistogramDataToDataSeries(self, maxValues: list[int], minValues: list[int]):
        # Clear the chart data series
        self.chartDataSeries = []

        # Add as many empty series objects as there are processors
        # This can again be determined by the length of the first list in the histogram data
        count_of_processors = len(self.histogramData[0])

        print(count_of_processors)

        for processor in range(count_of_processors):
            self.chartDataSeries.insert(processor, QLineSeries())
            # Set the name
            self.chartDataSeries[processor].setName(f"Prozessor {processor}")

            # self.chartDataSeries[i].append(10, 1)
            # self.chartDataSeries[i].append(20, 10)
            # self.chartDataSeries[i].append(30, 100)
            # self.chartDataSeries[i].append(40, 1000)

            # Add the data
            for index, dataset in enumerate(self.histogramData):
                latency_of_current_processor = dataset[processor]


                # If we're at the minimum or the maximum, insert a 0 before/after
                if (index + 1) == minValues[processor]:
                    print("MIN")
                    self.chartDataSeries[processor].append(index, 1)
                elif (index + 1) == maxValues[processor]:
                    print("MAX")
                    self.chartDataSeries[processor].append(index, 1)

                # Leave out the latencies that are never hit, as a logarithmic scale can't display 0
                if latency_of_current_processor == 0:
                    continue

                self.chartDataSeries[processor].append(index, latency_of_current_processor)
                #print(index, "|", latency_of_current_processor)
                #print(self.chartDataSeries[processor])


    def getChartDataSeries(self):
        return self.chartDataSeries
