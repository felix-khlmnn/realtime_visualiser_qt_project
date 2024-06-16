# This Python file uses the following encoding: utf-
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QWidget
from PySide6.QtCharts import QChart, QLineSeries, QChartView, QValueAxis, QLogValueAxis
from PySide6.QtGui import QPainter

class ChartWidget(QWidget):

    defaultMaxX = 400
    defaultMaxY = 10.0e8

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

    def displaySeries(self, series_list: list[QLineSeries]):

        axisX = QValueAxis()
        axisY = QLogValueAxis()

        for series in series_list:
            self.chart.addSeries(series)

        # Configure the X-axis

        axisX.setLabelFormat("%d")
        axisX.setMax(self.defaultMaxX)
        axisX.setMin(0)
        axisX.setTitleText("Latenz in us")

        # Configure the Y-axis
        axisY.setBase(10.0)
        axisY.setLabelFormat("%1.1e")
        axisY.setMax(self.defaultMaxY)
        axisY.setMin(0)
        axisY.setTitleText("Häufigkeit")

        for series in series_list:
            series.attachAxis(axisX)
            series.attachAxis(axisY)

        # Add the axes to the chart
        self.chart.setAxisX(axisX, series_list[0])
        self.chart.setAxisY(axisY, series_list[0])
        self.chart.setAxisX(axisX, series_list[1])
        self.chart.setAxisY(axisY, series_list[1])
