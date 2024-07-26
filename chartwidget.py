# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QWidget, QPushButton
from PySide6.QtCharts import QChart, QLineSeries, QChartView, QValueAxis, QLogValueAxis
from PySide6.QtGui import QPainter

class ChartWidget(QWidget):

    defaultMaxX = 400
    defaultMaxY = 10.0e8

    currentlyDisplayedSeries: list[QLineSeries] = []

    axisX: QValueAxis = None
    axisY: QLogValueAxis = None

    axesHaveBeenSet = False

    def __init__(self, parent=None):
        super(ChartWidget, self).__init__(parent)
        self.initUI()

    def initUI(self):
        # Create a QChart instance and add the series to it
        self.chart = QChart()

        # Create a QChartView instance and set the chart on it
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        # Create a layout and add the chart view to the layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.chart_view)
        self.setLayout(self.layout)

        # Add a clear button
        self.clear_button = QPushButton("Clear Graph")
        self.clear_button.clicked.connect(self.clearGraph)
        self.layout.addWidget(self.clear_button)

        # Axis setup
        self.axisX = QValueAxis()
        self.axisY = QLogValueAxis()

        # Configure the X-axis

        self.axisX.setLabelFormat("%d")
        self.axisX.setMax(self.defaultMaxX)
        self.axisX.setMin(0)
        self.axisX.setTitleText("Latenz in us")

        # Configure the Y-axis
        self.axisY.setBase(10.0)
        self.axisY.setLabelFormat("%1.1e")
        self.axisY.setMax(self.defaultMaxY)
        self.axisY.setMin(0)
        self.axisY.setTitleText("Häufigkeit")

    def displaySeries(self, series_list: list[QLineSeries]):

        #self.clearGraph()

        # Store our series
        self.currentlyDisplayedSeries = series_list



        for series in series_list:
            self.chart.addSeries(series)



        # Attach the axes
        for series in series_list:
            series.attachAxis(self.axisX)
            series.attachAxis(self.axisY)

        # Set the axes
        if not self.axesHaveBeenSet:
            for series in series_list:
                self.chart.setAxisX(self.axisX, series)
                self.chart.setAxisY(self.axisY, series)
            self.axesHaveBeenSet = True

    def clearGraph(self):
        # Remove all series from the chart
        print("Clearing graph...")

        # Print current series before clearing
        print(f"Current series count before clearing: {len(self.chart.series())}")
        try:
            while self.chart.series():
                self.chart.removeSeries(self.chart.series()[0])

            # Clear the currently displayed series list
            self.currentlyDisplayedSeries = []

            # Add the axes back to the chart to keep them visible
            #self.chart.addAxis(self.axisX, Qt.AlignBottom)
            #self.chart.addAxis(self.axisY, Qt.AlignLeft)
        except Exception as e:
            print(e)
        # Print current series after clearing
        print(f"Current series count after clearing: {len(self.chart.series())}")
